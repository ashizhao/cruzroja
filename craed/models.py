from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse

#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

Tijuana = Point(-117.0382, 32.5149, srid=4326)

# Create your models here.

class AED(models.Model):
    name          = models.CharField(max_length=254)
    description   = models.CharField(max_length=254, blank=True)
    location      = models.PointField(srid=4326, default=Tijuana)
    address       = models.CharField(max_length=254, blank=True)
    number        = models.PositiveIntegerField(blank=True, null=True)
    neighborhood  = models.CharField(max_length=100, blank=True)
    city          = models.CharField(max_length=100, default='Tijuana')
    state         = models.CharField(max_length=3, default='BN')
    country       = models.CharField(max_length=2, default='MX')
    public        = models.BooleanField(default=True)
    zipcode       = models.CharField(max_length=10)
    contact       = models.ForeignKey(User,
                                      on_delete=models.CASCADE)
    verified      = models.BooleanField(default=False)
    date_created  = models.DateField(auto_now_add=True)
    date_verified = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return "{} ({:9.6f}, {:9.6f})".format(self.name, 
                                              self.location.x,  #long
                                              self.location.y); #lat
        
class Photos(models.Model):
    aed   = models.ForeignKey(AED, 
                              on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'photos/', 
                              default = 'photos/None/no-img.jpg')

    def __str__(self):
        return "{}. {}".format(self.aed, self.photo);
