import logging
import os

import sentry_sdk

from celery import Celery
from celery.signals import celeryd_init
from sentry_sdk.integrations.celery import CeleryIntegration
from infrastructure import settings

from infrastructure.settings import APP_ENV

logger = logging.getLogger(__name__)

logger.info('INITIATE CELERY APP...')
app = Celery(main='DI')
app.config_from_object('infrastructure.celery_settings')

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    integrations=[
        CeleryIntegration(),
    ],
    request_bodies="medium",
    with_locals=True,
    environment=f"{APP_ENV}.DI",
    send_default_pii=True,
)

class CeleryApp:

    @property
    def app(self) -> Celery:
        return app
