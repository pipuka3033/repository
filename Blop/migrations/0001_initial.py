# Generated by Django 5.0.7 on 2024-07-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('text', models.TextField()),
                ('images', models.ImageField(upload_to='Blop/images')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('drafts', models.BooleanField(default=False)),
                ('is_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
