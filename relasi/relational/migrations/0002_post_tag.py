# Generated by Django 3.1.3 on 2022-06-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relational', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('tag', models.ManyToManyField(to='relational.Tag')),
            ],
        ),
    ]