# By default, Django signals are part of the same database transaction. This can be demonstrated by raising an exception in the signal handler and showing that the database transaction is rolled back.

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler that raises an exception
@receiver(post_save, sender=User)
def signal_handler_rollback(sender, instance, **kwargs):
    print("Signal handler triggered, raising exception...")
    raise Exception("Intentional error to trigger rollback.")

# Wrapping the save operation in a transaction to catch rollback
try:
    with transaction.atomic():
        user = User.objects.create(username="testuser", email="test@example.com")
except Exception as e:
    print(f"Transaction rolled back due to: {e}")

# Check if user was saved or rolled back
user_exists = User.objects.filter(username="testuser").exists()
print(f"Was the user saved? {user_exists}")
