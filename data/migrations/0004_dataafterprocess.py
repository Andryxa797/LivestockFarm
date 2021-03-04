# Generated by Django 3.1.7 on 2021-03-02 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0003_remove_databeforeprocess_audiofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataAfterProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeartBeat', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Количество сердцебиений')),
                ('CowCondition', models.IntegerField(verbose_name='Состояние коровы')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Обработанные данные',
                'verbose_name_plural': 'Обработанные данные',
            },
        ),
    ]
