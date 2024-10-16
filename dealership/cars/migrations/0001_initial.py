# Generated by Django 5.1.1 on 2024-10-07 09:25

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=70, verbose_name='Марка')),
                ('model', models.CharField(max_length=70, verbose_name='Модель')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время обновления')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car', verbose_name='Автомобиль')),
            ],
        ),
    ]
