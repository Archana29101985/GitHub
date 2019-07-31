# Generated by Django 2.0 on 2019-03-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('MovieID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('MovieTitle', models.CharField(max_length=50)),
                ('MovieYear', models.IntegerField(max_length=10)),
                ('MovieGenre', models.CharField(choices=[('Action', 'action'), ('Comedy', 'comedy'), ('Romance', 'romance'), ('Thriller', 'thriller')], default='Comedy', max_length=100)),
            ],
        ),
    ]
