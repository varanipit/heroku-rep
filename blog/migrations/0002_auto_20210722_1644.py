# Generated by Django 3.2.5 on 2021-07-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feature_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cover/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
