# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ably_platform_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHENTICATION = "Authentication"
    HISTORY = "History"
    PUBLISHING = "Publishing"
    PUSH = "Push"
    STATS = "Stats"
    STATUS = "Status"
