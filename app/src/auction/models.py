from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Creature(models.Model):
    CREATURE_SPECIES = (
        (1, 'Cat'),
        (2, 'Hedgehog'),
    )
    species = models.IntegerField(verbose_name='Species', choices=CREATURE_SPECIES)
    name = models.CharField(verbose_name='Name', max_length=64)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


class Lot(models.Model):
    creature = models.OneToOneField(Creature, primary_key=True, verbose_name='lot', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


class Bet(models.Model):
    lot = models.ForeignKey(Lot, verbose_name='Lot', related_name='bets', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Price', max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    selected = models.BooleanField(default=False, verbose_name='Selected')

    def __str__(self):
        return f'price: {self.price}, pk: {self.pk}, selected: {self.selected}'


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    funds_balance = models.DecimalField(verbose_name='Balance', max_digits=19, decimal_places=10, default=0.0)
    read_only_fields = ('user', )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
