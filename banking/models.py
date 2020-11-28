from django.db import models

APPROVAL_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('disapproved', 'disapproved')
)

class Banking(models.Model):
    email = models.EmailField(max_length=50)
    url = models.URLField()
    account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=5)
    amount = models.IntegerField()
    approve_status = models.CharField(max_length=15, choices=APPROVAL_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)