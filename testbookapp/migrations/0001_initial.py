# Generated by Django 4.2.15 on 2024-08-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=200)),
                ('bookprice', models.IntegerField()),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('bookimage', models.ImageField(blank=True, null=True, upload_to='book_media')),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]