# Generated by Django 4.1.7 on 2023-04-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('contenido', models.CharField(max_length=60)),
                ('imagen', models.ImageField(upload_to='inicio')),
            ],
        ),
    ]
