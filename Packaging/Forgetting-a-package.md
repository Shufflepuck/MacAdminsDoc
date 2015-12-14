Forgetting a package is a good way to troubleshoot some behaviours. It doesn't change anything on disk, but the computer will believe the package was never installed.

# Installer.app/SWU

For OS X packages, installed by Installer.app or Software update, use `sudo pkgutil --forget [package_id]`. You can list current installed packages with `pkgutil --pkgs`

This will get updated at next recon to Inventory > Package Receipts > Installer.app/SWU.

Note: According to pkgutil(1)
> Discard all receipt data about package-id, but do not touch the installed files.  DO NOT use this command from an installer package script to fix broken package design.

# Casper Suite

To change this (unrelated) list, you need to delete the relevant file in `/Library/Application Support/JAMF/Receipts`, then do a `sudo jamf recon`

Again, this doesn't do anything but change inventory.
