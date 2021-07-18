# from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("User must have an email!")
#         if not password:
#             raise ValueError("User must have a password!")
#
#         user = self.email(
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.isStaff = False
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None):
#         if not email:
#             raise ValueError("User must have an email!")
#         if not password:
#             raise ValueError("User must have a password!")
#
#         user = self.model(
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # email = models.CharField(max_length=255, unique=True)
    # password = models.CharField(max_length=255)

    isClient = models.BooleanField(default=True)
    isManager = models.BooleanField(default=False)
    isBailleur = models.BooleanField(default=False)
    numTel = models.CharField(max_length=200)

    # username = None

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    # objects = UserManager()


# class Manager(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Client(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Bailleur(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    libelle = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.libelle


class Announce(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photos/", null=True, blank=True)
    bailleur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bailleur', default=1)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager', default=1)
    quartier = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ville = models.CharField(max_length=200)
    region = models.CharField(max_length=200, default="Littoral")
    available = models.BooleanField(default=True)
    validated = models.BooleanField(default=False)

    def __str__(self):
        return "Announce number {0}".format(self.id)


class Comment(models.Model):
    author = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    def __str__(self):
        return "Comment of {0}, id is {1}".format(self.announce.title, self.id)


class Logement(models.Model):
    superficie = models.CharField(max_length=200)
    price = models.IntegerField()
    meuble = models.BooleanField(default=False)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Logement cree le {0}".format(self.created_at)


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date_of_visit = models.DateField()
    validation_of_meet = models.BooleanField(default=False)
    effectivity_of_meet = models.BooleanField(default=False)
    client_visit = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_visit')
    manager_visit = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager_visit', default=1)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    def __str__(self):
        return "Visit of {0} with {1}".format(self.client_visit.first_name, self.manager_visit.first_name)


class Location(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    announce = models.ForeignKey(Announce, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
