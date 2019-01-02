from django.db import models

# Create your models here.
class Item(models.Model):
    # Text based input with rules set
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        #Creates a human readable name for each item in admin page
        return self.name