import platform

class ServiceFactory:
    def get_serializer(self):
        if platform.system() == 'Windows':
            return WindowsServices()
        else:
            raise ValueError(format)

factory = ServiceFactory()