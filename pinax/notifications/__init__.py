try:
    from importlib.metadata import version
except ImportError:
    # Python < 3.8 fallback
    from pkg_resources import get_distribution

    def version(package_name):
        return get_distribution(package_name).version

import django

if django.VERSION < (3, 2):
    default_app_config = "pinax.notifications.apps.AppConfig"

__version__ = version("pinax-notifications")