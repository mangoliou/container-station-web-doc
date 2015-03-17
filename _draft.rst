Draft
======================

create container
-----------------

.. sourcecode:: json

    {
        "type": "lxc",
        "name": "utest",
        "image": "ubuntu-trusty",
        "tag": "latest",
        "environment": [
            "QPORT=90", 
            "QIP=1.2.3.4"
        ],
        "links": {
            "CT1": "DB1", 
            "CT2": "DB2"
        },
        "command": "/bin/bash",
        "user": "ubuntu",     
        "working_dir": "/tmp",
        "network": {
            "hostname": "CustomHostName",
            "dns": ["192.168.101.123"],
            "expose_port": [22,80,8080],
            "port": [
                [ 22222, 22, "tcp" ],
                [ 12345, 1234, "udp" ]
            ]
        },
        "resource": {
            "limit": {
                "cpuweight": 512,
                "cputime":   512,
                "memory": "768m"
            },
            "device": [
                [ "allow", "Open_Sound_System_(OSS)", "rw" ]
            ]
        },
        "volume": {
            "host":{
                "/test": {
                    "bind": "/mnt/vol1",
                    "ro": true
                },
                "/test/image": {
                    "bind": "/mnt/vol2",
                    "ro": false
                }
            },
            "container":[
                "DockerTest",
                "DockerTest2"
            ],
            "new":[ "/tmp/New1", "/tmp/New2" ]
        }
    }



System log
------------------

.. http:delete:: /api/v1/log

    Clear logs from database.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/log


.. http:post:: /api/v1/log/rotate

    UI doesn't have this Specs.

    :reqjson day: (required) Set how many days of logs retain in database.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt \
            -d '{"day": 50}' http://${QIP}:${QPORT}/api/v1/log/rotate
