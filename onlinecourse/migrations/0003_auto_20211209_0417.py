# Generated by Django 3.1.3 on 2021-12-09 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20211209_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='answer_correct',
            new_name='is_correct',
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=1000),
        ),
    ]
