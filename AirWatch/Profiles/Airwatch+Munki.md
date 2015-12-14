# Using AirWatch with Munki

##You need 3 Devices > File/Actions:

1. **Munki Tools**: Download and install latest release. Then upload it to /Library/AW and set Manifest to Install=`/Library/AW/munkitools-xx.yy.pkg`
2. **Munki Bootstrap**: Run= `/usr/bin/touch /Users/Shared/.com.googlecode.munki.checkandinstallatstartup`
3. **Munki Forcerun**: Run=`/usr/local/munki/managedsoftwareupdate --auto`

I'm aware Forcerun is bad practice and you should reboot before. But I was told by Greg that worst case scenario nothing works until next reboot. I think I'm safe enough.

##You need one "Devices > Products":

Create a product that includes the three File/Actions before.
##You need one "Devices > Profiles":

###Custom Settings
```xml
<dict>
    <key>PayloadDisplayName</key>
    <string>MacLovin - Munki (Demonstration Setup)</string>
    <key>PayloadEnabled</key>
    <true />
    <key>PayloadIdentifier</key>
    <string>org.maclovin.munki.test</string>
    <key>PayloadUUID</key>
    <string>8214F1A8-0E65-422C-A82C-088502A14FD6</string>
    <key>PayloadType</key>
    <string>ManagedInstalls</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
    <key>SoftwareRepoURL</key>
    <string>http://munki.maclovin.org/munki_repo</string>
    <key>ClientIdentifier</key>
    <string>test_munki_client</string>
</dict>
``` 
