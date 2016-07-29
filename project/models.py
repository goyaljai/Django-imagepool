from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
import os


def get_image_path(instance, filename):
    return os.path.join('profile_pictures', filename)


def get_image_path2(instance, filename):
    return os.path.join('user_images',  filename)


class SiteUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    profile_picture = models.FileField(upload_to=get_image_path ,  null=True, blank=True)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Image(models.Model):
    image = models.FileField(upload_to=get_image_path2 ,  null=True, blank=True)
    caption = models.TextField(max_length=1000)
    like_count = models.IntegerField(default=0)
    CHOICES = (
        ('Pub', 'Public'),
        ('Pri', 'Private'),
    )

    access_users = models.CharField(max_length=3, choices=CHOICES, null=True)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.user.pk})

    def __str__(self):
        return str(self.caption)


class Liker(models.Model):
    user = models.ForeignKey(SiteUser,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Follow(models.Model):
    user = models.ForeignKey(SiteUser,on_delete=models.CASCADE)
    follower = models.ForeignKey(SiteUser,related_name="follower",on_delete=models.CASCADE)

    # follower ki followings mein user aa jaayega and user ki follows mein follower aa jaaega

    def __str__(self):
        return str(self.pk)
