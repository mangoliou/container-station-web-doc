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
    :query level: (optional) Log level like ``INFO``, ``WARN``, ``ERROR``.
    :query category: (optional) Function category like ``container``, ``image``, ``import``, ``export``, ``backup``, ``system``.
    :query text: (optional) Filter text

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/log?limit=5"

    **Example response**

    .. sourcecode:: json

        [
            {
                "category": "import",
                "id": 53,
                "level": "INFO",
                "message": "Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)",
                "ts": 1426526976,
                "user": "Anonymous"
            },
            {
                "category": "system",
                "id": 52,
                "level": "INFO",
                "message": "Create a new folder at /home/vagrant/container-station-web/test/new_folder",
                "ts": 1426526973,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 51,
                "level": "INFO",
                "message": "Import task logs are cleared",
                "ts": 1426526967,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 50,
                "level": "INFO",
                "message": "Start to import container (lxc, utest_import) from (/test/c.tgz)",
                "ts": 1426526966,
                "user": "Anonymous"
            },
            {
                "category": "container",
                "id": 49,
                "level": "INFO",
                "message": "Destroy container (lxc, utest_import)",
                "ts": 1426526963,
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
        2015-03-16 17:26:45.627297,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-16 17:26:45.912700,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-03-16 17:26:45.951865,INFO,backup,system,"Finished backup container (lxc, utest)"
        2015-03-16 17:26:46.167602,INFO,backup,system,"Start to restore container (lxc, utest)"
        2015-03-16 17:26:46.173896,ERROR,backup,system,"Backup error: [[Errno 2] No such file or directory: '/home/vagrant/container-station-web/ctstation/../test/image/docker/tmp3G9S2Y-import-docker/metadata'] (lxc, utest)"
        2015-03-16 17:26:46.177475,INFO,backup,system,"Finished restore container (lxc, utest)"
        2015-03-16 17:26:46.387085,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-03-16 17:26:46.393715,INFO,backup,system,"Finished backup container (lxc, utest)"
        2015-03-16 17:27:49.262017,INFO,image,Anonymous,"Start to download image from appcenter (lxc, ubuntu-trusty:latest)"
        2015-03-16 17:28:05.349159,INFO,image,Anonymous,"Finished to download image from appcenter (lxc, ubuntu-trusty:latest)"
        2015-03-16 17:28:11.674225,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-16 17:28:17.524110,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-16 17:28:17.752067,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-16 17:28:19.162231,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-16 17:28:19.565798,INFO,container,Anonymous,"Stop container (docker, ed00311d9b98, DockerTestAPI)"
        2015-03-16 17:28:21.893817,INFO,container,Anonymous,"Destroy container (docker, ed00311d9b98, DockerTestAPI)"
        2015-03-16 17:28:22.449384,INFO,container,Anonymous,"Create container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-16 17:28:24.531240,INFO,container,Anonymous,"Create container (docker, 978cf9969290, DockerTestAPI2)"
        2015-03-16 17:28:26.714467,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-16 17:28:27.337507,INFO,container,Anonymous,"Start container (lxc, utest)"
        2015-03-16 17:28:27.400314,INFO,container,Anonymous,"Stop container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-16 17:28:27.577804,INFO,container,Anonymous,"Start container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-16 17:28:33.445781,INFO,container,Anonymous,"Restart container (lxc, utest)"
        2015-03-16 17:28:33.666464,INFO,container,Anonymous,"Restart container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-16 17:28:39.013871,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-16 17:28:39.075171,INFO,container,Anonymous,"Stop container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-16 17:28:39.307321,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-16 17:28:39.415343,INFO,container,Anonymous,"Stop container (docker, 978cf9969290, DockerTestAPI2)"
        2015-03-16 17:28:39.972855,INFO,container,Anonymous,"Destroy container (docker, 978cf9969290, DockerTestAPI2)"
        2015-03-16 17:28:41.468491,INFO,container,Anonymous,"Destroy container (lxc, ctest)"
        2015-03-16 17:28:41.573641,INFO,container,Anonymous,"Start to create container (lxc, ctest)"
        2015-03-16 17:28:41.636683,INFO,container,Anonymous,"Stop container (docker, b6112ba86c28, dtest)"
        2015-03-16 17:28:42.684474,INFO,container,Anonymous,"Destroy container (docker, b6112ba86c28, dtest)"
        2015-03-16 17:28:42.878175,INFO,container,Anonymous,Create task logs are cleared
        2015-03-16 17:28:44.108306,INFO,container,Anonymous,"Create container (lxc, ctest)"
        2015-03-16 17:28:45.669890,INFO,container,Anonymous,"Finished create container (lxc, ctest) (return=0)"
        2015-03-16 17:28:45.673042,INFO,container,Anonymous,"Start to create container (docker, dtest)"
        2015-03-16 17:28:45.933893,INFO,container,Anonymous,"Create container (docker, f3ba3b9a079f, dtest)"
        2015-03-16 17:28:45.963925,INFO,container,Anonymous,"Finished create container (docker, dtest) (return=0)"
        2015-03-16 17:28:54.125871,INFO,image,Anonymous,"Start to download image from dockerhub (docker, lgsd/diamond:latest)"
        2015-03-16 17:28:54.132426,WARN,image,Anonymous,"Download: Image already exists (dockerhub, docker, lgsd/diamond:latest)"
        2015-03-16 17:28:56.489398,INFO,image,Anonymous,"Image removed (docker, lgsd/diamond)"
        2015-03-16 17:28:58.271156,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-16 17:28:58.726121,INFO,export,Anonymous,"Start to export container (lxc, utest) to (/test/c.tgz)"
        2015-03-16 17:29:01.005295,INFO,export,Anonymous,Export task logs are cleared
        2015-03-16 17:29:08.835915,INFO,export,Anonymous,"Finished export container (lxc, utest) to (/test/c.tgz) (return=0)"
        2015-03-16 17:29:08.841483,INFO,export,Anonymous,"Start to export container (docker, 397568fb6bde, DockerTestAPI) to (/test/d.tgz)"
        2015-03-16 17:29:22.977553,INFO,export,Anonymous,"Finished export container (docker, 397568fb6bde, DockerTestAPI) to (/test/d.tgz) (return=0)"
        2015-03-16 17:29:23.314150,INFO,container,Anonymous,"Destroy container (lxc, utest_import)"
        2015-03-16 17:29:26.417469,INFO,import,Anonymous,"Start to import container (lxc, utest_import) from (/test/c.tgz)"
        2015-03-16 17:29:27.115561,INFO,import,Anonymous,Import task logs are cleared
        2015-03-16 17:29:33.778059,INFO,system,Anonymous,Create a new folder at /home/vagrant/container-station-web/test/new_folder
        2015-03-16 17:29:36.899476,INFO,import,Anonymous,"Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)"
        
        
Event
------------------

.. http:get:: /api/v1/event

    :query index: start from. default returns the latest 20
    :query offset: the newest one

    **Response format**
    
    Category:User:JSON

    =========   =====  ==================================
    Category    User   JSON
    =========   =====  ==================================
    image       user   action: ``download``
                          - name: image name
                          - from: ``dockerhub``, ``appcenter``
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``delete``
                          - name: image name
                          - type: ``docker``, ``lxc``
                          - state: ``success``, ``error``
                       action: ``update``
                          - from: ``local``, ``appcenter``, ``official``
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
            "index": 59,
            "messages": [
                "import:Anonymous:{\"state\": \"completed\", \"result\": 0, \"cid\": \"utest_import\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"stop\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "import:Anonymous:{\"tid\": 1, \"path\": \"/test/c.tgz\", \"state\": \"running\", \"type\": \"lxc\", \"cid\": \"utest_import\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"destroy\", \"type\": \"lxc\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"397568fb6bde77cd7cb98930b5400497aeca1ce3e91ef1d51f475723e8b9f65c\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"397568fb6bde77cd7cb98930b5400497aeca1ce3e91ef1d51f475723e8b9f65c\", \"compress\": true, \"state\": \"running\", \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"type\": \"lxc\", \"port\": \"add\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"running\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"start\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "image:Anonymous:{\"action\": \"delete\", \"state\": \"success\", \"type\": \"docker\", \"name\": \"lgsd/diamond\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"091f251415982b8a4f6b2ad04e1f6284362ef34792175e50b53e59c56d3ce689\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"ffc94ca58a3b479dfb18e32b75ef605dfeb2d43aba243ff933edbc7018330865\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"delete\", \"from\": \"local\", \"id\": \"bfa7f7cadbffc9375bae0f57267f4c6939158574f791bb7e8a757e00c3ce9c32\"}"
            ],
            "offset": 79
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
                "10.0.3.201"
            ],
            "memory": 10846208,
            "name": "utest",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "lxc"
        }
        
        
