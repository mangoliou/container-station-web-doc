System
=============

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

    .. sourcecode:: json

        {
            "anonymous": false,
            "isAdmin": false,
            "logintime": "2015-05-19 08:05:54",
            "username": "nobody"
        }
        
        
.. http:get:: /api/v1/login_refresh

    .. autosimple:: api.login_refresh

    :resjson boolean isAdmin: is administrator group or not
    :resjson string username: request username

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/login_refresh

    **Example response**

    .. sourcecode:: json

        {
            "anonymous": false,
            "isAdmin": false,
            "logintime": "2015-05-19 08:05:54",
            "username": "nobody"
        }
        
        
.. http:put:: /api/v1/logout

    .. autosimple:: api.logout

    :resjson string username: request username

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt http://${QIP}:${QPORT}/api/v1/logout

    **Example response**

    .. sourcecode:: json

        {
            "username": "nobody"
        }
        
        
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

    .. sourcecode:: json

        {
            "cpu_core": 2,
            "cpu_thread": 2,
            "hostname": "vagrant-ubuntu-trusty-64",
            "machine": "amd64",
            "processor": "Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz",
            "version": {
                "docker_version": "1.6.1",
                "lxc_version": "1.0.7",
                "web": "unknown"
            }
        }
        
        
.. http:get:: /api/v1/system/resource

    .. autosimple:: api.system_resource_info

    :resjson string cpu_usage: CPU usage in percentage
    :resjson object memory_usage: Memory usage in MB

    **Example request**

    .. sourcecode:: bash

        $ curl -sq http://${QIP}:${QPORT}/api/v1/system/resource

    **Example response**

    .. sourcecode:: json

        {
            "cpu_usage": "0.0",
            "memory_usage": {
                "buffers": 125,
                "cached": 1634,
                "percent": 23,
                "percent_buffers": 3,
                "percent_cached": 41,
                "total": 3953,
                "used": 913
            }
        }
        
        
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

    .. sourcecode:: json

        {
            "used": true
        }
        {
            "used": false
        }
        
        
