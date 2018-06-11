from django.db import models


# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(blank=True, null=True, verbose_name='Zdjecie', upload_to='avatars/')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)
