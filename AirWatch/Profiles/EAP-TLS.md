# Using a EAP-TLS certificate with WPA2 Enterprise (802.11x)

## Pre-requisites:

1. Use a cloud connector and configure Enterprise Integration to request a certificate from your Active Directory CA (ADDS) -- Not covered here
2. Create a single profile.

In this profile, you'll add two payloads:

### Credentials (order is important):
1. First tab: Upload your CA, and select "Allow access to all applications" and "Allow export from Keychain"
2. Second tab: use your machine certificate (uncheck everything)
###Network:
1. check Auto-Join
2. WPA/WPA2 Enteprise. For some reason, if I choose only "WPA2 Enterprise", it fails. But it will then connect as WPA2.
3. Uncheck "User logs in to authenticate with the network"
4. Protocols: EAP-TLS
5. Username: {EnrollmentUser}
6. Identity Certificate: Certificate #2 (This is why order is important).
7. Trusted certificates: Check both
8. Allow trust exceptions: Check
