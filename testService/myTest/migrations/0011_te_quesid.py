# Generated by Django 4.0.5 on 2022-06-29 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0010_te_ques_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='te',
            name='quesid',
            field=models.ManyToManyField(to='myTest.ques'),
        ),
    ]