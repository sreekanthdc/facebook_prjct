# Generated by Django 2.2.3 on 2019-07-12 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('sureName', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=10)),
                ('fklogin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebookapp.UserData')),
            ],
        ),
    ]
