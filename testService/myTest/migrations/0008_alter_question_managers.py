# Generated by Django 4.0.5 on 2022-06-28 19:46

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0007_usertest_testresults'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('answers', django.db.models.manager.Manager()),
            ],
        ),
    ]
