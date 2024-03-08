<div align="center">

[![Visit Ably](./header.png)](https://ably.com)

# Ably<a id="ably"></a>

The [REST API specification](https://www.ably.io/documentation/rest-api) for Ably.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`ably.authentication.request_access_token`](#ablyauthenticationrequest_access_token)
  * [`ably.history.get_messages_by_channel`](#ablyhistoryget_messages_by_channel)
  * [`ably.history.get_presence_history_of_channel`](#ablyhistoryget_presence_history_of_channel)
  * [`ably.publishing.publish_messages_to_channel`](#ablypublishingpublish_messages_to_channel)
  * [`ably.push.delete_push_device_details`](#ablypushdelete_push_device_details)
  * [`ably.push.get_channels_with_push_subscribers`](#ablypushget_channels_with_push_subscribers)
  * [`ably.push.get_push_device_details`](#ablypushget_push_device_details)
  * [`ably.push.get_push_subscriptions_on_channels`](#ablypushget_push_subscriptions_on_channels)
  * [`ably.push.get_registered_push_devices`](#ablypushget_registered_push_devices)
  * [`ably.push.patch_push_device_details`](#ablypushpatch_push_device_details)
  * [`ably.push.publish_push_notification_to_devices`](#ablypushpublish_push_notification_to_devices)
  * [`ably.push.put_push_device_details`](#ablypushput_push_device_details)
  * [`ably.push.register_push_device`](#ablypushregister_push_device)
  * [`ably.push.subscribe_push_device_to_channel`](#ablypushsubscribe_push_device_to_channel)
  * [`ably.push.unregister_all_push_devices`](#ablypushunregister_all_push_devices)
  * [`ably.push.unregister_push_device`](#ablypushunregister_push_device)
  * [`ably.push.update_push_device_details`](#ablypushupdate_push_device_details)
  * [`ably.stats.get_stats`](#ablystatsget_stats)
  * [`ably.stats.get_time`](#ablystatsget_time)
  * [`ably.status.get_metadata_of_all_channels`](#ablystatusget_metadata_of_all_channels)
  * [`ably.status.get_metadata_of_channel`](#ablystatusget_metadata_of_channel)
  * [`ably.status.get_presence_of_channel`](#ablystatusget_presence_of_channel)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Ably&serviceName=Platform&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from ably_platform_python_sdk import Ably, ApiException

ably = Ably(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Request an access token
    request_access_token_response = ably.authentication.request_access_token(
        body=None,
        key_name="keyName_example",
        capability={
    },
        client_id="string_example",
        key_name="xVLyHw.LMJZxw",
        nonce="string_example",
        timestamp=1,
        mac="string_example",
        x_ably_version="string_example",
        format="json",
    )
    print(request_access_token_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi.request_access_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from ably_platform_python_sdk import Ably, ApiException

ably = Ably(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

async def main():
    try:
        # Request an access token
        request_access_token_response = await ably.authentication.arequest_access_token(
            body=None,
            key_name="keyName_example",
            capability={
    },
            client_id="string_example",
            key_name="xVLyHw.LMJZxw",
            nonce="string_example",
            timestamp=1,
            mac="string_example",
            x_ably_version="string_example",
            format="json",
        )
        print(request_access_token_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi.request_access_token: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from ably_platform_python_sdk import Ably, ApiException

ably = Ably(

    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD',

    access_token = 'YOUR_BEARER_TOKEN'
)

try:
    # Request an access token
    request_access_token_response = ably.authentication.raw.request_access_token(
        body=None,
        key_name="keyName_example",
        capability={
    },
        client_id="string_example",
        key_name="xVLyHw.LMJZxw",
        nonce="string_example",
        timestamp=1,
        mac="string_example",
        x_ably_version="string_example",
        format="json",
    )
    pprint(request_access_token_response.body)
    pprint(request_access_token_response.body["capability"])
    pprint(request_access_token_response.body["expires"])
    pprint(request_access_token_response.body["issued"])
    pprint(request_access_token_response.body["key_name"])
    pprint(request_access_token_response.body["token"])
    pprint(request_access_token_response.headers)
    pprint(request_access_token_response.status)
    pprint(request_access_token_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AuthenticationApi.request_access_token: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `ably.authentication.request_access_token`<a id="ablyauthenticationrequest_access_token"></a>

This is the means by which clients obtain access tokens to use the service. You can see how to construct an Ably TokenRequest in the [Ably TokenRequest spec](https://www.ably.io/documentation/rest-api/token-request-spec) documentation, although we recommend you use an Ably SDK rather to create a TokenRequest, as the construction of a TokenRequest is complex. The resulting token response object contains the token properties as defined in Ably TokenRequest spec. Authentication is not required if using a Signed TokenRequest.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_access_token_response = ably.authentication.request_access_token(
    body=None,
    key_name="keyName_example",
    capability={
    },
    client_id="string_example",
    key_name="xVLyHw.LMJZxw",
    nonce="string_example",
    timestamp=1,
    mac="string_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### key_name: `str`<a id="key_name-str"></a>

The [key name](https://www.ably.io/documentation/rest-api/token-request-spec#api-key-format) comprises of the app ID and key ID of an API key.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### requestBody: [`Any`](./ably_platform_python_sdk/type/typing_any.py)<a id="requestbody-anyably_platform_python_sdktypetyping_anypy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TokenDetails`](./ably_platform_python_sdk/pydantic/token_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/keys/{keyName}/requestToken` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.history.get_messages_by_channel`<a id="ablyhistoryget_messages_by_channel"></a>

Get message history for a channel

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_messages_by_channel_response = ably.history.get_messages_by_channel(
    channel_id="channel_id_example",
    x_ably_version="string_example",
    format="json",
    start="string_example",
    limit=100,
    end="now",
    direction="backwards",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The [Channel's ID](https://www.ably.io/documentation/rest/channels).

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### start: `str`<a id="start-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### end: `str`<a id="end-str"></a>

##### direction: `str`<a id="direction-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Message`](./ably_platform_python_sdk/pydantic/message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/messages` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.history.get_presence_history_of_channel`<a id="ablyhistoryget_presence_history_of_channel"></a>

Get presence on a channel

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_presence_history_of_channel_response = ably.history.get_presence_history_of_channel(
    channel_id="channel_id_example",
    x_ably_version="string_example",
    format="json",
    start="string_example",
    limit=100,
    end="now",
    direction="backwards",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The [Channel's ID](https://www.ably.io/documentation/rest/channels).

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### start: `str`<a id="start-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### end: `str`<a id="end-str"></a>

##### direction: `str`<a id="direction-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PresenceMessage`](./ably_platform_python_sdk/pydantic/presence_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/presence/history` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.publishing.publish_messages_to_channel`<a id="ablypublishingpublish_messages_to_channel"></a>

Publish a message to the specified channel

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
publish_messages_to_channel_response = ably.publishing.publish_messages_to_channel(
    channel_id="channel_id_example",
    client_id="string_example",
    connection_id="string_example",
    data="string_example",
    encoding="string_example",
    extras={
    },
    id="string_example",
    name="string_example",
    timestamp=1,
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The [Channel's ID](https://www.ably.io/documentation/rest/channels).

##### client_id: `str`<a id="client_id-str"></a>

The [client ID](https://www.ably.io/documentation/core-features/authentication#identified-clients) of the publisher of this message.

##### connection_id: `str`<a id="connection_id-str"></a>

The connection ID of the publisher of this message.

##### data: `str`<a id="data-str"></a>

The string encoded payload, with the encoding specified below.

##### encoding: `str`<a id="encoding-str"></a>

This will typically be empty as all messages received from Ably are automatically decoded client-side using this value. However, if the message encoding cannot be processed, this attribute will contain the remaining transformations not applied to the data payload.

##### extras: [`Extras`](./ably_platform_python_sdk/type/extras.py)<a id="extras-extrasably_platform_python_sdktypeextraspy"></a>


##### id: `str`<a id="id-str"></a>

A Unique ID that can be specified by the publisher for [idempotent publishing](https://www.ably.io/documentation/rest/messages#idempotent).

##### name: `str`<a id="name-str"></a>

The event name, if provided.

##### timestamp: `int`<a id="timestamp-int"></a>

Timestamp when the message was received by the Ably, as milliseconds since the epoch.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Message`](./ably_platform_python_sdk/type/message.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.delete_push_device_details`<a id="ablypushdelete_push_device_details"></a>

Delete a device details object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ably.push.delete_push_device_details(
    x_ably_version="string_example",
    format="json",
    channel="string_example",
    device_id="string_example",
    client_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### channel: `str`<a id="channel-str"></a>

Filter to restrict to subscriptions associated with that channel.

##### device_id: `str`<a id="device_id-str"></a>

Must be set when clientId is empty, cannot be used with clientId.

##### client_id: `str`<a id="client_id-str"></a>

Must be set when deviceId is empty, cannot be used with deviceId.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/channelSubscriptions` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.get_channels_with_push_subscribers`<a id="ablypushget_channels_with_push_subscribers"></a>

Returns a paginated response of channel names.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_channels_with_push_subscribers_response = ably.push.get_channels_with_push_subscribers(
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.get_push_device_details`<a id="ablypushget_push_device_details"></a>

Get the full details of a device.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_push_device_details_response = ably.push.get_push_device_details(
    device_id="device_id_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's ID.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations/{device_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.get_push_subscriptions_on_channels`<a id="ablypushget_push_subscriptions_on_channels"></a>

Get a list of push notification subscriptions to channels.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_push_subscriptions_on_channels_response = ably.push.get_push_subscriptions_on_channels(
    x_ably_version="string_example",
    format="json",
    channel="string_example",
    device_id="string_example",
    client_id="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### channel: `str`<a id="channel-str"></a>

Filter to restrict to subscriptions associated with that channel.

##### device_id: `str`<a id="device_id-str"></a>

Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.

##### client_id: `str`<a id="client_id-str"></a>

Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/channelSubscriptions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.get_registered_push_devices`<a id="ablypushget_registered_push_devices"></a>

List of device details of devices registed for push notifications.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_registered_push_devices_response = ably.push.get_registered_push_devices(
    x_ably_version="string_example",
    format="json",
    device_id="string_example",
    client_id="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### device_id: `str`<a id="device_id-str"></a>

Optional filter to restrict to devices associated with that deviceId.

##### client_id: `str`<a id="client_id-str"></a>

Optional filter to restrict to devices associated with that clientId.

##### limit: `int`<a id="limit-int"></a>

The maximum number of records to return.

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.patch_push_device_details`<a id="ablypushpatch_push_device_details"></a>

Specific attributes of an existing registration can be updated. Only clientId, metadata and push.recipient are mutable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
patch_push_device_details_response = ably.push.patch_push_device_details(
    device_id="device_id_example",
    client_id="string_example",
    device_secret="string_example",
    form_factor="phone",
    id="string_example",
    metadata={},
    platform="ios",
    push_recipient={
        "transport_type": "apns",
    },
    push_state="Active",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's ID.

##### client_id: `str`<a id="client_id-str"></a>

Optional trusted client identifier for the device.

##### device_secret: `str`<a id="device_secret-str"></a>

Secret value for the device.

##### form_factor: `str`<a id="form_factor-str"></a>

Form factor of the push device.

##### id: `str`<a id="id-str"></a>

Unique identifier for the device generated by the device itself.

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Optional metadata object for this device. The metadata for a device may only be set by clients with push-admin privileges and will be used more extensively in the future with smart notifications.

##### platform: `str`<a id="platform-str"></a>

Platform of the push device.

##### push_recipient: [`Recipient`](./ably_platform_python_sdk/type/recipient.py)<a id="push_recipient-recipientably_platform_python_sdktyperecipientpy"></a>


##### push_state: `str`<a id="push_state-str"></a>

the current state of the push device.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceDetails`](./ably_platform_python_sdk/type/device_details.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations/{device_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.publish_push_notification_to_devices`<a id="ablypushpublish_push_notification_to_devices"></a>

A convenience endpoint to deliver a push notification payload to a single device or set of devices identified by their client identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ably.push.publish_push_notification_to_devices(
    recipient={
        "transport_type": "apns",
    },
    push={
    },
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient: [`Recipient`](./ably_platform_python_sdk/type/recipient.py)<a id="recipient-recipientably_platform_python_sdktyperecipientpy"></a>


##### push: [`Push`](./ably_platform_python_sdk/type/push.py)<a id="push-pushably_platform_python_sdktypepushpy"></a>


##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Any`](./ably_platform_python_sdk/type/typing_any.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/publish` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.put_push_device_details`<a id="ablypushput_push_device_details"></a>

Device registrations can be upserted (the existing registration is replaced entirely) with a PUT operation. Only clientId, metadata and push.recipient are mutable.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
put_push_device_details_response = ably.push.put_push_device_details(
    device_id="device_id_example",
    client_id="string_example",
    device_secret="string_example",
    form_factor="phone",
    id="string_example",
    metadata={},
    platform="ios",
    push_recipient={
        "transport_type": "apns",
    },
    push_state="Active",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's ID.

##### client_id: `str`<a id="client_id-str"></a>

Optional trusted client identifier for the device.

##### device_secret: `str`<a id="device_secret-str"></a>

Secret value for the device.

##### form_factor: `str`<a id="form_factor-str"></a>

Form factor of the push device.

##### id: `str`<a id="id-str"></a>

Unique identifier for the device generated by the device itself.

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Optional metadata object for this device. The metadata for a device may only be set by clients with push-admin privileges and will be used more extensively in the future with smart notifications.

##### platform: `str`<a id="platform-str"></a>

Platform of the push device.

##### push_recipient: [`Recipient`](./ably_platform_python_sdk/type/recipient.py)<a id="push_recipient-recipientably_platform_python_sdktyperecipientpy"></a>


##### push_state: `str`<a id="push_state-str"></a>

the current state of the push device.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceDetails`](./ably_platform_python_sdk/type/device_details.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations/{device_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.register_push_device`<a id="ablypushregister_push_device"></a>

Register a device’s details, including the information necessary to deliver push notifications to it. Requires "push-admin" capability.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
register_push_device_response = ably.push.register_push_device(
    client_id="string_example",
    device_secret="string_example",
    form_factor="phone",
    id="string_example",
    metadata={},
    platform="ios",
    push_recipient={
        "transport_type": "apns",
    },
    push_state="Active",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

Optional trusted client identifier for the device.

##### device_secret: `str`<a id="device_secret-str"></a>

Secret value for the device.

##### form_factor: `str`<a id="form_factor-str"></a>

Form factor of the push device.

##### id: `str`<a id="id-str"></a>

Unique identifier for the device generated by the device itself.

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

Optional metadata object for this device. The metadata for a device may only be set by clients with push-admin privileges and will be used more extensively in the future with smart notifications.

##### platform: `str`<a id="platform-str"></a>

Platform of the push device.

##### push_recipient: [`Recipient`](./ably_platform_python_sdk/type/recipient.py)<a id="push_recipient-recipientably_platform_python_sdktyperecipientpy"></a>


##### push_state: `str`<a id="push_state-str"></a>

the current state of the push device.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DeviceDetails`](./ably_platform_python_sdk/type/device_details.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.subscribe_push_device_to_channel`<a id="ablypushsubscribe_push_device_to_channel"></a>

Subscribe either a single device or all devices associated with a client ID to receive push notifications from messages sent to a channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ably.push.subscribe_push_device_to_channel(
    body=None,
    channel="string_example",
    device_id="string_example",
    client_id="string_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel: `str`<a id="channel-str"></a>

Channel name.

##### device_id: `str`<a id="device_id-str"></a>

Must be set when clientId is empty, cannot be used with clientId.

##### client_id: `str`<a id="client_id-str"></a>

Must be set when deviceId is empty, cannot be used with deviceId.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Any`](./ably_platform_python_sdk/type/typing_any.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/channelSubscriptions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.unregister_all_push_devices`<a id="ablypushunregister_all_push_devices"></a>

Unregisters devices. All their subscriptions for receiving push notifications through channels will also be deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ably.push.unregister_all_push_devices(
    x_ably_version="string_example",
    format="json",
    device_id="string_example",
    client_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### device_id: `str`<a id="device_id-str"></a>

Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.

##### client_id: `str`<a id="client_id-str"></a>

Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.unregister_push_device`<a id="ablypushunregister_push_device"></a>

Unregisters a single device by its device ID. All its subscriptions for receiving push notifications through channels will also be deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ably.push.unregister_push_device(
    device_id="device_id_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's ID.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations/{device_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.push.update_push_device_details`<a id="ablypushupdate_push_device_details"></a>

Gets an updated device details object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_push_device_details_response = ably.push.update_push_device_details(
    device_id="device_id_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Device's ID.

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🔄 Return<a id="🔄-return"></a>

[`DeviceDetails`](./ably_platform_python_sdk/pydantic/device_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/push/deviceRegistrations/{device_id}/resetUpdateToken` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.stats.get_stats`<a id="ablystatsget_stats"></a>

The Ably system can be queried to obtain usage statistics for a given application, and results are provided aggregated across all channels in use in the application in the specified period. Stats may be used to track usage against account quotas.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_stats_response = ably.stats.get_stats(
    x_ably_version="string_example",
    format="json",
    start="string_example",
    limit=100,
    end="now",
    direction="backwards",
    unit="minute",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### start: `str`<a id="start-str"></a>

##### limit: `int`<a id="limit-int"></a>

##### end: `str`<a id="end-str"></a>

##### direction: `str`<a id="direction-str"></a>

##### unit: `str`<a id="unit-str"></a>

Specifies the unit of aggregation in the returned results.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/stats` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.stats.get_time`<a id="ablystatsget_time"></a>

This returns the service time in milliseconds since the epoch.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_time_response = ably.stats.get_time(
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.status.get_metadata_of_all_channels`<a id="ablystatusget_metadata_of_all_channels"></a>

Enumerate all active channels of the application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_of_all_channels_response = ably.status.get_metadata_of_all_channels(
    x_ably_version="string_example",
    format="json",
    limit=100,
    prefix="string_example",
    by="value",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### limit: `int`<a id="limit-int"></a>

##### prefix: `str`<a id="prefix-str"></a>

Optionally limits the query to only those channels whose name starts with the given prefix

##### by: `str`<a id="by-str"></a>

optionally specifies whether to return just channel names (by=id) or ChannelDetails (by=value)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.status.get_metadata_of_channel`<a id="ablystatusget_metadata_of_channel"></a>

Get metadata of a channel

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_metadata_of_channel_response = ably.status.get_metadata_of_channel(
    channel_id="channel_id_example",
    x_ably_version="string_example",
    format="json",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The [Channel's ID](https://www.ably.io/documentation/rest/channels).

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

#### 🔄 Return<a id="🔄-return"></a>

[`ChannelDetails`](./ably_platform_python_sdk/pydantic/channel_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ably.status.get_presence_of_channel`<a id="ablystatusget_presence_of_channel"></a>

Get presence on a channel

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_presence_of_channel_response = ably.status.get_presence_of_channel(
    channel_id="channel_id_example",
    x_ably_version="string_example",
    format="json",
    client_id="string_example",
    connection_id="string_example",
    limit=100,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### channel_id: `str`<a id="channel_id-str"></a>

The [Channel's ID](https://www.ably.io/documentation/rest/channels).

##### x_ably_version: `str`<a id="x_ably_version-str"></a>

The version of the API you wish to use.

##### format: `str`<a id="format-str"></a>

The response format you would like

##### client_id: `str`<a id="client_id-str"></a>

##### connection_id: `str`<a id="connection_id-str"></a>

##### limit: `int`<a id="limit-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PresenceMessage`](./ably_platform_python_sdk/pydantic/presence_message.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/channels/{channel_id}/presence` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
