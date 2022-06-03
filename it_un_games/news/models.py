from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    city = models.CharField('Город', max_length=250)
    desc = models.TextField('Описание')
    tags = models.CharField('Теги', max_length=50)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'