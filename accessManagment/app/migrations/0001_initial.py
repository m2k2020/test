# Generated by Django 4.2 on 2023-05-03 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casetype', models.CharField(max_length=10)),
                ('crimename', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('date', models.DateField(auto_now_add=True)),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cases')),
            ],
        ),
    ]
