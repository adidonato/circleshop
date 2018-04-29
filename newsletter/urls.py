from django.conf.urls import patterns, include, url
from newsletter.models import Subscription
from newsletter_subscription.backend import ModelBackend
from newsletter_subscription.urls import newsletter_subscriptions_urlpatterns

urlpatterns = patterns('',
    url(r'^newsletter/', include(newsletter_subscriptions_urlpatterns(
        backend=ModelBackend(Subscription),))
    ),
)
