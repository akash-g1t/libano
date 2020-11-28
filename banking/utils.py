from django.core.mail import send_mail
from django.utils import timezone

SUBJECT = 'Status For Your Tokens'
FROM = 'Libano@gmail.com'

def sending_mail(to, status, account_number, amount):
    print('Sending Mail TO : ', to)
    print('Status is : ', status, '\nSending...')
    if status == 'approved':
        BODY = 'Your Token Request with account number {} for {} tokens ( at {} ) has been Approved Successfully!'.format(account_number, amount, timezone.now().strftime('%Y-%m-%d %H:%M'))
    elif status == 'disapproved':
        BODY = 'Your Token Request with account number {} for {} tokens ( at {} ) has been Dissaproved!'.format(account_number, amount, timezone.now().strftime('%Y-%m-%d %H:%M'))
    else:
        BODY = 'Your Token Request with account number {} for {} tokens ( at {} ) is Successfully Registered!'.format(account_number, amount, timezone.now().strftime('%Y-%m-%d %H:%M'))

    send_mail(SUBJECT, BODY, FROM, [to, FROM], fail_silently=True)
    print('Email Has been sent Successfully!')
