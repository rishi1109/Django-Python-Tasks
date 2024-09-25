# By default, Django signals are executed synchronously. This means that the signal handler is called and completed before control is returned to the code that sent the signal.

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received! Starting a slow task...")
    time.sleep(5)  # Simulating a slow task with sleep
    print("Signal handler completed.")

# Example of saving a User instance to trigger the signal
user = User.objects.create(username="testuser", email="test@example.com")
print("User save operation completed.")
