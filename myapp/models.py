from django.db import models
import uuid
# Create your models here.
class Addservice(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_name = models.CharField(max_length=100,blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    service_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.service_name