# Generated by Django 2.1.2 on 2018-10-21 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181021_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='user',
        ),
        migrations.RemoveField(
            model_name='question',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
