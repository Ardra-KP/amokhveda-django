# Generated by Django 5.1.2 on 2025-07-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_experts_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experts',
            name='whatsapp_number',
            field=models.CharField(blank=True, help_text='Add number with country code, e.g., 919876543210', max_length=15),
        ),
        migrations.AlterField(
            model_name='experts',
            name='image',
            field=models.ImageField(default='experts/default.jpg', upload_to='experts/'),
            preserve_default=False,
        ),
    ]
