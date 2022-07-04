# Generated by Django 4.0.5 on 2022-06-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0004_remove_test_questionid_alter_question_questionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='questionid',
            field=models.ManyToManyField(through='myTest.TestQuestion', to='myTest.question'),
        ),
    ]