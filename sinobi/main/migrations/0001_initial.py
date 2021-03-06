from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='burger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of burger', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of drink', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of pizza', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='roll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of roll or sushi', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='snack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of snack', max_length=20)),
            ],
        ),
    ]
