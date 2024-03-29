# Generated by Django 5.0.1 on 2024-01-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sotuv', '0002_universiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universiter',
            name='nomi',
            field=models.CharField(choices=[('HP', 'HP'), ('Acer', 'Acer'), ('Asus', 'Asus'), ('Lenovo', 'Lenovo')], max_length=100),
        ),
        migrations.AlterField(
            model_name='universiter',
            name='rasmi',
            field=models.FileField(blank=True, null=True, unique=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='universiter',
            name='yillik',
            field=models.CharField(default=4, max_length=2),
        ),
    ]
