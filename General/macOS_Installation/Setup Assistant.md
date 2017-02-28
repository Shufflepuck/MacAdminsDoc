Setup Assistant
===============

Setup Assistant is also called "MacBuddy"

Setup Assistant Steps
--------------------------------


+----+--------------------+------------+-----------------+--------------+
|Name|Log Short Name		| MDM Key 	| MDM Skippable? | File Trigger |
+====+=====================+============+================+==============+
|Choose Language|||No| | `/var/db/.AppleSetupDone`|
|Select Keyboard|SelectKeyboard		|				| No	| `/var/db/.AppleSetupDone`|
|Network Setup|SelectWiFiNetwork	|				| No	| `/var/db/.AppleSetupDone`|
| Transfer Data |MigrationWelcome	| Restore 	| Yes | `/var/db/.AppleSetupDone`|
|Location Services|EnableCoreLocation	| Location	| Yes | `/var/db/.AppleSetupDone`|
|Apple ID and iCloud Sign-in|iCloudLogin			| AppleID 	| Yes | `com.apple.SetupAssistant.plist` |
|Terms and Conditions|LicenseViewer		| TOS 			| Yes |  `/var/db/.AppleSetupDone`|
|Create User Account|CreateUserAccount	|				| Yes*	| `/var/db/.AppleSetupDone`|
|Automatically sending diagnostic information|DiagnosticsAndUsage| Diagnostics| Yes |`com.apple.SetupAssistant.plist` |
|Siri|EnableSiri			| Siri 		| Yes | `/var/db/.AppleSetupDone`|
| Touch ID|| Biometric|Yes | `/var/db/.AppleSetupDone`|
| Apple Pay|| Payment| Yes| `/var/db/.AppleSetupDone`|
|Setting Up Your Mac|SettingUpYourMac	|				| No	| `/var/db/.AppleSetupDone`|


\*Initial User Creation can be skipped under certain conditions



Skipping Setup Assistant
--------------------------------

With an MDM
^^^^^^^^^^^

Having a MDM can allow skipping some steps.

More info on MDM protocol [here](https://developer.apple.com/library/prerelease/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/4-Profile_Management/ProfileManagement.html#//apple_ref/doc/uid/TP40017387-CH7-SW50) (search for `skip_setup_items`)

By messing with some files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setup Assistant will only launch if `/var/db/.AppleSetupDone` is not present. Deleting this key will skip most of the steps.

`/Users/[username]/Library/Preferences/com.apple.SetupAssistant.plist` will store iCloud/Apple ID setup and Diagnostic Information agreement. More info on [Rich's blog](https://derflounder.wordpress.com/2014/10/16/disabling-the-icloud-and-diagnostics-pop-up-windows-in-yosemite/)

Mager Valp has an [interesting script](https://github.com/MagerValp/SkipAppleSetupAssistant) you might want to check.