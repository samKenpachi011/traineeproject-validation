from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from datetime import datetime
from dateutil.tz import gettz


class AppConfig(DjangoAppConfig):
    name = 'traineeproject_validations'
    verbose_name = 'Trainee Project Validations'


if settings.APP_NAME == 'traineeproject_validation':   
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfigs

    class BaseEdcProtocolAppConfig(BaseEdcProtocolAppConfigs):
        protocol = 'ADZ1222'
        protocol_name = 'ADZ 1222 - ESR-21-21311'
        protocol_number = '1222'
        protocol_title = ''
        study_open_datetime = datetime(
            2021, 4, 15, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))