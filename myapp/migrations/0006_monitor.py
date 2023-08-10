# Generated by Django 4.1.5 on 2023-04-16 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_price_desktop_prices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prices', models.CharField(max_length=150)),
                ('image', models.ImageField(default='default.jpg', upload_to='media')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Monitor',
                'verbose_name_plural': 'Monitor',
            },
        ),
    ]