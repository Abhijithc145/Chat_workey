# Generated by Django 4.1.2 on 2022-10-14 06:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='model_Chat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.DateTimeField(auto_now_add=True, verbose_name='Created bt')),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_at', models.DateTimeField(auto_now=True, verbose_name='Delete at')),
                ('deleted_by', models.DateTimeField(auto_now=True, verbose_name='Delete bt')),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('model_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.model_chat')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('model_chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.model_chat')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.organization')),
            ],
        ),
    ]
