from __future__ import unicode_literals
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

# models
class Category(models.Model):
    type = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User)

class Basket(models.Model):
    user = models.ForeignKey(User)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    total = models.FloatField()

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, addressline1, addressline2, city, phone, password=None):

        if not email:
            raise ValueError('User needs to have an email address')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          addressline1=addressline1, addressline2=addressline2, city=city, phone=phone,
                          password=password)
        user.set_password(password)
        user.save(using=self._db)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, addressline1, addressline2, city, phone, password=None):

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name,
                          addressline1=addressline1, addressline2=addressline2, city=city, phone=phone,
                          password=password)
        user.set_password(password)
        user.is_admin = True
        user.admin_permission = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    addressline1 = models.TextField(max_length=55, blank=True)
    addressline2 = models.TextField(max_length=55, blank=False)
    city = models.CharField(max_length=30, blank=True)
    phone = models.TextField(max_length=11, blank=True)

    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'addressline1', 'addressline2', 'city', 'phone']


    def get_full_name(self):
        return self.first_name + ' ' +self.last_name

    def get_short_name(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    def __str__ (self):
        return self.email


# models
class Category(models.Model):
    type = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User)

class Basket(models.Model):
    user = models.ForeignKey(User)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    total = models.FloatField()
