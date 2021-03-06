# Generated by Django 2.2.9 on 2020-03-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_owner_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('notification', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Aviso',
                'verbose_name_plural': 'Avisos',
                'db_table': 'notification',
            },
        ),
    ]
