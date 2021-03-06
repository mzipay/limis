limis
=====
.. image:: https://travis-ci.org/limis-project/limis.svg?branch=master
    :alt: limis build status
    :target: https://travis-ci.org/limis-project/limis

.. image:: https://codecov.io/gh/limis-project/limis/branch/master/graph/badge.svg
    :alt: limis coverage status
    :target: https://codecov.io/gh/limis-project/limis

limis is a light microservice framework built in `Python <https://www.python.org/>`_ and powered by
`Tornado <https://www.tornadoweb.org/>`_.

.. warning::
    The project is currently in active development and should be considered alpha grade at the moment. Features are
    being added and removed and expect the API to change frequently. Release 0.1 is targeted to be a more stable
    release.

Examples: limis examples can be found on github at `limis_examples <https://github.com/limis-project/limis_examples>`_

Instructions
------------

Installation
~~~~~~~~~~~~
.. code-block::

    pip install limis

Project Creation
~~~~~~~~~~~~~~~~
.. code-block::

    limis-management create_project <project_name>

Service Creation
~~~~~~~~~~~~~~~~
* Scaffold the services with the project management command:

.. code-block::

    cd <project_name>
    python management.py create_service <service_name>

* Create a request handler to route service requests to your component in '<service_name>/handlers.py':

.. code-block:: python

    from typing import Union

    from tornado.websocket import WebSocketHandler
    from limis.services.handlers import ComponentHandler


    class HelloHTTPHandler(ComponentHandler):
        def get(self):
            self.write(self.component_class().hello())


    class HelloWebSocketHandler(ComponentHandler, WebSocketHandler):
        def on_message(self, message: Union[str, bytes]):
            self.write_message(self.component_class().hello())

* Create a component to perform actions on requests in '<service_name>/components.py':

.. code-block:: python

    from limis.services.components import Component

    from hello.handlers import HelloHTTPHandler, HelloWebSocketHandler


    class HelloComponent(Component):
        component_name = 'hello'
        component_path = 'hello'
        component_http_handler = HelloHTTPHandler
        component_websocket_handler = HelloWebSocketHandler

        def hello(self):
            return 'hello'

* Create a services configuration entry in '<service_name>'/services.py:

.. code-block:: python

    from limis.services import Service

    from hello.components import HelloComponent


    services = [
        Service(name='hello', path='hello', components=[HelloComponent]),
    ]

* Add your services module to the project services configuration '<project_name>/services.py':

.. code-block:: python

    from hello.services import services as hello_services


    context_root = ''
    services = hello_services

Launch Server
~~~~~~~~~~~~~
Launch the limis server from the command prompt:

.. code-block::

    python manage.py server --http --websocket

Test Service
~~~~~~~~~~~~

* HTTP Service

.. code-block::

    curl http://localhost:8080/hello/hello

Output:

.. code-block::

    hello

* WebSocket Service

Example using `websocket-client <https://github.com/websocket-client/websocket-client>`_

.. code-block:: python

    from websocket import create_connection
    websocket = create_connection('ws://localhost:8888/hello/hello/')
    websocket.send('test')
    websocket.recv()

Output:

.. code-block::

    hello