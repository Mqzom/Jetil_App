from django.db import models

# Create your models here.

class CustomerInfo(models.Model):
    name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class FreeLesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='lesson_images/')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses_images/')
    discount = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='teacher_images/')

    def __str__(self):
        return self.name