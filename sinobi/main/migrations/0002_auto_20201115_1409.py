# Generated by Django 3.1.3 on 2020-11-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='burger',
            name='summary',
            field=models.TextField(default='default title', help_text='describe burger', max_length=1000),
        ),
        migrations.AddField(
            model_name='pizza',
            name='summary',
            field=models.TextField(default='default title', help_text='describe pizza', max_length=1000),
        ),
        migrations.AddField(
            model_name='roll',
            name='summary',
            field=models.TextField(default='default title', help_text='describe roll or sushi', max_length=1000),
        ),
        migrations.AddField(
            model_name='snack',
            name='summary',
            field=models.TextField(default='default title', help_text='describe snack', max_length=1000),
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('summary', models.TextField(default='default title', help_text='describe set', max_length=1000)),
                ('roll', models.ManyToManyField(help_text='Select a rolls for this set', to='main.Roll')),
            ],
        ),
    ]
