# Generated by Django 2.2.2 on 2019-06-11 03:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('U', 'Unread'), ('V', 'Viewed'), ('R', 'Replied'), ('S', 'Sold')], db_index=True, default='U', max_length=1)),
                ('package', models.CharField(choices=[('starter', 'Starter'), ('advanced', 'Advanced'), ('complete', 'Complete'), ('custom', 'Custom')], max_length=8)),
                ('full_name', models.CharField(max_length=128)),
                ('company', models.CharField(blank=True, max_length=64, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PricingLead',
            fields=[
                ('lead_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='leads.Lead')),
                ('narrations_needed', models.PositiveIntegerField(default=1)),
                ('podcast_distribution', models.BooleanField(default=0)),
                ('alexa_skill', models.BooleanField(default=0)),
                ('alexa_flash_briefing', models.BooleanField(default=0)),
                ('google_news', models.BooleanField(default=0)),
                ('google_action', models.BooleanField(default=0)),
                ('thirdparty_integration', models.BooleanField(default=0)),
            ],
            bases=('leads.lead',),
        ),
    ]