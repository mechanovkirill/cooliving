from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Users creating
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, username, email, password=None):
        if not email:
            raise ValueError('User mast have an email adress')
        if not username:
            raise ValueError('User mast have username')
        user = self.model(
            email=self.normalize_email(email),  # приводит имэйл к нижнему регистру
            username=username,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_stuff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


# Account model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=256, unique=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

    def is_staff(self):
        return self.is_admin
"""
Не забыть прописать в файле настроек AUTH_USER_MODEL = 'accounts.Account' 
"""

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(blank=True, null=True, upload_to='userprofile')

    def __str__(self):
        return self.user.first_name


