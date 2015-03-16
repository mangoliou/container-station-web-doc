System
=============

.. automodule:: ctstation


Authentication
------------------

.. http:post:: /api/v1/login

    .. autosimple:: api.login

    :resjson boolean isAdmin: is administrator group or not
    :resjson string username: request username

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -c cookies.txt -d 'username=admin&password=admin' \
              http://${QIP}:${QPORT}/api/v1/login

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -c cookies.txt -d 'username=admin&password=admin' http://${QIP}:${QPORT}/api/v1/login  | python -mjson.tool

.. http:get:: /api/v1/login_refresh

    .. autosimple:: api.login_refresh

    :resjson boolean isAdmin: is administrator group or not
    :resjson string username: request username

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/login_refresh

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/login_refresh | python -mjson.tool

.. http:put:: /api/v1/logout

    .. autosimple:: api.logout

    :resjson string username: request username

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/logout

    **Example response**

    .. runcode:: json

        curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/logout | python -mjson.tool

System Information
------------------

.. http:get:: /api/v1/system

    .. autosimple:: api.system_info

    :resjson int cpu_core: CPU core count
    :resjson int cpu_thread: Total CPU thread count
    :resjson string hostname: Device hostname
    :resjson string processor: Processor information
    :resjson string machine: Machine type, e.g. 'x86_64', 'armv7l'. An empty string is returned if the value cannot be determined.
    :resjson object version: Version of Docker, LXC, and container-station-web


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system

    **Example response**

    .. runcode:: json

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system | python -mjson.tool

.. http:get:: /api/v1/system/resource

    .. autosimple:: api.system_resource_info

    :resjson string cpu_usage: CPU usage in percentage
    :resjson object memory_usage: Memory usage in MB

    **Example request**

    .. sourcecode:: bash

        $ curl -sq http://${QIP}:${QPORT}/api/v1/system/resource

    **Example response**

    .. runcode:: json

        curl -sq http://${QIP}:${QPORT}/api/v1/system/resource | python -mjson.tool

System Port 
------------------

.. http:get:: /api/v1/system/port/(string:protocol)/(string:port)

    .. autosimple:: api.system_port_check

    :resjson boolean used: The port has been used or not.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/tcp/5000
        $ curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/udp/33806

    **Example response**

    .. runcode:: json

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/tcp/5000 | python -mjson.tool;
        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/udp/33806 | python -mjson.tool;
