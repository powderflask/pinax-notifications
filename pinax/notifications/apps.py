from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.notifications"
    label = "pinax_notifications"
    verbose_name = _("Pinax Notifications")
    default_auto_field = 'django.db.models.AutoField'  # BigAutoField when ready to add migration.