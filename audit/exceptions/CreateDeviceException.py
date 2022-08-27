from rest_framework.exceptions import APIException


class CreateDeviceEmptyQRException(APIException):
    status_code = 400
    default_detail = 'Cannot create device with no QR code.'
    default_code = 'cannot_create_device'


class CreateDeviceExistsException(APIException):
    status_code = 400
    default_detail = 'Cannot create device that already exists.'
    default_code = 'cannot_create_device'