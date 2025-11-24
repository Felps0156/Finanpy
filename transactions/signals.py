from decimal import Decimal

from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver

from accounts.models import Account
from categories.models import Category
from transactions.models import Transaction


def _apply_delta(account: Account, amount: Decimal, category_type: str, reverse: bool = False):
    delta = amount
    if category_type == Category.TYPE_INCOME:
        delta = amount if not reverse else -amount
    else:
        delta = -amount if not reverse else amount
    account.balance = (account.balance or Decimal('0')) + delta
    account.save(update_fields=['balance'])


@receiver(pre_save, sender=Transaction)
def cache_previous_state(sender, instance, **kwargs):
    if not instance.pk:
        instance._previous_state = None
        return
    previous = Transaction.objects.get(pk=instance.pk)
    instance._previous_state = {
        'account_id': previous.account_id,
        'amount': previous.amount,
        'type': previous.category.type,
    }


@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, created, **kwargs):
    if created or not getattr(instance, '_previous_state', None):
        _apply_delta(instance.account, instance.amount, instance.category.type)
        return

    prev = instance._previous_state
    prev_account = Account.objects.get(pk=prev['account_id'])
    _apply_delta(prev_account, prev['amount'], prev['type'], reverse=True)
    _apply_delta(instance.account, instance.amount, instance.category.type)


@receiver(pre_delete, sender=Transaction)
def revert_balance_on_delete(sender, instance, **kwargs):
    _apply_delta(instance.account, instance.amount, instance.category.type, reverse=True)
