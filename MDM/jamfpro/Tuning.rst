:Title: JSS Tuning
:Author: Mosen

JSS Tuning
==========

.. warning:: Do not attempt to make any of these changes without a Backup of your JSS Database.

Java & Tomcat
-------------

- See `Rich Trouton's Post <https://derflounder.wordpress.com/2016/04/17/performance-tuning-for-the-casper-jss/>`_

Database
--------

optimizer_search_depth
^^^^^^^^^^^^^^^^^^^^^^^

For some reason this is recommended to be set to **3**.
I believe this is to stop MariaDB/MySQL from coming up with too many execution plans.

key_buffer_size
^^^^^^^^^^^^^^^

As per this `article <https://mariadb.com/kb/en/mariadb/optimizing-key_buffer_size/>`_, key buffer size should be set to
about 25% or more of the available server RAM.

query_cache_size
^^^^^^^^^^^^^^^^

See `article <https://mariadb.com/kb/en/mariadb/query-cache/>`_, Set to 0.

query_cache_type
^^^^^^^^^^^^^^^^

Set to 0 to disable the query cache.

(ignore) Table Storage: InnoDB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changing the table storage might have far reaching implications for you so I don't recommend this now, but these settings were recommended::

    innodb_log_file_size=512M
    innodb_flush_log_at_trx_commit=1
    innodb_file_per_table=1
    innodb_buffer_pool_size=amount_of_RAMG # 60% or more of your total ram
    innodb_buffer_pool_instances=8
    