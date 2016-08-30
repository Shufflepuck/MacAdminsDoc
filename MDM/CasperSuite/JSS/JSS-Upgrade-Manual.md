# Upgrade JSS, the Manual way


## Disclaimer
I'm just listing what I usually do to upgrade JSS. If you have a better idea, please [contribute](https://github.com/Shufflepuck/MacAdminsDoc/blob/master/00_About/Contributing.md)! 

Please first test on a test JSS.


## Backup, Backup, Backup!
Make sure you have a working backup before doing anything. 
I use the following command:
`java -jar /usr/local/jss/bin/JSSDatabaseUtil.jar backup -saveBackupTo ~/ -server jamf-mysql1.sdfsfsaa111.eu-west-1.rds.amazonaws.com -pass`
This will save the backup in your user home folder. Send it to another computer.

In general, please follow this article: [Preparing to Upgrade the JSS](https://jamfnation.jamfsoftware.com/article.html?id=136)

## Prepare the JSS Installer
Download the JSS Installer from JAMF Nation. 

1. Connect to JAMF Nation
2. Go to [My Assets](https://jamfnation.jamfsoftware.com/myAssets.html)
3. Click "Show JSS installer downloads"
4. Download JSS Manual Installation
5. Upload it to your Linux box
6. Unzip it, and you're ready to go!

Note: I usually upload it to my Distribution Point, and get it from my Ubuntu server using:

`curl https://login:password@dp-1.fti.io/JSS_Installers/JSSInstallation9.93.zip --digest -k -O`

## Upgrade JSS
If you have a Clustered JSS, please read [Upgrading the JSS in a Clustered Environment](https://jamfnation.jamfsoftware.com/article.html?id=212). 

First, let's stop the JSS:

`service jamf.tomcat7 stop`

Then archive the current install to `~/ROOT-war-20160830.tgz`:
```sh
tar czf ~/ROOT-war-20160830.tgz /usr/local/jss/tomcat/webapps/
rm -rf /usr/local/jss/tomcat/webapps/*
```

Copy the new ROOT.war and restart tomcat:
```sh
mv JSSInstallation/JSS\ Components/ROOT.war /usr/local/jss/tomcat/webapps/
service jamf.tomcat7 start
```

Just reconfigure the database, and everything should be working again!

## If something goes wrong

Read the logs in `/usr/local/jss/tomcat/logs/`. Worst case, restore from backup and use the Linux automatic updater.
