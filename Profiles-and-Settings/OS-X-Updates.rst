macOS Updates
=============

com.apple.commerce
------------------

* **AutoUpdate** → Install app updates
* **AutoUpdateRestartRequired** → Install OS X updates

com.apple.SoftwareUpdate
------------------------

* **AutomaticCheckEnabled** → Automatically check for updates
* **AutomaticDownload** → Download newly available updates in the background
* **ConfigDataInstall** → Install system data files
* **CriticalUpdateInstall** → Install security updates ([Der Flouder](https://derflounder.wordpress.com/2014/12/24/managing-os-xs-automatic-security-updates/))
* **AllowPreReleaseInstallation** → Allow OS X Beta ([HT203018](https://support.apple.com/HT203018))

Deploying
---------

As of 2015.12.14, deploying com.apple.commerce doesn't work as profiles. You can use this `script <https://github.com/74bit/74bit_scripts/blob/master/enableOSXAutomaticUpdates/enableOSXAutomaticUpdates.sh>`_.

With Casper Suite
^^^^^^^^^^^^^^^^^

1. Create a `script <https://github.com/ftiff/ftiff-scripts/blob/master/bash/set-osx-autoupdates.sh>`_ from "Computer Management > Scripts"
2. Create a Policy "Once per Computer" to execute this script
3. Create a Policy "Once per Week" with Software Updates > Install Software Updates from "Each computer's default software update server". Don't forget to set restart options.
