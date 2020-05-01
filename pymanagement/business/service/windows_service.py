import psutil

class WindowsService:
    pass

def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service

service = get_service('wuauserv')

if service:
    print("Service found: ", service)
else:
    print("Service not found")

if service and service['status'] == 'running':
    print("Service is running")
else:
    print("Service is not running")