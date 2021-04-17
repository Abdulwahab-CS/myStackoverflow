# Generated by Django 3.2 on 2021-04-17 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210417_1412'),
        ('answers', '0002_auto_20210417_1929'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answercomment',
            name='answer',
            field=models.ForeignKey(db_column='answer_id', on_delete=django.db.models.deletion.CASCADE, to='answers.answer'),
        ),
        migrations.AlterField(
            model_name='questioncomment',
            name='question',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='questions.question'),
        ),
    ]
