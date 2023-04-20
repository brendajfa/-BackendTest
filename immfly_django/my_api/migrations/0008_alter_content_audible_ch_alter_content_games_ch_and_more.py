# Generated by Django 4.2 on 2023-04-20 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0007_remove_audible_contents_remove_games_contents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='audible_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.audible'),
        ),
        migrations.AlterField(
            model_name='content',
            name='games_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.games'),
        ),
        migrations.AlterField(
            model_name='content',
            name='kids_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.kids'),
        ),
        migrations.AlterField(
            model_name='content',
            name='lifestyle_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.lifestyle'),
        ),
        migrations.AlterField(
            model_name='content',
            name='movies_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.movies'),
        ),
        migrations.AlterField(
            model_name='content',
            name='music_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.music_podcasts'),
        ),
        migrations.AlterField(
            model_name='content',
            name='press_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.press_magazines'),
        ),
        migrations.AlterField(
            model_name='content',
            name='tvshow_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content', to='my_api.tvshow'),
        ),
    ]