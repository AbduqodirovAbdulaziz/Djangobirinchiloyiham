# Generated by Django 5.0.1 on 2024-02-03 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sotuv', '0011_imtixon_natija_nazoratchi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('familiya', models.CharField(max_length=30)),
                ('jinsi', models.CharField(choices=[('ayol', 'ayol'), ('erkak', 'erkak')], max_length=10)),
                ('yosh', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=35)),
                ('credit', models.IntegerField()),
                ('oqituvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sotuv.ustoz')),
            ],
        ),
    ]
