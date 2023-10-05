from django.db import models
from django.contrib.auth.models import User

class Value(models.Model):
    ECOLOGICAL = 'ecological'
    SOCIAL = 'social'
    ECONOMIC = 'economic'
    NUTRITIONAL = 'nutritional'
    OTHER = 'other'

    VALUE_CHOICES = [
        (ECOLOGICAL, 'Ecological'),
        (SOCIAL, 'Social'),
        (ECONOMIC, 'Economic'),
        (NUTRITIONAL, 'Nutritional'),
        (OTHER, 'Other'),
    ]

    value = models.CharField(
        max_length=50,
        choices=VALUE_CHOICES,
    )

    def __str__(self):
        return self.get_value_display()

class Plant(models.Model):
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    region = models.ManyToManyField('Region', related_name='plants', blank=True)
    life_form = models.ManyToManyField('LifeForm', related_name='plants', blank=True)
    unique_habitat = models.CharField(max_length=250)
    values = models.ManyToManyField(Value, through='ValueDetail', related_name='plants')
    other_value_details = models.ManyToManyField('OtherValueDetail', related_name='plants')
    climate_impact = models.CharField(max_length=250)
    research_notes = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to='media_files')
    videos = models.FileField(null=True, blank=True, upload_to='media_files')
    audio = models.FileField(null=True, blank=True, upload_to='media_files')
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.english_name} {self.scientific_name}"

class Region(models.Model):
    NORTHERN_UGANDA = 'Northern Uganda'
    WEST_NILE = 'West Nile'
    CENTRAL_UGANDA = 'Central Uganda'
    EASTERN_UGANDA = 'Eastern Uganda'
    WESTERN_UGANDA = 'Western Uganda'
    ALL_REGIONS = 'All Regions'

    REGION_CHOICES = [
        (NORTHERN_UGANDA, 'Northern Uganda'),
        (WEST_NILE, 'West Nile'),
        (CENTRAL_UGANDA, 'Central Uganda'),
        (EASTERN_UGANDA, 'Eastern Uganda'),
        (WESTERN_UGANDA, 'Western Uganda'),
        (ALL_REGIONS, 'All Regions'),
    ]

    regions = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        default=ALL_REGIONS,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.get_regions_display()

class LifeForm(models.Model):
    SHRUB = 'shrub'
    TREE = 'tree'
    HERB = 'herb'
    GRASS = 'grass'
    CLIMBER = 'climber'
    OTHER = 'other'

    LIFE_FORM_CHOICES = [
        (SHRUB, 'Shrub'),
        (TREE, 'Tree'),
        (HERB, 'Herb'),
        (GRASS, 'Grass'),
        (CLIMBER, 'Climber'),
        (OTHER, 'Other'),
    ]

    life_form = models.CharField(
        max_length=50,
        choices=LIFE_FORM_CHOICES,
        default=OTHER,
    )

    other_life_form_description = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Specify other life form (if selected "Other")'
    )

    def __str__(self):
        if self.life_form == self.OTHER and self.other_life_form_description:
            return f"Other: {self.other_life_form_description}"
        return self.get_life_form_display()

class ValueDetail(models.Model):
    value = models.ForeignKey(Value, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)  # Added this foreign key
    details = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.value} Detail: {self.details}"

class OtherValueDetail(models.Model):
    other_value = models.CharField(max_length=50)
    details = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.other_value} Detail: {self.details}"

class PlantLocalName(models.Model):
    plant = models.ForeignKey(Plant, related_name='plant_local_names', on_delete=models.CASCADE)
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
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    plant = models.OneToOneField(Plant, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.medicinal_values_entered = bool(
            self.health_issues
            or self.part_used_for_health_issues
            or self.preparation_steps
            or self.dosage
            or self.contraindications
            or self.shelf_life
            or self.notes
        )
        if self.id and MedicinalPlant.objects.filter(plant=self.plant).exclude(id=self.id).exists():
            raise ValueError("A medicinal values entry already exists for this plant. Update the existing entry.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Medicinal Plant: {self.plant.english_name if self.plant else 'No English Name'}, {self.plant.scientific_name if self.plant else 'No Scientific Name'}"
