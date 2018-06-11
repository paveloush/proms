from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Person(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(blank=True, null=True, verbose_name='Zdjecie', upload_to='avatars/')

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Promise(models.Model):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    text = RichTextField()
    start_date = models.DateField()
    finish_date = models.DateField()
    link = models.URLField(verbose_name='Ссылка')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    result = models.TextField(verbose_name='Результат', blank=True, default=None)
    result_link = models.URLField(verbose_name='Ссылка к результату', blank=True, default=None)
    vote_up = models.PositiveIntegerField(verbose_name='Верят', default=0)
    vote_down = models.PositiveIntegerField(verbose_name='Не верят', default=0)

    def __str__(self):
        return '%s: %s' % (self.person.surname, self.title)

    class Meta:
        verbose_name = 'Обещание'
        verbose_name_plural = 'Обещания'


class Region(models.Model):
    name = models.CharField(max_length=30)
    promise = models.ForeignKey(Promise, on_delete=models.PROTECT)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    promise = models.ForeignKey(Promise, on_delete=models.PROTECT)


class Ip(models.Model):
    ip = models.GenericIPAddressField()
    promise = models.ForeignKey(Promise, on_delete=models.SET('0.0.0.0'))
