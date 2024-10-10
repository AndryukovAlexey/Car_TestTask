from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    make = models.CharField('Марка', max_length=70)
    model = models.CharField('Модель', max_length=70)
    year = models.IntegerField("Год выпуска", blank=True, null=True)
    description = models.TextField("Описание")
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата и время обновления", auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор записи")

    def __str__(self):
        return f'{self.make} {self.model}'

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Comment(models.Model):
    content = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата и время создания", auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
    def __str__(self):
        return f'{self.car.make} {self.car.model} {self.author}'
    