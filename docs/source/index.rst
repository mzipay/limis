limis - light microservice solution
===================================
`limis <https://limis.io>`_ provides a framework for creating small services. A RESTful approach to services is
followed. In addition to traditional HTTP services a WebSocket layer is also provided. WebSockets are highly beneficial
for services due to their two-way communication pattern and single socket connection for multiple calls.
`Tornado <https://www.tornadoweb.org>`_ provides the communication back-bone for limis, The Tornado framework enables
limis to build services on a well established transport platform.

.. warning:: limis is currently an alpha release. There may be significant bugs, and class, methods, variable names may
    change prior to the beta release.

.. toctree::
    :maxdepth: 2
    :caption: Introduction

    introduction/overview
    introduction/installation

.. toctree::
    :maxdepth: 2
    :caption: Reference

    modules/core
    modules/management
    modules/server
    modules/services

    documentation_index
