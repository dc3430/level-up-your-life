# Generated by Django 2.2.5 on 2019-09-17 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_post_mealplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mealplan',
        ),
        migrations.AddField(
            model_name='post',
            name='mealplan',
            field=models.ManyToManyField(to='main_app.MealPlan'),
        ),
    ]