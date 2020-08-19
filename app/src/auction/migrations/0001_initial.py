# Generated by Django 3.1 on 2020-08-19 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.IntegerField(choices=[(1, 'Cat'), (2, 'Hedgehog')], verbose_name='Species')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('funds_balance', models.DecimalField(decimal_places=10, default=0.0, max_digits=19, verbose_name='Balance')),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('creature', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auction.creature', verbose_name='lot')),
                ('price', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Price')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=10, max_digits=19, verbose_name='Price')),
                ('selected', models.BooleanField(default=False, verbose_name='Selected')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bets', to='auction.lot', verbose_name='Lot')),
            ],
        ),
    ]
