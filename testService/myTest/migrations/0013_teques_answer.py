# Generated by Django 4.0.5 on 2022-06-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0012_remove_ques_testid_remove_te_quesid_teques'),
    ]

    operations = [
        migrations.AddField(
            model_name='teques',
            name='answer',
            field=models.ManyToManyField(to='myTest.ans'),
        ),
    ]
