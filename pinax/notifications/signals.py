import django.dispatch

# providing_args=["batches", "sent", "sent_actual", "run_time"]  # Removed in dj4.x
emitted_notices = django.dispatch.Signal()

