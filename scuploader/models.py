from django.db import models

class Photo(models.Model):
    user = models.ForeignKey(User, db_index=True)
    photo = models.ImageField(upload_to='photos/%Y%m%d', db_index=True)