Log and Event
=============

Log
------------------

.. http:get:: /api/v1/log

    :query time_start: (optional) Time stamp of system logs start time (epoch). **Default is 0.**
    :query time_end: (optional) Time stamp of system logs end time (epoch). **Default is 0.**
    :query limit: (optional) Number of system log records. **Default is 20.**
    :query offset: (optional) Response logs start with.
    :query user: (optional) User name who login.
    :query level: (optional) Log level like ``INFO``, ``WARN``, ``ERROR``. Append with comma(,) if you want to filter with more than two levels.
    :query category: (optional) Function category like ``container``, ``image``, ``import``, ``export``, ``backup``, ``system``. Append with comma(,) if you want to filter with more than two categories.
    :query text: (optional) Filter text

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/log?limit=5&category=image,export"

    **Example response**

    .. sourcecode:: json

        [
            {
                "category": "export",
                "id": 50,
                "level": "INFO",
                "message": "Finished export container (docker, 1753ab55c36e, DockerTestAPI) to /test/d.tgz",
                "ts": 1432022739,
                "user": "Anonymous"
            },
            {
                "category": "image",
                "id": 49,
                "level": "INFO",
                "message": "Finished to download image from dockerhub (docker, lgsd/diamond:latest)",
                "ts": 1432022737,
                "user": "Anonymous"
            },
            {
                "category": "export",
                "id": 48,
                "level": "INFO",
                "message": "Start to export container (docker, 1753ab55c36e, DockerTestAPI) to /test/d.tgz",
                "ts": 1432022730,
                "user": "Anonymous"
            },
            {
                "category": "export",
                "id": 47,
                "level": "INFO",
                "message": "Finished export container (lxc, utest) to /test/c.tgz",
                "ts": 1432022730,
                "user": "Anonymous"
            },
            {
                "category": "export",
                "id": 46,
                "level": "INFO",
                "message": "Export task logs are cleared",
                "ts": 1432022726,
                "user": "Anonymous"
            }
        ]
        
        
.. http:get:: /api/v1/log/export

    Export logs to csv format.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/log/export

    **Example response**

    .. sourcecode:: text

        Date,Level,Category,User,Message
        2015-05-19 08:03:53.173968,INFO,container,Anonymous,Create a new redmine application: test
        2015-05-19 08:03:54.900782,INFO,container,Anonymous,"Destroy container (lxc, ctest)"
        2015-05-19 08:03:54.982283,INFO,container,Anonymous,"Start to do background task (create, ctest)"
        2015-05-19 08:03:55.044036,INFO,container,Anonymous,"Stop container (docker, b1d73c45086f, dtest)"
        2015-05-19 08:03:55.074089,INFO,container,Anonymous,"Destroy container (docker, b1d73c45086f, dtest)"
        2015-05-19 08:03:55.334810,INFO,backup,Anonymous,Add backup target testsite (127.0.0.1:5000)
        2015-05-19 08:03:55.761119,INFO,backup,Anonymous,Update backup target testsite (127.0.0.1:5000)
        2015-05-19 08:03:55.817075,INFO,backup,Anonymous,Remove backup target testsite (127.0.0.1:5000)
        2015-05-19 08:03:56.498284,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-05-19 08:03:56.932014,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-05-19 08:03:56.946959,INFO,backup,system,"Finished backup container (lxc, utest)"
        2015-05-19 08:03:57.273933,INFO,backup,system,"Start to restore container (lxc, utest)"
        2015-05-19 08:03:57.286040,ERROR,backup,system,"Backup error: [[Errno 2] No such file or directory: '/home/vagrant/container-station-web/ctstation/../tmp/tmpbyr9kv/metadata'] (lxc, utest)"
        2015-05-19 08:03:57.296792,INFO,backup,system,"Finished restore container (lxc, utest)"
        2015-05-19 08:03:57.645748,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-05-19 08:03:57.655533,INFO,backup,system,"Finished backup container (lxc, utest)"
        2015-05-19 08:04:07.866309,INFO,container,Anonymous,"Create container (lxc, ctest)"
        2015-05-19 08:04:08.234364,INFO,container,Anonymous,"Finished background task (create, ctest)"
        2015-05-19 08:04:08.249760,INFO,container,Anonymous,"Start to do background task (create, dtest)"
        2015-05-19 08:04:08.533218,INFO,container,Anonymous,"Create container (docker, 4a3633b8730d, dtest)"
        2015-05-19 08:04:08.546143,INFO,container,Anonymous,"Finished background task (create, dtest)"
        2015-05-19 08:04:59.874611,INFO,image,Anonymous,"Start to download image from qnap (lxc, ubuntu-trusty:latest)"
        2015-05-19 08:04:59.887517,WARN,image,Anonymous,"Download: ubuntu-trusty:latest (qnap, lxc, ubuntu-trusty:latest)"
        2015-05-19 08:05:01.280748,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-05-19 08:05:04.995096,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-05-19 08:05:05.220879,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-05-19 08:05:06.461266,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-05-19 08:05:06.866338,INFO,container,Anonymous,"Stop container (docker, e0360e6fe8ee, DockerTestAPI)"
        2015-05-19 08:05:06.897210,INFO,container,Anonymous,"Destroy container (docker, e0360e6fe8ee, DockerTestAPI)"
        2015-05-19 08:05:07.184924,INFO,container,Anonymous,"Create container (docker, 1753ab55c36e, DockerTestAPI)"
        2015-05-19 08:05:07.543961,INFO,container,Anonymous,"Create container (docker, 11abb7a227d7, DockerTestAPI2)"
        2015-05-19 08:05:08.875218,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-05-19 08:05:09.418246,INFO,container,Anonymous,"Start container (lxc, utest)"
        2015-05-19 08:05:09.470956,INFO,container,Anonymous,"Stop container (docker, 1753ab55c36e, DockerTestAPI)"
        2015-05-19 08:05:09.625173,INFO,container,Anonymous,"Start container (docker, 1753ab55c36e, DockerTestAPI)"
        2015-05-19 08:05:10.830863,INFO,container,Anonymous,"Restart container (lxc, utest)"
        2015-05-19 08:05:11.057968,INFO,container,Anonymous,"Restart container (docker, 1753ab55c36e, DockerTestAPI)"
        2015-05-19 08:05:16.311245,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-05-19 08:05:16.366120,INFO,container,Anonymous,"Stop container (docker, 1753ab55c36e, DockerTestAPI)"
        2015-05-19 08:05:16.586827,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-05-19 08:05:16.685231,INFO,container,Anonymous,"Stop container (docker, 11abb7a227d7, DockerTestAPI2)"
        2015-05-19 08:05:16.720875,INFO,container,Anonymous,"Destroy container (docker, 11abb7a227d7, DockerTestAPI2)"
        2015-05-19 08:05:19.574727,INFO,image,Anonymous,"Start to download image from dockerhub (docker, lgsd/diamond:latest)"
        2015-05-19 08:05:20.946651,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-05-19 08:05:21.437004,INFO,export,Anonymous,"Start to export container (lxc, utest) to /test/c.tgz"
        2015-05-19 08:05:26.583202,INFO,export,Anonymous,Export task logs are cleared
        2015-05-19 08:05:30.354270,INFO,export,Anonymous,"Finished export container (lxc, utest) to /test/c.tgz"
        2015-05-19 08:05:30.360105,INFO,export,Anonymous,"Start to export container (docker, 1753ab55c36e, DockerTestAPI) to /test/d.tgz"
        2015-05-19 08:05:37.481961,INFO,image,Anonymous,"Finished to download image from dockerhub (docker, lgsd/diamond:latest)"
        2015-05-19 08:05:39.794424,INFO,export,Anonymous,"Finished export container (docker, 1753ab55c36e, DockerTestAPI) to /test/d.tgz"
        2015-05-19 08:05:40.050190,INFO,container,Anonymous,"Destroy container (lxc, utest_import)"
        2015-05-19 08:05:43.138930,INFO,import,Anonymous,"Start to import container (lxc, utest_import) from /test/c.tgz"
        2015-05-19 08:05:43.538430,INFO,import,Anonymous,Import task logs are cleared
        2015-05-19 08:05:44.279709,INFO,system,Anonymous,Create a new folder at /home/vagrant/container-station-web/test/new_folder
        2015-05-19 08:05:44.856886,INFO,container,TestUser1,Hello container station
        2015-05-19 08:05:44.863714,WARN,container,TestUser2,Hello container station
        2015-05-19 08:05:44.869210,ERROR,container,TestUser3,Hello container station
        
        
.. http:delete:: /api/v1/log

    Clear all system logs.

    :resjson int records: Returns the number of rows deleted.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE -b cookies.txt http://${QIP}:${QPORT}/api/v1/log

    **Example response**

    .. sourcecode:: text

        {"records": 58}
        
        
Event
------------------

.. http:get:: /api/v1/event

    :query index: start from. default returns the latest 20
    :query offset: the newest one

    **Response format**
    
    Category:User:Timestamp:JSON

    =========   =====  ==================================
    Category    User   JSON
    =========   =====  ==================================
    image       user   action: ``download``
                          - name: image name
                          - repository: ``dockerhub``, ``qnap``
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``delete``
                          - name: image name
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``update``
                          - category: ``local``
                          - type: ``docker``, ``lxc``
    container   user   - container: container name
                       - id: container ID
                       - type: ``docker``, ``lxc``
                       - state: ``create``, ``start``, ``stop``, ``restart``, ``destroy``, ``pause``, ``unpause``
                       - port: ``add``, ``remove``
    export      user   - type: ``docker``, ``lxc``
                       - container: container name
                       - cid: container ID
                       - path: export to
                       - compress: ``true``, ``false``
                       - state: ``running``, ``completed``, ``aborted``
                       - result: if not ``0``, means something wrong.
    import      user   - type: ``docker``, ``lxc``
                       - cid: container name
                       - path: import from
                       - state: ``running``, ``completed``, ``aborted``
                       - result: if not ``0``, means something wrong.
    =========   =====  ==================================


    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event

    **Example response**

    .. sourcecode:: json

        {
            "index": 61,
            "messages": [
                "import:Anonymous:1432022743:{\"tid\": 1, \"path\": \"/test/c.tgz\", \"state\": \"running\", \"type\": \"lxc\", \"cid\": \"utest_import\"}",
                "container:all:1432022740:{\"container\": \"utest_import\", \"state\": \"destroy\", \"type\": \"lxc\"}",
                "export:Anonymous:1432022739:{\"container\": \"DockerTestAPI\", \"cid\": \"1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "image:Anonymous:1432022737:{\"name\": \"lgsd/diamond\", \"repository\": \"dockerhub\", \"state\": \"success\", \"tag\": \"latest\", \"action\": \"download\", \"type\": \"docker\"}",
                "image:all:1432022737:{\"action\": \"update\", \"category\": \"local\", \"state\": \"pull\", \"type\": \"docker\", \"id\": \"lgsd/diamond:latest\"}",
                "export:Anonymous:1432022730:{\"container\": \"DockerTestAPI\", \"cid\": \"1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a\", \"compress\": true, \"state\": \"running\", \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:1432022730:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:1432022726:{\"container\": \"utest\", \"type\": \"lxc\", \"port\": \"add\"}",
                "container:all:1432022721:{\"container\": \"utest\", \"state\": \"start\", \"type\": \"lxc\"}",
                "export:Anonymous:1432022721:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"running\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:1432022721:{\"container\": \"utest\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:Anonymous:1432022719:{\"action\": \"delete\", \"state\": \"error\", \"type\": \"docker\", \"name\": \"lgsd/diamond\"}",
                "container:all:1432022716:{\"container\": \"DockerTestAPI2\", \"state\": \"destroy\", \"type\": \"docker\", \"id\": \"11abb7a227d7c6001e8bb5f6418f284845123e6dc56ef95309e6d3881d51f3a4\"}",
                "container:all:1432022716:{\"container\": \"DockerTestAPI2\", \"state\": \"die\", \"type\": \"docker\", \"id\": \"11abb7a227d7c6001e8bb5f6418f284845123e6dc56ef95309e6d3881d51f3a4\"}",
                "container:all:1432022716:{\"container\": \"utest\", \"state\": \"destroy\", \"type\": \"lxc\"}",
                "container:all:1432022716:{\"container\": \"utest\", \"state\": \"stop\", \"type\": \"lxc\"}",
                "container:all:1432022714:{\"container\": \"utest\", \"type\": \"lxc\", \"port\": \"add\"}",
                "container:all:1432022711:{\"container\": \"DockerTestAPI\", \"state\": \"die\", \"type\": \"docker\", \"id\": \"1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a\"}",
                "container:all:1432022711:{\"container\": \"DockerTestAPI\", \"state\": \"restart\", \"type\": \"docker\", \"id\": \"1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a\"}",
                "container:all:1432022711:{\"container\": \"DockerTestAPI\", \"state\": \"start\", \"type\": \"docker\", \"id\": \"1753ab55c36e99195042ddc875e59d4f877f1c140d25196ad34a5bece9f1cf3a\"}"
            ],
            "offset": 81
        }
        
        
.. http:get:: /api/v1/event/wait/(string:container_type)/(string:container_id)/(string:state)

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    :param state: ``running``, ``stopped``
    :query duration: timeout in seconds (default: 60)

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/stopped?duration=5"

    **Example response**

    .. sourcecode:: json

        {
            "cpu": 0.0,
            "id": "utest",
            "image": "ubuntu-trusty:latest",
            "ipaddress": [
                "10.0.3.47"
            ],
            "memory": 11751424,
            "name": "utest",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "lxc"
        }
        
        
