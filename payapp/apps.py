from django.apps import AppConfig
import threading


class PayappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payapp'

    def ready(self):
        import os
        if os.environ.get("RUN_MAIN") != "true":
            return
        from timestampserver import run_server
        threading.Thread(target=run_server, daemon=True).start()
