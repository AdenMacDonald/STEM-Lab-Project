# Generated by Django 4.2.7 on 2023-12-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], default='Monday', max_length=10)),
                ('time', models.CharField(choices=[('8:00-9:00 AM', '8:00-9:00 AM'), ('9:00-10:00 AM', '9:00-10:00 AM'), ('10:00-11:00 AM', '10:00-11:00 AM'), ('11:00-12:00 PM', '11:00-12:00 PM'), ('12:00-1:00 PM', '12:00-1:00 PM'), ('1:00-2:00 PM', '1:00-2:00 PM'), ('2:00-3:00 PM', '2:00-3:00 PM'), ('3:00-4:00 PM', '3:00-4:00 PM'), ('4:00-5:00 PM', '4:00-5:00 PM'), ('5:00-6:00 PM', '5:00-6:00 PM')], default='9:00-10:00 AM', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('subjects', models.ManyToManyField(to='homepage.subject')),
                ('tutoring_times', models.ManyToManyField(to='homepage.timeslot')),
            ],
        ),
    ]
