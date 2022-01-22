from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import translit


class Dino(models.Model):
    name = models.CharField(max_length=40)                 # название
    view = models.CharField(max_length=20)                 # привязка к пище
    detachment = models.CharField(max_length=20)           # отряд
    suborder = models.CharField(max_length=20)             # подотряд
    family = models.CharField(max_length=20)               # семейство
    genus = models.CharField(max_length=20)                # род
    height = models.FloatField()                           # высота
    length = models.FloatField()                           # длина
    weight = models.FloatField()                           # вес
    description = models.CharField(max_length=10000)       # описание
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, "ru", reversed=True))
        super(Dino, self).save(*args, kwargs)

    def get_url(self):
        return reverse('dino_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name}'


#  Dino(name='', view='', detachment='', suborder='', family='', genus='', height=, length=, weight=, description='').save()