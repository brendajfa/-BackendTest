# Generated by Django 4.2 on 2023-04-20 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0006_remove_content_parent_channel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audible',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='games',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='kids',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='lifestyle',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='music_podcasts',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='press_magazines',
            name='contents',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='contents',
        ),
        migrations.AddField(
            model_name='content',
            name='audible_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='audible', to='my_api.audible'),
        ),
        migrations.AddField(
            model_name='content',
            name='games_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='my_api.games'),
        ),
        migrations.AddField(
            model_name='content',
            name='kids_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kids', to='my_api.kids'),
        ),
        migrations.AddField(
            model_name='content',
            name='lifestyle_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lifestyle', to='my_api.lifestyle'),
        ),
        migrations.AddField(
            model_name='content',
            name='movies_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='my_api.movies'),
        ),
        migrations.AddField(
            model_name='content',
            name='music_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='music', to='my_api.music_podcasts'),
        ),
        migrations.AddField(
            model_name='content',
            name='press_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='press', to='my_api.press_magazines'),
        ),
        migrations.AddField(
            model_name='content',
            name='tvshow_ch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tvshow', to='my_api.tvshow'),
        ),
    ]
