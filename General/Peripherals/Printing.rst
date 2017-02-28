Printing
========
On OS X, the printing subsystem is CUPS. 

Ways to modify CUPS configuration
---------------------------------

- System Preferences > Printers & Scanners
- `<http://localhost:631/>`_
- ``sudo lpadmin``

Options
-------

Set default printer
^^^^^^^^^^^^^^^^^^^

``sudo lpadmin -d [printer]``

Enable Kerberos Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``sudo lpadmin -p [printer] -o auth-info-required=negotiate``

You can eventually follow `this article <https://support.apple.com/en-us/HT202311>`_ from Apple.

Change default options
^^^^^^^^^^^^^^^^^^^^^^

To change defaults, use this command: ``sudo lpadmin -p [printer] -o [option]=[value]``. For example: ``sudo lpadmin -p Follow-Me -o XRBannerSheet=None``

List available options 
^^^^^^^^^^^^^^^^^^^^^^

Use ``lpoptions -p [printer] -l``.

Notable options
^^^^^^^^^^^^^^^

==================      ==================================================================================    ======================================================
Option                  Values                                                                                Description
==================      ==================================================================================    ======================================================
printer_is_shared       true/false                                                                            share printer 
auth-info-required      "none", "username,password", "domain,username,password", or "negotiate" (Kerberos)    Set to ``negotiate`` to allow Kerberos
media                   Letter A4…                                                                            See `here <http://www.cups.org/documentation.php/doc-2.1/options.html?VERSION=2.1>`_ for more info
XRBannerSheet           \*None AtStart                                                                         On Xerox, displays the coverpage with Job ID
==================      ==================================================================================    ======================================================

More info `here <http://www.cups.org/documentation.php/doc-2.1/options.html?VERSION=2.1>`_

Discovering options
^^^^^^^^^^^^^^^^^^^

This will allow you to make changes using a GUI, and find the right option.

Using GUI
"""""""""

1. Open print dialog
2. Create a preset
3. execute ``defaults read ~/Library/Preferences/com.apple.print.custompresets.forprinter.[printer].plist [preset] > before.txt``
4. Make changes
5. Create a new preset
6. execute ``defaults read ~/Library/Preferences/com.apple.print.custompresets.forprinter.[printer].plist [new_preset] > after.txt``
7. See differences with ``diff before.txt after.txt``

Using CUPS Web
""""""""""""""

I found it quite interesting to follow this:

1. ``lpoptions -p [printer] -l > before.txt``
2. Make the changes on `<http://localhost:631/printers/>`_ > Printer > Set default Options
3. Run ``lpoptions -p [printer] -l > after.txt``
4. See differences with ``diff before.txt after.txt``


Adding a printer
----------------

Network Printer
^^^^^^^^^^^^^^^
The command to install a printer is ``lpadmin``. You will need to specify:

- ``-E`` to Enable the destination and accept jobs
- ``-p [name]``: name of the printer
- ``-v [uri]``: path to the queue (smb://server/queue)
- ``-P [PPD]``: path to PPD (usually in /Library/Printers/PPDs/Contents/Resources/)
- ``-o [option]=[value]``: specify options


Example
""""""""

.. code-block:: bash

    #!/bin/bash
    #
    # Installs printer, using Xerox Drivers (Xerox_Print_Driver_3.52.0.pkg)
    # 
    
    readonly LPSTAT='/usr/bin/lpstat'
    readonly LPADMIN='/usr/sbin/lpadmin'
    readonly CUPSENABLE='/usr/sbin/cupsenable'
    readonly CUPSACCEPT='/usr/sbin/cupsaccept'
    
    
    #######################################
    # Add printers using cups
    # Globals:
    #   LPSTAT
    #   LPADMIN
    #   CUPSENABLE
    #   CUPSACCEPT
    # Arguments:
    #   name
    #   uri
    #   ppd
    # Returns:
    #   None
    #######################################
    
    add_printer() {
    
      local name="$1"
      local uri="$2"
      local ppd="$3"
    
      if ! ${LPADMIN} -E -p "${name}" \
        -v "${uri}" \
        -P "${ppd}" \
        -o printer_is_shared=false \
        -o auth-info-required=negotiate \
        -o XRBannerSheet=None \
        -o media=iso_a4_210x297mm; then
          echo "ERROR: ${name}: Unable to lpadmin (add printer)" >&2
          exit -1
      fi
      
      # cupsaccept and cupsenable are not needed before of '-E'. I don't remember why I included them.
      if ! ${CUPSACCEPT} "${name}"; then
        echo "ERROR: ${name}: Unable to cupsaccept." >&2
        exit -1
      fi
    
      if ! ${CUPSENABLE} "${name}"; then
        echo "ERROR: ${name}: Unable to cupsenable." >&2
        exit -1
      fi
    }
    
    if (! ${LPSTAT} -v "Follow-Me"); then
      add_printer "Follow-Me" \
                  "smb://printserver.fti.io/Follow-Me%20Xerox%20(PCL6)" \
                  "/Library/Printers/PPDs/Contents/Resources/Xerox WC 7545.gz"
    fi
    
    
    exit 0

