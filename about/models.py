from django.db import models

# Create your models here.
class AboutModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    profile_image = models.ImageField(upload_to='portfolio/images')
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name;
