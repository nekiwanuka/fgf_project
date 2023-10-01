from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Choices for fields
REGION_CHOICES = [
    ('', 'Select Region'),
    ('Northern Uganda', 'Northern Uganda'),
    ('West Nile', 'West Nile'),
    ('Central Uganda', 'Central Uganda'),
    ('Eastern Uganda', 'Eastern Uganda'),
    ('Western Uganda', 'Western Uganda'),
    ('All Regions', 'All Regions'),
]

LIFE_FORM_CHOICES = [
    ('', 'Select Life Form'),
    ('shrub', 'Shrub'),
    ('tree', 'Tree'),
    ('herb', 'Herb'),
    ('grass', 'Grass'),
    ('climber', 'Climber'),
    ('other', 'Other'),
]

VALUE_CHOICES = [
    ('', 'Select Value'),
    ('ecological', 'Ecological'),
    ('social', 'Social'),
    ('economic', 'Economic'),
    ('nutritional', 'Nutritional'),
    ('other', 'Other'),
]

class Plant(models.Model):
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    region = models.CharField(max_length=50, choices=REGION_CHOICES)
    unique_habitat = models.CharField(max_length=250)
    life_form = models.CharField(max_length=250, choices=LIFE_FORM_CHOICES)
    specify_other_life_form = models.CharField(max_length=250, blank=True, null=True)
    value = models.CharField(max_length=250, choices=VALUE_CHOICES)
    if_other_value_specify = models.CharField(max_length=250, blank=True, null=True)
    value_details = models.CharField(max_length=250, blank=True, null=True)
    climate_impact = models.CharField(max_length=250)
    research_notes = models.TextField()
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    PUBLISH_CHOICES = [
        ('', 'Select Publishing Preference'),
        ('name_and_email', 'Name and Email'),
        ('name_only', 'Name Only'),
        ('none', 'Do Not Publish'),
    ]
    publish_preference = models.CharField(max_length=20, choices=PUBLISH_CHOICES, default='', blank=True, null=True)

    def __str__(self):
        return self.english_name

class PlantName(models.Model):
    plant = models.ForeignKey(Plant, related_name='plant_names', on_delete=models.CASCADE)
    local_name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.local_name} ({self.language})"

class MedicinalPlant(models.Model):
    medicinal_values_entered = models.BooleanField(default=False)
    health_issues = models.TextField(blank=True, help_text='Add multiple health issues, separated by commas')
    part_used_for_health_issues = models.TextField(blank=True, help_text='Part of the plant used for each health issue')
    preparation_steps = models.TextField(blank=True, help_text='Preparation steps for each health issue')
    dosage = models.TextField(blank=True, help_text='Dosage for each health issue')
    contraindications = models.TextField(blank=True, help_text='Contraindications for each health issue')
    shelf_life = models.CharField(max_length=100, blank=True, help_text='Shelf life of the prepared medicine')
    notes = models.TextField(blank=True, help_text='Additional notes for medicinal values')
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Check if medicinal values are provided and update the flag accordingly
        self.medicinal_values_entered = bool(
            self.health_issues
            or self.part_used_for_health_issues
            or self.preparation_steps
            or self.dosage
            or self.contraindications
            or self.shelf_life
            or self.notes
        )
        # Ensure only one entry per plant
        if self.id and MedicinalPlant.objects.filter(plant=self.plant).exclude(id=self.id).exists():
            raise ValueError("A medicinal values entry already exists for this plant. Update the existing entry.")

        super().save(*args, **kwargs)

    def __str__(self):
        english_name = self.plant.english_name if self.plant else "No English Name"
        scientific_name = self.plant.scientific_name if self.plant else "No Scientific Name"
        local_names = ', '.join([plant_name.local_name for plant_name in self.plant.plant_names.all()]) if self.plant else "No Local Names"
        
        return f"Medicinal Plant: English Name: {english_name}, Scientific Name: {scientific_name}, Local Names: {local_names},"
