# Generated by Django 5.1 on 2024-08-31 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity_sold', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('review_count', models.IntegerField()),
            ],
        ),
    ]
