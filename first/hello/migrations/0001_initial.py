# Generated by Django 3.0.3 on 2020-04-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=240, unique='True')),
                ('topic_date', models.DateField()),
                ('topic_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='webpages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=240, unique='True')),
                ('page_address', models.URLField(unique='True')),
            ],
        ),
    ]
