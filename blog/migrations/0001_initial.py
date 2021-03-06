# Generated by Django 4.0.4 on 2022-04-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('post_text', models.CharField(max_length=200)),
                ('image_names', models.FileField(null=True, upload_to='images/')),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
