# Generated by Django 4.0.2 on 2022-02-01 21:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('designer', models.CharField(max_length=100)),
                ('year_released', models.IntegerField()),
                ('num_of_players', models.IntegerField()),
                ('est_time_to_play', models.FloatField()),
                ('age_recomendation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamertag', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=500)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player')),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.category')),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='categories', through='raterprojectapi.GameCategory', to='raterprojectapi.Category'),
        ),
        migrations.AddField(
            model_name='game',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raterprojectapi.player'),
        ),
    ]