# Generated by Django 3.1.2 on 2020-10-30 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201030_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='sub_category_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
