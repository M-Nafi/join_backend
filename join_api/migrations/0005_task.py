# Generated by Django 5.1.3 on 2024-11-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join_api', '0004_contact_delete_contacts_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.EmailField(max_length=254)),
                ('dueDate', models.CharField(max_length=20)),
                ('priorit', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('subtask', models.CharField(max_length=100)),
            ],
        ),
    ]
