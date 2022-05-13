# Generated by Django 3.0.5 on 2020-04-18 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='test')),
            ],
        ),
    ]
