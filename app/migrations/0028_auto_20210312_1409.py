# Generated by Django 3.1.7 on 2021-03-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20210312_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(choices=[(1, 'Алмазарский район'), (2, 'Бектемирский район'), (3, 'Мирабадский район'), (4, 'Мирзо-Улугбекский район'), (5, 'Сергелийский район'), (6, 'Учтепинский район'), (7, 'Чиланзарский район'), (8, 'Шайхантахурский район'), (9, 'Юнусабадский район'), (10, 'Яккасарайский район'), (11, 'Яшнабадский район')], max_length=100),
        ),
    ]