# Generated by Django 2.2.7 on 2020-01-05 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('year_of_birth', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lyrictext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('genre', models.CharField(choices=[('a', 'Jazz'), ('c', 'Rock')], max_length=1, null=True)),
                ('album', models.CharField(blank=True, max_length=100, verbose_name='Album name')),
                ('track_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Track number')),
                ('release_date', models.DateField()),
                ('duration', models.PositiveIntegerField(help_text='in Minutes')),
                ('interpret', models.ManyToManyField(blank=True, to='yamod.Artist')),
                ('lyric', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yamod.Lyric')),
            ],
        ),
    ]