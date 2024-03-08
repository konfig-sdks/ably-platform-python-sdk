operation_parameter_map = {
    '/keys/{keyName}/requestToken-POST': {
        'parameters': [
            {
                'name': 'keyName'
            },
            {
                'name': 'capability'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'keyName'
            },
            {
                'name': 'nonce'
            },
            {
                'name': 'timestamp'
            },
            {
                'name': 'mac'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/channels/{channel_id}/messages-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'end'
            },
            {
                'name': 'direction'
            },
        ]
    },
    '/channels/{channel_id}/presence/history-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'end'
            },
            {
                'name': 'direction'
            },
        ]
    },
    '/channels/{channel_id}/messages-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'connectionId'
            },
            {
                'name': 'data'
            },
            {
                'name': 'encoding'
            },
            {
                'name': 'extras'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'timestamp'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/channelSubscriptions-DELETE': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'clientId'
            },
        ]
    },
    '/push/channels-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/deviceRegistrations/{device_id}-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/channelSubscriptions-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/push/deviceRegistrations-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/push/deviceRegistrations/{device_id}-PATCH': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'deviceSecret'
            },
            {
                'name': 'formFactor'
            },
            {
                'name': 'id'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'push.recipient'
            },
            {
                'name': 'push.state'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/publish-POST': {
        'parameters': [
            {
                'name': 'recipient'
            },
            {
                'name': 'push'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/deviceRegistrations/{device_id}-PUT': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'deviceSecret'
            },
            {
                'name': 'formFactor'
            },
            {
                'name': 'id'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'push.recipient'
            },
            {
                'name': 'push.state'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/deviceRegistrations-POST': {
        'parameters': [
            {
                'name': 'clientId'
            },
            {
                'name': 'deviceSecret'
            },
            {
                'name': 'formFactor'
            },
            {
                'name': 'id'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'push.recipient'
            },
            {
                'name': 'push.state'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/channelSubscriptions-POST': {
        'parameters': [
            {
                'name': 'channel'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/deviceRegistrations-DELETE': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'clientId'
            },
        ]
    },
    '/push/deviceRegistrations/{device_id}-DELETE': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/push/deviceRegistrations/{device_id}/resetUpdateToken-GET': {
        'parameters': [
            {
                'name': 'device_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/stats-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'start'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'end'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'unit'
            },
        ]
    },
    '/time-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/channels-GET': {
        'parameters': [
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'prefix'
            },
            {
                'name': 'by'
            },
        ]
    },
    '/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/channels/{channel_id}/presence-GET': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'X-Ably-Version'
            },
            {
                'name': 'format'
            },
            {
                'name': 'clientId'
            },
            {
                'name': 'connectionId'
            },
            {
                'name': 'limit'
            },
        ]
    },
};