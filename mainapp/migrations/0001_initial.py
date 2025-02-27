# Generated by Django 5.1.6 on 2025-02-21 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='With no role', max_length=100)),
                ('can_write', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_positive', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(db_index=True, error_messages={'unique': 'Such name taken already'}, max_length=100, unique=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(default=0)),
                ('chat_background_color', models.CharField(default='#fff88f', max_length=7)),
                ('chat_font_color', models.CharField(default='#000000', max_length=7)),
                ('chat_height', models.IntegerField(default=500)),
                ('chat_width', models.IntegerField(default=630)),
                ('action_chat_background_color', models.CharField(default='#fff88f', max_length=7)),
                ('action_chat_font_color', models.CharField(default='#000000', max_length=7)),
                ('action_chat_height', models.IntegerField(default=500)),
                ('action_chat_width', models.IntegerField(default=630)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_posts', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(through='mainapp.Membership', to=settings.AUTH_USER_MODEL)),
                ('rated_persons', models.ManyToManyField(related_name='rated_posts', through='mainapp.Rating', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.roomtype')),
            ],
            options={
                'verbose_name_plural': 'rooms',
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.rooms'),
        ),
        migrations.AddField(
            model_name='membership',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.rooms'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reject_date', models.DateTimeField(null=True)),
                ('was_rejected', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='mainapp.rooms')),
            ],
        ),
        migrations.AddConstraint(
            model_name='membership',
            constraint=models.UniqueConstraint(fields=('room_id', 'user_id'), name='unique_membership'),
        ),
        migrations.AddConstraint(
            model_name='application',
            constraint=models.UniqueConstraint(fields=('room_id', 'user_id'), name='unique_application'),
        ),
    ]
