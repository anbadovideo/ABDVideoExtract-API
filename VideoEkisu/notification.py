import logging

__author__ = 'seung-wongim'

from .models import Device
from scarface.models import SNSDevice, APNApplication, GCMApplication, PushMessage


def get_arn(device_token, device_type):
    """
    registers the device to sns
    :param device_token: the token of device
    :param device_type: the type of device ; 'ios' or 'gcm'
    """

    logger = logging.getLogger(__name__)
    logger.warning(device_token)

    # get the correct notification platform
    if device_type == 'ios':
        application_platform = APNApplication()
    else:
        application_platform = GCMApplication()

    # register the application
    application_platform.register()

    # create the device resource with the token (may be the push token or the registration id)
    sns_device = SNSDevice(application_platform, device_token)

    # register the device with sns or update the token/the attributes
    sns_device.register_or_update(new_token=device_token, custom_user_data="device_id={0}".format('1'))

    # this is important: after updating or registration,
    # your sns resource should have a arn. save this to your database.
    if sns_device.arn:
        logger.warning(sns_device.arn)
        return sns_device.arn
    else:
        return 'invalid_arn'


def send_message(message):
    """
    sends a push to the targeted devices
    :param message: the text message
    """

    device_list = Device.objects.order_by('id')

# set up the application. in this scenario we can target both platforms
    apns = APNApplication()
    gcm = GCMApplication()

    # for every targeted device...
    for device in device_list:
        # ...get the correct application
        if device.type == 'ios':
            application_platform = apns
        else:
            application_platform = gcm

        # and if your device model has a arn....
        if device.arn:
            # ...create the device resource...
            sns_device = SNSDevice(application_platform, device.token, arn=device.arn)
            # ... and the push message...
            message = PushMessage(badge_count=1, context='push', context_id='none', has_new_content=True,
                                  message=message, sound="default")
            # ...and then send it.
            sns_device.send(message)