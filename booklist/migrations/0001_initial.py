# Generated by Django 3.2.5 on 2021-07-04 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('datepublished', models.DateField(blank=True, null=True)),
                ('numpages', models.IntegerField(null=True)),
                ('booktype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booklist.booktype')),
            ],
        ),
    ]