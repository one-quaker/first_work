from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PositionMixin(models.Model):
    position = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Category(CreatedMixin):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Employer(CreatedMixin):
    name = models.CharField(max_length=64)
    legal_form = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=64)
    hr_name = models.CharField(max_length=256)
    trusted = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='employer', blank=True, default='')

    def __str__(self):
        return self.name


class Job(CreatedMixin):
    AGE_CHOICES = (
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
    )

    name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=4096, default='')
    salary = models.PositiveSmallIntegerField(blank=True, default=0)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.name
