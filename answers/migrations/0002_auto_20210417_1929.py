# Generated by Django 3.2 on 2021-04-17 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20210417_1412'),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='question_id',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question_id',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='questions.question'),
        ),
    ]
