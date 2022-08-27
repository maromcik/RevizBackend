from rest_framework.exceptions import APIException


class UpdateDeviceNotExistsException(APIException):
    status_code = 400
    default_detail = 'Cannot update non existing device.'
    default_code = 'cannot_update_device'


class UpdateDeviceDuplicitQRException(APIException):
    status_code = 400
    default_detail = 'Cannot update device with QR of another device'
    default_code = 'cannot_update_device'