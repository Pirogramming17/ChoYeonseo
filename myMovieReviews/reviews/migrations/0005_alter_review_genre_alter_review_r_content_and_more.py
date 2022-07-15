# Generated by Django 4.0.6 on 2022-07-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_rename_review_review_r_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(choices=[('AT', 'Action'), ('SF', 'SF'), ('RM', 'Romance'), ('CM', 'Comedy'), ('AM', 'Animation'), ('TR', 'Thriller')], max_length=2, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='review',
            name='r_content',
            field=models.TextField(verbose_name='리뷰'),
        ),
        migrations.AlterField(
            model_name='review',
            name='r_time',
            field=models.CharField(max_length=30, verbose_name='러닝타임'),
        ),
    ]