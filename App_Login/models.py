from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy 



class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The email Must Be Set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('SuperUser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('SuperUser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True, null=False)
    is_staff = models.BooleanField(ugettext_lazy('Staff Status'), default=False, 
        help_text = ugettext_lazy('Designates whether the user can log in the site')
    )
    
    is_active = models.BooleanField(ugettext_lazy('active'), 
        help_text = ugettext_lazy('Designates whether this user should be treatea as active')
    )


    USERNAME_FIELD = 'email'
    objects = MyUserManager()


    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    username = models.CharField(max_length=264, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    address_1 = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=40, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=20, blank=True)
    phone = models.CharField(maxLength=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.username + "'s Profile"


    




