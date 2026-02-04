from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roleid = models.IntegerField(choices=[(1, 'Admin'), (2, 'Public')], default=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    genderid = models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], null=True, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username

class HelpPost(models.Model):
    HELP_TYPE = [
        ('need', 'Need Help'),
        ('offer', 'Offer Help'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Emergency'),
        (2, 'Medium'),
        (3, 'Low'),
    ]
    STATUS_CHOICES = [
        (0, 'Open'),
        (1, 'In Progress'),
        (2, 'Closed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    city = models.CharField(max_length=50, default='kathmandu')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    contact = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    help_type = models.CharField(max_length=10, choices=HELP_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db.models.signals import post_save # The "Signal"
from django.dispatch import receiver # The "Receiver"

# This function runs every time a User is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# This function ensures the profile is saved when the user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()