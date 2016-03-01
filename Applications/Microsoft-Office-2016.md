# Changing the Name and Initials

If you deployed Office 2016 with a volume license, chances are your user will complain that the name used for reviews (or Auto-Track changes) is "Microsoft Office User" with initials "MO" (or any localized variation).

It is stored here : `~/Library/Group Containers/UBF8T346G9.Office/MeContact.plist`
```bash 
minidefrancois:~ fti$ defaults read "/Users/fti/Library/Group Containers/UBF8T346G9.Office/MeContact.plist"
{
    Initials = FTI;
    Name = "Francois Levaux-Tiffreau";
}
```

#### How to script it

A simple script that sets both the Office 2016 Name and Initials values in the MeContact.plist for the currently logged in user.

```bash
#!/bin/bash
PATH=/bin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/libexec
export PATH

FullScriptName=$(basename "$0") # Variable used to store the file name of this script

DsclSearchPath="/Local/Default" # Variable used to store the search path used by the dscl command.

# Get the username of the person currently running the script.
username=$(id -un)

echo "$FullScriptName -- Personalizing Office 2016 for $username"

# Lookup the user's name from the local directory
firstname=$(dscl "$DsclSearchPath" -read /Users/$username RealName | tr -d '\n' | awk '{print $2}')
lastname=$(dscl "$DsclSearchPath" -read /Users/$username RealName | tr -d '\n' | awk '{print $3}')

# Get the first letter for the initial
firstInitial=${firstname:0:1}

# Get the first letter for the initial
lastInitial=${lastname:0:1}

# Concatenate the initials together into one variable.
UserInitials="$(echo $firstInitial$lastInitial)"

# Concatenate the full name together into one variable.
UserFullName="$(echo $firstname $lastname)"

# Remove any leading or trailing whitepace
UserFullName="$(echo -e "${UserFullName}" | sed -e 's/^[[:space:]]//' -e 's/[[:space:]]$//')"
UserInitials="$(echo -e "${UserInitials}" | sed -e 's/^[[:space:]]//' -e 's/[[:space:]]$//')"

defaults write "/Users/$username/Library/Group Containers/UBF8T346G9.Office/MeContact.plist" Name "$UserFullName"

defaults write "/Users/$username/Library/Group Containers/UBF8T346G9.Office/MeContact.plist" Initials "$UserInitials"

echo "$FullScriptName -- Completed personalizing Office 2016 for $username"

# Quit the script without errors.
exit 0
```

# Deploying Office Templates

It's technically possible to deploy your templates in `~/Library/Group Containers/UBF8T346G9.Office/User Content.localized/Templates.localized`, but unfortunately this container won't exist until the user launches an Office application. There's a better way.

Simply drop your templates in `/Library/Application Support/Microsoft/Office365/User Content.localized/Templates.localized` to get them avaiable for all users at any time. They will be available to the user in `File > New from Template…`. You can also create subfolders (won't change display). As they're directly referenced, any change to this folder will be reflected in Office (they're not copied).

#### How to script it

You can either create a package to deploy the templates at the right place, or use this script to create the directories:
```bash
# This script checks for and creates if needed the directories for Office 2016 templates for Word, PowerPoint and Excel

function test_command {
    "$@"
    local status=$?
    /bin/echo -n "Executing '$@'… "
    if [ $status -ne 0 ]; then
        echo "ERROR: $@" >&2
        exit $status
    fi
    echo "OK"

}

if [[ ! -e "/Library/Application Support/Microsoft/Office365/User Content.localized/Templates.localized" ]]; then
   /bin/echo "Necessary support directories for Office 2016 templates not found."
   /bin/echo "Creating necessary support directories for Office 2016 templates."
   test_command /bin/mkdir -p "/Library/Application Support/Microsoft/Office365/User Content.localized/Templates.localized"
   test_command /usr/sbin/chown -R root:admin "/Library/Application Support/Microsoft/Office365"
   test_command /bin/chmod -R 775 "/Library/Application Support/Microsoft/Office365"
fi
```
