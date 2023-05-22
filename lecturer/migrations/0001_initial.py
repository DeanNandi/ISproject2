# Generated by Django 4.0 on 2022-11-23 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=2555)),
                ('email_address', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('admission', models.CharField(max_length=255)),
                ('unit_name', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('ID_No', models.IntegerField()),
                ('phone_No', models.IntegerField()),
                ('email', models.CharField(max_length=255)),
                ('faculty', models.CharField(max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('unit_name', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=255)),
                ('academic_year', models.CharField(max_length=255)),
                ('image_urls', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('unit_name', models.CharField(max_length=255)),
                ('group_year', models.CharField(max_length=255)),
                ('qr_generator', models.CharField(max_length=20083)),
                ('form_generator', models.CharField(max_length=20083)),
                ('edit_link', models.CharField(max_length=20083)),
                ('responses_link', models.CharField(max_length=2083)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.CharField(max_length=255)),
                ('unit_name', models.CharField(max_length=255)),
                ('academic_year', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
