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

## How to script it

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
