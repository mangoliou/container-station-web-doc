Resource
==================


.. http:get:: /api/v1/container/(string:container_type)/(string:container_id)/all

    .. autosimple:: api.resource_all

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    resource list

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/all

    **Example response**

    .. sourcecode:: json

        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "utest",
                "port": []
            },
            "resource": {
                "device": [],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPOST -b cookies.txt -d '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}' http://${QIP}:${QPORT}/api/v1/container  -o /dev/null; 
        curl -sq -XGET -b cookies.txt 
           http://${QIP}:${QPORT}/api/v1/container/lxc/utest/all
           | python -mjson.tool

Hostname
----------

.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/network/hostname

    Update container hostname.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt -d 'yourhostname' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/hostname 

    **Example response**

    .. sourcecode:: json

        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": []
            },
            "resource": {
                "device": [],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPUT -b cookies.txt -d 'yourhostname'
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/hostname
            | python -mjson.tool;

Auto start
----------

.. http:put:: /api/v1/container/(string:container_type)/(string:container_id)/autostart/(string:state)

    Update container auto start setting.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    :param state: ``on``, ``off``

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/autostart/on
        $ curl -sq -XPUT -b cookies.txt \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/autostart/off

    **Example response**

    .. sourcecode:: json

        {
            "autostart": true,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": []
            },
            "resource": {
                "device": [],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": []
            },
            "resource": {
                "device": [],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPUT -b cookies.txt
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/autostart/on
            | python -mjson.tool;
        curl -sq -XPUT -b cookies.txt
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/autostart/off
            | python -mjson.tool;

Port Forwarding
---------------

.. http:post:: /api/v1/container/(string:container_type)/(string:container_id)/network/port

    Add port forwarding.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '[12345, 12345, "tcp"]' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/port

    **Example response**

    .. sourcecode:: json

        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": [
                    [
                        12345,
                        12345,
                        "tcp"
                    ]
                ]
            },
            "resource": {
                "device": [],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPOST -b cookies.txt -d '[12345, 12345, "tcp"]' 
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/port
            | python -mjson.tool;

.. http:delete:: /api/v1/container/(string:container_type)/(string:container_id)/network/port

    Delete port forwarding.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt -d '[12345, 12345, "tcp"]' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/port

    **Example response**

    .. sourcecode:: json

        []
        
        

        curl -sq -XDELETE -b cookies.txt -d '[12345, 12345, "tcp"]' 
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/network/port
            | python -mjson.tool;

Devices 
--------

.. http:get:: /api/v1/resource/device

    Get available device list.
    The device allows access inside container.


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET http://${QIP}:${QPORT}/api/v1/resource/device

    **Example response**

    .. sourcecode:: json

        [
            "Open_Sound_System_(OSS)",
            "Direct_Render_Infrastructure_(DRI)",
            "video4linux"
        ]
        
        

        curl -sq -XGET http://${QIP}:${QPORT}/api/v1/resource/device | python -mjson.tool;

.. http:post:: /api/v1/container/(string:container_type)/(string:container_id)/resource/device

    Add device permission.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    
    :access is a sequence of one or more of the following letters: 
        r — allows tasks to read from the specified device 

        w — allows tasks to write to the specified device 

        m — allows tasks to create device files that do not yet exist 


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '["allow", "Open_Sound_System_(OSS)", "rwm]' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/device

    **Example response**

    .. sourcecode:: json

        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": []
            },
            "resource": {
                "device": [
                    [
                        "allow",
                        "Open_Sound_System_(OSS)",
                        "rwm"
                    ]
                ],
                "limit": {}
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPOST -b cookies.txt -d '["allow", "Open_Sound_System_(OSS)", "rwm"]'
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/device
            | python -mjson.tool;

.. http:delete:: /api/v1/container/(string:container_type)/(string:container_id)/resource/device

    Delete device permission.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt -d '["allow", "Open_Sound_System_(OSS)", "rwm"]' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/device

    **Example response**

    .. sourcecode:: json

        []
        
        

        curl -sq -XDELETE -b cookies.txt -d '["allow", "Open_Sound_System_(OSS)", "rwm"]'
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/device
            | python -mjson.tool;

Limit
----------

.. http:post:: /api/v1/container/(string:container_type)/(string:container_id)/resource/limit

    Add resource limitation.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    :reqjson int cputime: (optional) [10-999]. cpu usage time in milliseconds(ms)
    :reqjson int cpuweight: (optional) [2-1024]. relative cpu usage
    :reqjson string memory: (optional) Unit in MB. Must higher than 64m

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"cputime": 100, "cpuweight": 600, "memory": "512m"}' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/limit

    **Example response**

    .. sourcecode:: json

        {
            "autostart": false,
            "image": "ubuntu-trusty",
            "name": "utest",
            "network": {
                "hostname": "yourhostname",
                "port": []
            },
            "resource": {
                "device": [],
                "limit": {
                    "cputime": 100,
                    "cpuweight": 600,
                    "memory": "512m"
                }
            },
            "type": "lxc",
            "volume": {
                "host": {}
            }
        }
        
        

        curl -sq -XPOST -b cookies.txt -d '{"cputime": 100, "cpuweight": 600, "memory": "512m"}'
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/limit
            | python -mjson.tool;

.. http:delete:: /api/v1/container/(string:container_type)/(string:container_id)/resource/limit

    Delete resource limitation.

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt -d '{"cputime": 0}' \
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/limit

    **Example response**

    .. sourcecode:: json

        []
        
        

        curl -sq -XDELETE -b cookies.txt -d '{"cputime": 0}'
            http://${QIP}:${QPORT}/api/v1/container/lxc/utest/resource/limit
            | python -mjson.tool;

