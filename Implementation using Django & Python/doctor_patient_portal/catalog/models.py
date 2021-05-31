from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns


class AccountInfo(models.Model):
    # Create your models here.

    TYPE_CHOICES = (
        ('DO', 'Doctor'),
        ('PA', 'Patient'),
        )

    # Fields
    uid=models.CharField(max_length=15, help_text='Enter ID')
    upassword=models.CharField(max_length=20, help_text='Enter password')
    name=models.CharField(max_length=20, help_text='Enter your name')
    type=models.CharField(max_length=2, choices=TYPE_CHOICES)
    location=models.CharField(max_length=30, help_text='Enter your location')
    email=models.EmailField()

    class Meta:
        ordering = ['name']

    # Methods
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('accountInfo-detail', args=[str(self.uid)])

