# Generated by Django 3.2 on 2021-04-17 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210417_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answercomment',
            old_name='answer',
            new_name='answer_id',
        ),
        migrations.RenameField(
            model_name='questioncomment',
            old_name='question',
            new_name='question_id',
        ),
    ]