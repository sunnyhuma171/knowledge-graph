# Generated by Django 2.0.2 on 2018-10-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Triples',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_text', models.CharField(max_length=200)),
                ('predicts_text', models.CharField(max_length=200)),
                ('object_text', models.CharField(max_length=200)),
            ],
        ),
    ]
