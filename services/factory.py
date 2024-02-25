from enum import Enum
from services.inc42.inc42 import INC42


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
            return INC42()
        else:
            raise "Invalid service provider"
