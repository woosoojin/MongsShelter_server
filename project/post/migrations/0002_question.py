# Generated by Django 2.1.1 on 2019-07-19 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images2/')),
                ('description2', models.CharField(max_length=10000)),
            ],
        ),
    ]
