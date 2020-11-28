from .models import Banking
from django.db.models.signals import post_save
from django.dispatch import receiver

from .utils import sending_mail

@receiver(post_save, sender=Banking)
def when_created(sender, instance, created, **kwargs):
    if created:
        pass

@receiver(post_save, sender=Banking)
def check_for_approved(sender, instance, **kwargs):
    if instance.approve_status == 'approved':
        sending_mail(instance.email, instance.approve_status, instance.account_number, instance.amount)
        print('Approved changed to Approve in: ', instance.account_number)

    elif instance.approve_status == 'disapproved':
        sending_mail(instance.email, instance.approve_status, instance.account_number, instance.amount)
        print('Approved changed to Disapprove in: ', instance.account_number)

    else:
        sending_mail(instance.email, instance.approve_status, instance.account_number, instance.amount)
        print('Approved changed to Pending in: ', instance.account_number)