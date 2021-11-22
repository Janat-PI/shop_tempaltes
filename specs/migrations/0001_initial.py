# Generated by Django 3.0.8 on 2021-08-23 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=50, verbose_name='Имя ключа для категории')),
                ('feature_filter_name', models.CharField(max_length=50, verbose_name='Имя для фильтра')),
                ('unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Единица измерения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
            ],
            options={
                'unique_together': {('category', 'feature_name', 'feature_filter_name')},
            },
        ),
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.CategoryFeature', verbose_name='Характеристика')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValidator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_feature_value', models.CharField(max_length=100, verbose_name='Валидное значение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category', verbose_name='Категория')),
                ('feature_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.CategoryFeature', verbose_name='Ключ характеристики')),
            ],
        ),
    ]
