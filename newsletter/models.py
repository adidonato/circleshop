from django.db import models
from django.utils.translation import ugettext_lazy as _

from newsletter_subscription.models import SubscriptionBase

class Subscription(SubscriptionBase):
    full_name = models.CharField(_('full name'), max_length=100, blank=True)
