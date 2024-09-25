# By default, Django signals run in the same thread as the code that triggered the signal. We can verify this by comparing thread IDs.

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.get_ident()}")

# Example of saving a User instance to trigger the signal
print(f"User save running in thread: {threading.get_ident()}")
user = User.objects.create(username="testuser", email="test@example.com")
