# Generated by Django 5.0.6 on 2024-05-08 10:53

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderData',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this instance was created.')),
                ('modified', models.DateTimeField(auto_now=True, help_text='When this instance was modified.')),
                ('po_number', models.CharField(max_length=250, unique=True)),
                ('order_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=30)),
                ('quality_rating', models.FloatField(null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateField(null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='_po_vendor', to='vendor.vendordata')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
