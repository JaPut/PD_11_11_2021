# Generated by Django 3.2.8 on 2021-11-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=77)),
                ('e_mail', models.EmailField(max_length=78)),
            ],
        ),
    ]
