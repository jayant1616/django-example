from django.db import models
#yet to create models

# Create your models here.
#new model to be created

class topics(models.Model):
    topic_name = models.CharField(max_length=240,default='def')
    topic_email= models.EmailField(default='def')
