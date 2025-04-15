# Generated by Django 5.1.7 on 2025-04-15 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('payment_method', models.CharField(max_length=50)),
                ('card_number', models.CharField(blank=True, max_length=30, null=True)),
                ('card_name', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=10, null=True)),
                ('cvv', models.CharField(blank=True, max_length=10, null=True)),
                ('paypal_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
