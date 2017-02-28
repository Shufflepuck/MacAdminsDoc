
#Using AirWatch API
## Initial Setup

According to the "AirWatch REST API Guide" PDF document that you can get in https://my.air-watch.com, you need:

- **the URL**: https://<host>/API/v1/help
- **the Token**: aw-tenant-code (or API Key)
- **Authorization**: Basic base64.b64encode("username:password")

### Enable Basic Authentication and get the Token

1. Select the right Organization Group (eg. Root)
2. Enable Basic Authentication from `Groups > Groups & Settings > System > Advanced > API > REST > Authentication`
2. Go to `Group & Settings > System > Advanced > API > REST > General`
3. Tick “Enable API Access” & add a service. Entering a service name will generate an API Key, which we’ll need for API calls.

> NOTE: This was called "Tenant Code" or "aw-tenant-code" previously & in the current (8.2) API documentation & will be referred as such within this post.[^accessing-airwatchs-rest-api-with-python]

[^accessing-airwatchs-rest-api-with-python]: https://macmule.com/2015/12/14/accessing-airwatchs-rest-api-with-python/

### Authorization

The easiest way is to use Basic authentication.

1. Make sure your admin has the correct role. In production, you should create a custom Role, but for test, Console Administrator is fine. Make sure he's in the correct OG, of course.
2. The form should be "username:password", encoded using Base64. You can do this on OS X terminal (see below)

```bash
$ python -c "import base64; print base64.b64encode('login:password')"
bG9naW46cGFzc3dvcmQ=
```

### Testing

#### Testing with Curl

```bash
$ curl -X "GET" "https://host.awmdm.com/API/v1/help" \ -H "Authorization: Basic bG9naW46cGFzc3dvcmQ=" \ -H "aw-tenant-code: bG9naW46cGFzc3dvcmFzZG/2FmYXNkZmFkc2Zhc2Zk="
```

#### Testing with Python

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

## Queries (using Python)

I suggest using a REST editor to test your parameters, such as [Paw](https://luckymarmot.com/paw). It can also automatically generates python code.

### Opening Request


```python
import requests

# Set your console URL (eg. 'http://cn23.awmdm.com')
consoleURL = 'http://cn23.awmdm.com'

# Maximum set of values (1-10000 - default: 500)
lookupLimit = '500'

# Base64 encoded 'login:password' -- discouraged in production
b64EncodedAuth = 'bG9naW46cGFzc3dvcmQ='

# Your tenant code (see above)
tenantCode = 'bG9naW46cGFzc3dvcmFzZG/2FmYXNkZmFkc2Zhc2Zk='

# Your request. See API documentation.
request = '/API/v1/mdm/devices/search'

# It's a good idea to enclose the following in a try-except format.
try:
    # API call, pulling in all Employee Owned devices from the OG "All Peoples Devices"
    request = requests.get(consoleURL + request + "?pagesize=" + lookupLimit, 
              headers={"Authorization": "Basic " + b64EncodedAuth,
                       "aw-tenant-code": tenantCode,
                       "Accept": "application/json"},
              timeout=30)

    # If the above gives a 4XX or 5XX error
    request.raise_for_status()
    
    # Insert your code here

except requests.exceptions.RequestException as e:
    print 'Get request failed with %s' % e
```


### Getting all devices

`request = '/API/v1/mdm/devices/search'`

```python
	# Get the JSON from the above
	deviceDetails = request.json()
	
	# Pull in the "Devices' dict only
	deviceDetails = deviceDetails['Devices']
	
	# For each device in deviceDetails
	for device in deviceDetails:
	
		# Log each devices one by one
		print device
```

## Using with OS X Clients

Unfortunately, the API doesn't -yet- support all the features from OS X Clients:
```xml
<AirWatchFaultContract xmlns="http://www.air-watch.com/" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <ActivityId>56b6ed75-30a2-418e-84fa-f8e04d35506a</ActivityId>
  <ErrorCode>501</ErrorCode>
  <Message>Functionality not supported for device type : AppleOsX</Message>
</AirWatchFaultContract>
```
