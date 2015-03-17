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
            "logintime": "2015-03-16 17:29:52",
            "username": "nobody"
        }
        
        

        curl -sq -XPOST -c cookies.txt -d 'username=admin&password=admin' http://${QIP}:${QPORT}/api/v1/login  | python -mjson.tool

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
            "logintime": "2015-03-16 17:29:52",
            "username": "nobody"
        }
        
        

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/login_refresh | python -mjson.tool

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

    .. sourcecode:: json

        {
            "cpu_core": 2,
            "cpu_thread": 2,
            "hostname": "vagrant-ubuntu-trusty-64",
            "machine": "amd64",
            "processor": "Intel(R) Core(TM) i7-4770 CPU @ 3.40GHz",
            "version": {
                "docker_version": "1.5.0",
                "lxc_version": "1.0.7",
                "web": "unknown"
            }
        }
        
        

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system | python -mjson.tool

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
                "buffers": 102,
                "cached": 1578,
                "percent": 17,
                "percent_buffers": 2,
                "percent_cached": 39,
                "total": 3953,
                "used": 697
            }
        }
        
        

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

    .. sourcecode:: json

        {
            "used": true
        }
        {
            "used": false
        }
        
        

        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/tcp/5000 | python -mjson.tool;
        curl -sq -b cookies.txt http://${QIP}:${QPORT}/api/v1/system/port/udp/33806 | python -mjson.tool;
