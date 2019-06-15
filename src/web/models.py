from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from slugify import slugify


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PositionMixin(models.Model):
    position = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class NameSlugMixin(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, default='')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class City(NameSlugMixin):
    pass


class Category(CreatedMixin, NameSlugMixin):
    logo = models.ImageField(upload_to='category', blank=True, default='')


class Employer(CreatedMixin, NameSlugMixin):
    legal_form = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=64)
    hr_name = models.CharField(max_length=256)
    trusted = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='employer', blank=True, default='')


class Job(CreatedMixin, NameSlugMixin):
    AGE_CHOICES = (
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
    )

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    age = models.PositiveSmallIntegerField(choices=AGE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=4096, default='')
    salary = models.PositiveSmallIntegerField(blank=True, default=0)

    class Meta:
        ordering = ['created_at', ]


@receiver(pre_save, sender=City)
def city_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name.lower())


@receiver(pre_save, sender=Category)
def category_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name.lower())


@receiver(pre_save, sender=Employer)
def employer_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name.lower())


@receiver(pre_save, sender=Job)
def job_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name.lower())
