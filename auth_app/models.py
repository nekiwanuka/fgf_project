"""
Users and Authentication Models
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,Group, Permission, PermissionsMixin)
import uuid
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.core.mail import send_mail
# from core.mixins.model_mixins import Registrable
# from core.utilities.unique_code_generators import UniqueMonotonicCodeGenerator
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given  email, and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Email and password are required. Other fields are optional.
    """
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    Id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=False,
        null=True,
        blank=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=gender_choices, blank=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )

    is_admin = models.BooleanField(
        _('FGF system Administrator status'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as a FGF system Administrator.')
    )

    is_contributor = models.BooleanField(
        _('Contributor status'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as a Contributor')
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.Id = uuid.uuid4()
        super(User, self).save()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='user_groups'  # Add related_name here
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='user_permissions'  # Add related_name here
    )

    # class Meta:
    #     # db_table = 'User'
    #     ordering = ['-joined_at']
    # End class Meta

    # PK added
    def is_administrator(self):
        return self.is_admin

    def is_contributor(self):
        return self.is_contributor


class Administrator(models.Model):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Administrator, self).save()

    #PK added
    def is_administrator(self):
        return True

    def __str__(self):
        return f'{self.user}'


class Contributor(models.Model):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Contributor, self).save()

    def is_contributor(self):
        return True
    
    def __str__(self):
        return f'{self.user}'


class PasswordResetInfo(models.Model):
    """
    The PasswordResetInfo Model:
        Lays specifications of how the PasswordResetInfo Entity / Table Should be Created in the Database.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6, default='000000', unique=True)
    created_at = models.DateTimeField(default=timezone.now)    
    expires_at = models.DateTimeField(
        default=(timezone.now() + timezone.timedelta(hours=24)))

    def __str__(self):
        _str = ''
        if(self.user.first_name or self.user.last_name):
            if self.user.first_name:
                _str += self.user.first_name
            if self.user.last_name:
                _str += ' ' + self.user.last_name
        if self.user.email:
            _str += ' ' + self.user.email + ''
        if self.reset_code:
            _str += ' (' + str(self.reset_code) + ')'
        return _str

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self._state.adding:
            CodeGenerator = UniqueMonotonicCodeGenerator()
            self.reset_code = CodeGenerator.generate()
            self.expires_at = (timezone.now() + timezone.timedelta(hours=24))
        super(PasswordResetInfo, self).save()

    class Meta:
        verbose_name_plural = 'Password Reset Info'
        ordering = ['user']
    # End class Meta