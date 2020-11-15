# Generated by Django 3.1.3 on 2020-11-15 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201115_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='burger',
            field=models.ManyToManyField(blank=True, help_text='Select a burger for this set', to='main.Burger'),
        ),
        migrations.AddField(
            model_name='set',
            name='drink',
            field=models.ManyToManyField(blank=True, help_text='Select a drink for this set', to='main.Drink'),
        ),
        migrations.AddField(
            model_name='set',
            name='pizza',
            field=models.ManyToManyField(blank=True, help_text='Select a pizza for this set', to='main.Pizza'),
        ),
        migrations.AddField(
            model_name='set',
            name='snack',
            field=models.ManyToManyField(blank=True, help_text='Select a rolls snack this set', to='main.Snack'),
        ),
        migrations.AlterField(
            model_name='set',
            name='roll',
            field=models.ManyToManyField(blank=True, help_text='Select a rolls for this set', to='main.Roll'),
        ),
    ]