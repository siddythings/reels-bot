from enum import Enum
from services.inc24.inc24 import INC24


class ServiceProviderFactory(Enum):
    INC42 = "INC42"
    UNKNOWN = "UNKNOWN"

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            return ServiceProviderFactory.UNKNOWN

    @staticmethod
    def get_provider(provider_name):
        if ServiceProviderFactory.value_of(provider_name) == ServiceProviderFactory.INC42:
            return INC24()
        else:
            raise "Invalid service provider"
