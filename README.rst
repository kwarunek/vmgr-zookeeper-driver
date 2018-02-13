vmgr-zookeeper-driver
=====================

Work in progress
----------------

TODO

- lock
- revise API
- proper integration tests with docker


Introduction
------------

Provides plugin for ``vmgr`` - driver allows to store runtime data and lock management in Zookeeper.

Installation
------------

Simply use ``pip``.

:: 

    pip install vmgr-zookeeper-driver


Library requires (as well as Vmgr itself) python 3.6 or later.

Usage
-----

Install package (in the same environment as Vmgr) and configure ``Vmgr`` like:

::

    # ...

    runtime:
      driver: ZookeeperDriver
      driver_params:
        servers:
         - some.zk.host
        working_path: /vmgr
        addauth:
          auth: vmgruser:password


    # ...

Available config options
~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :header: "Name", "Type", "Description", "Default value"
   :widths: 15, 10, 40, 10

   "servers", "list", "Zookeeper hosts", ""
   "working_path", "string", "Base path where vmgr will read/write/create/deletes its nodes. A cdrwa permissions must be set for this path either to provided auth otherwise to anyone/world", "/vmgr"
   "addauth", "object", "Authentication options. If not provided or `null` no auth assumed.", "null"
   "addauth.scheme", "string", "Zookeeper's auth scheme (eg. digest sasl).", "digest"
   "addauth.auth", "string", "Auth data specific to given scheme (eg. user:password for digest)","vmgr:vmgr"

License
-------

MIT
