# Generated by Django 4.2.4 on 2023-08-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='почта')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_time', models.DateTimeField(verbose_name='mailing_time')),
                ('frequency', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], default='daily', max_length=15, verbose_name='frequency')),
                ('status', models.CharField(choices=[('completed', 'Завершена'), ('created', 'Создана'), ('started', 'Запущена')], default='created', max_length=15, verbose_name='status')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('body', models.TextField(blank=True, null=True, verbose_name='body')),
                ('clients', models.ManyToManyField(to='mailing.client', verbose_name='clients')),
            ],
            options={
                'verbose_name': 'Mailing',
                'verbose_name_plural': 'Mailings',
            },
        ),
        migrations.CreateModel(
            name='MailingLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try_datetime', models.DateTimeField(auto_now_add=True, verbose_name='last_try_datetime')),
                ('attempt_status', models.CharField(choices=[('successfully', 'Успешно'), ('not successfully', 'Не успешно')], default='successfully', max_length=20, verbose_name='attempt_status')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='server_response')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='mailing')),
            ],
        ),
    ]
