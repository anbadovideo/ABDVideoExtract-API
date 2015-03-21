__author__ = 'seung-wongim'

from .models import Device


def send_message(message):
    from scarface.models import SNSDevice, APNApplication, GCMApplication, PushMessage

    """
    sends a push to the targeted devices
    :param message: the text message
    :param badge: the new badge count (only applies to ios
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