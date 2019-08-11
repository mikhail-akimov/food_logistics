# Generated by Django 2.2.1 on 2019-08-11 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persons', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_description', models.CharField(max_length=300)),
                ('default_persons', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe2Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=1)),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='food_app.Ingredient')),
                ('measure_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='food_app.Measure')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Meal2Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.Dish')),
                ('meal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.Meal')),
            ],
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.Recipe'),
        ),
        migrations.CreateModel(
            name='Day2Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('meal_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.Meal')),
            ],
        ),
    ]
