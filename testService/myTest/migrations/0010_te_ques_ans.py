# Generated by Django 4.0.5 on 2022-06-29 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myTest', '0009_alter_question_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Te',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Te')),
            ],
        ),
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Te')),
                ('testid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myTest.te', verbose_name='Tes')),
            ],
        ),
        migrations.CreateModel(
            name='Ans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Ans')),
                ('questionid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myTest.ques', verbose_name='Ans')),
            ],
        ),
    ]
