from django.db import models
from ckeditor.fields import RichTextField
from person.models import *


# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Promise(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    text = RichTextField()
    # start_date = models.DateField(auto_now=True)
    finish_date = models.DateField()
    link = models.URLField(verbose_name='Ссылка')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    region = models.ManyToManyField(Region)
    tag = models.ManyToManyField(Tag)
    result = RichTextField(verbose_name='Результат', blank=True, default=None, null=True)
    result_link = models.URLField(verbose_name='Ссылка к результату', blank=True, default=None, null=True)
    vote_up = models.PositiveIntegerField(verbose_name='Верят', default=0)
    vote_down = models.PositiveIntegerField(verbose_name='Не верят', default=0)

    def __str__(self):
        return '%s: %s' % (self.person.surname, self.title)

    class Meta:
        verbose_name = 'Обещание'
        verbose_name_plural = 'Обещания'
