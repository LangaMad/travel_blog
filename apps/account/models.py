from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField('Никнейм',max_length=20, unique=True)
    email = models.EmailField('Почта',unique=True)
    avatar = models.ImageField('Фото профиля',upload_to='avatars/', null=True, blank=True)
    bio = models.TextField('Биография',null=True, blank=True)
    phone = models.CharField('Телефон', max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField('Возраст', null=True, blank=True)
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)
    
    objects = UserManager()

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []







