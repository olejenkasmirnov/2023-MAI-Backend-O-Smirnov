from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    foundation_date = models.DateField(verbose_name='Дата основания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клуб"
        verbose_name_plural = "Клубы"


class Player(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Пол')
    age = models.IntegerField(verbose_name='Возраст')
    club = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name='Клуб')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"


class Match(models.Model):
    city = models.CharField(max_length=100, verbose_name='Город')
    date = models.DateField(verbose_name='Дата')
    players = models.ManyToManyField(Player, verbose_name='Игроки')

    def __str__(self):
        return f'{self.city} {self.date}'

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"
