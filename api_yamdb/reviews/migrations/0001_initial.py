# Generated by Django 3.2 on 2023-05-10 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата изменения')),
                ('mark', models.CharField(choices=[('5', 'Отлично'), ('4', 'Хорошо'), ('3', 'Нормально'), ('2', 'Плохо'), ('1', 'Ужасно')], max_length=20, verbose_name='Value')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.title')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата изменения')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review')),
            ],
        ),
    ]
