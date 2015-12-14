# How to use the REST API

According to the "AirWatch REST API Guide" PDF document that you can get in https://my.air-watch.com, you need:

- **the URL**: https://<host>/API/v1/help
- **the Token**: aw-tenant-code (or API Key)
- **Authorization**: Basic base64.b64encode("username:password")

## How to find the Token

1. Select the right Organization Group
2. Go to Group & Settings > System > Advanced > API > REST > General
3. Select "Override"
4. an API Key will be generated. This is your "aw-tenant-code"

## Authorization

The easiest way is to use Basic authentication.

1. Make sure your admin has the correct role. In production, you should create a custom Role, but for test, Console Administrator is fine. Make sure he's in the correct OG, of course.
2. The form should be "username:password", encoded using Base64. You can do this on OS X terminal (see below)

```bash
$ python -c "import base64; print base64.b64encode('login:password')"
bG9naW46cGFzc3dvcmQ=
```

## Testing

### Testing with Curl

```bash
$ curl -X "GET" "https://host.awmdm.com/API/v1/help" \ -H "Authorization: Basic bG9naW46cGFzc3dvcmQ=" \ -H "aw-tenant-code: bG9naW46cGFzc3dvcmFzZG/2FmYXNkZmFkc2Zhc2Zk="
```

### Testing with Python

```python
# Install the Python Requests library:
# from bash: pip install requests

import requests


def send_request():
    # My API
    # GET https://host.awmdm.com/API/v1/help

    try:
        response = requests.get(
            url="https://host.awmdm.com/API/v1/help",
            headers={
                "Authorization": "Basic bG9naW46cGFzc3dvcmQ=",
                "aw-tenant-code": "bG9naW46cGFzc3dvcmFzZGZ/2FmYXNkZmFkc2Zhc2Zk=",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')
```

Or just use Paw https://luckymarmot.com/paw ;-)

## Using with OS X Clients

Unfortunately, the API doesn't -yet- support all the features from OS X Clients:
```xml
<AirWatchFaultContract xmlns="http://www.air-watch.com/" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <ActivityId>56b6ed75-30a2-418e-84fa-f8e04d35506a</ActivityId>
  <ErrorCode>501</ErrorCode>
  <Message>Functionality not supported for device type : AppleOsX</Message>
</AirWatchFaultContract>
```
