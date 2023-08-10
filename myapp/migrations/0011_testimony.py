# Generated by Django 4.1.5 on 2023-05-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_smarttv_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media\testimonies')),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonies',
                'db_table': '',
                'managed': True,
            },
        ),
    ]