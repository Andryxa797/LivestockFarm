from django.contrib.auth.models import User
from django.db import models


class DataBeforeProcess(models.Model):
    Cepstral = models.BinaryField(blank=True, verbose_name="Кепстральные коэффициенты")
    BatteryStation = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,
                                         verbose_name="Заряд аккумулятора")
    NewPost = models.BooleanField(default=True, verbose_name="Новый пост")
    DataTimeCreate = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE,
                             verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Первичные данные'
        verbose_name_plural = 'Первичные данные'


class DataAfterProcess(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE,
                             verbose_name="Пользователь")
    HeartBeat = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,
                                    verbose_name="Количество сердцебиений")
    CowCondition = models.IntegerField(verbose_name="Состояние коровы")

    class Meta:
        verbose_name = 'Обработанные данные'
        verbose_name_plural = 'Обработанные данные'
