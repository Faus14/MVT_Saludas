# Generated by Django 4.0.3 on 2022-03-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='nombre')),
                ('canada', models.IntegerField(verbose_name='Canada')),
            ],
        ),
    ]
