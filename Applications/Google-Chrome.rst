.. only:: html

    .. sidebar:: Article information

        **Authors**: 
            * :ref:`ftiff <team-ftiff>`

Google Chrome
=============

Configure Suggested Preferences
-------------------------------

To do that, we'll create a file: ``/Library/Google/Google Chrome Master Preferences``

Use these pages as a reference:
* <https://support.google.com/chrome/a/answer/187948>
* <https://www.chromium.org/administrators/configuring-other-preferences> (may not be up to date)

For example:

.. code-block:: json

    { 
      "homepage" : "http://www.maclovin.org", 
      "homepage_is_newtabpage" : true, 
      "browser" : { 
        "show_home_button" : true, 
        "check_default_browser" : false
      },
      "bookmark_bar" : { 
        "show_on_all_tabs" : true 
      }, 
      "distribution" : { 
        "skip_first_run_ui" : true, 
        "show_welcome_page" : false, 
        "import_search_engine" : true, 
        "import_history" : false, 
        "create_all_shortcuts" : true,   
        "do_not_launch_chrome" : true, 
        "make_chrome_default" : false 
      }, 
      "first_run_tabs" : [ 
        "http://www.maclovin.org", 
        "welcome_page", 
        "new_tab_page" 
      ] 
    }

If you want to delete every user Preferences and Cache, and launch Chrome as if it was its first run, use the following commands:

.. code-block:: sh

    rm ~/Library/Preferences/com.google.Chrome.plist
    rm -rf ~/Library/Caches/Google/
    rm -rf ~/Library/Application\ Support/Google/Chrome/
    Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --force-first-run

-> `Good ressource on Google Chrome's Command Line options <http://peter.sh/experiments/chromium-command-line-switches/>`_
