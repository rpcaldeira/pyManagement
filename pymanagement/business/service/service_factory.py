import platform
from .windows_service import WindowsService

class ServiceFactory:
    def get_serializer(self):
        if platform.system() == 'Windows':
            return WindowsService()
        else:
            raise ValueError(format)

factory = ServiceFactory()