from ably_platform_python_sdk.paths.push_device_registrations.get import ApiForget
from ably_platform_python_sdk.paths.push_device_registrations.post import ApiForpost
from ably_platform_python_sdk.paths.push_device_registrations.delete import ApiFordelete


class PushDeviceRegistrations(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
