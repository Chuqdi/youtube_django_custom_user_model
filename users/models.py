from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser




class UserManager(BaseUserManager):
    def create_user(self, email, username, password, phone_number, **extra_fields):
        if not email:
            raise ValueError("Please enter an email")
        
        if not username:
            raise ValueError("Please enter an username")
        
        if not password:
            raise ValueError("Please enter an password")
        
        if not phone_number:
            raise ValueError("Please enter an phone_number")
        

        email = self.normalize_email(email)

        user = self.model(
            username = username,
            email = email,
            phone_number = phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password, phone_number, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        user = self.create_user(email, username, password, phone_number, **extra_fields)
        return user




class User(AbstractUser):
    phone_number = models.CharField(null=False, blank=False, max_length=30)

    USERNAME_FIELD ="username"
    REQUIRED_FIELDS = ["phone_number", "email"]

    objects = UserManager()

    def __str__(self) -> str:
        return self.email