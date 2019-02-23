# Generated by Django 2.1.7 on 2019-02-20 17:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('content', models.TextField()),
                ('seo_title', models.CharField(max_length=250)),
                ('seo_description', models.CharField(max_length=160)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=9)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alcoholapp.Category')),
            ],
        ),
    ]
