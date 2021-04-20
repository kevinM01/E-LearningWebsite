# Generated by Django 3.1.7 on 2021-04-20 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file_field', models.FileField(upload_to='uploads/')),
                ('desc', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.faculty')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
