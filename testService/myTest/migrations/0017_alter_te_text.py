# Generated by Django 4.0.5 on 2022-07-03 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0016_remove_ans_questionid_ques_r_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='te',
            name='text',
            field=models.CharField(max_length=255, unique=True, verbose_name='Te'),
        ),
    ]
