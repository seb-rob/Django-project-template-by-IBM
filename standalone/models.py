from django.db import models

# Test Model
class Test(models.Model):
    name = models.CharField(max_length = 30)
