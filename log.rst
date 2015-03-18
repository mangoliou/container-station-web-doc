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
                "id": 52,
                "level": "INFO",
                "message": "Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)",
                "ts": 1426613412,
                "user": "Anonymous"
            },
            {
                "category": "system",
                "id": 51,
                "level": "INFO",
                "message": "Create a new folder at /home/vagrant/container-station-web/test/new_folder",
                "ts": 1426613408,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 50,
                "level": "INFO",
                "message": "Import task logs are cleared",
                "ts": 1426613401,
                "user": "Anonymous"
            },
            {
                "category": "import",
                "id": 49,
                "level": "INFO",
                "message": "Start to import container (lxc, utest_import) from (/test/c.tgz)",
                "ts": 1426613400,
                "user": "Anonymous"
            },
            {
                "category": "export",
                "id": 48,
                "level": "INFO",
                "message": "Finished export container (docker, 08fd4fac14b8, DockerTestAPI) to (/test/d.tgz) (return=0)",
                "ts": 1426613397,
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
        2015-03-17 17:27:06.452144,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-17 17:27:06.895225,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-03-17 17:27:06.946738,INFO,backup,system,"User cancel of backup job (lxc, utest)"
        2015-03-17 17:27:07.309297,INFO,backup,system,"Start to restore container (lxc, utest)"
        2015-03-17 17:27:07.317374,ERROR,backup,system,"Backup error: [[Errno 2] No such file or directory: '/home/vagrant/container-station-web/ctstation/../test/image/docker/tmpdlwwO4-import-docker/metadata'] (lxc, utest)"
        2015-03-17 17:27:07.326575,INFO,backup,system,"Finished restore container (lxc, utest)"
        2015-03-17 17:27:07.713056,INFO,backup,system,"Start to backup container (lxc, utest)"
        2015-03-17 17:27:07.722057,INFO,backup,system,"Finished backup container (lxc, utest)"
        2015-03-17 17:28:10.948978,INFO,image,Anonymous,"Start to download image from appcenter (lxc, ubuntu-trusty:latest)"
        2015-03-17 17:28:29.978229,INFO,image,Anonymous,"Finished to download image from appcenter (lxc, ubuntu-trusty:latest)"
        2015-03-17 17:28:36.778244,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-17 17:28:42.770755,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-17 17:28:43.131795,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-17 17:28:45.080830,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-17 17:28:45.670936,INFO,container,Anonymous,"Stop container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-17 17:28:51.381775,INFO,container,Anonymous,"Destroy container (docker, 397568fb6bde, DockerTestAPI)"
        2015-03-17 17:28:52.085012,INFO,container,Anonymous,"Create container (docker, 08fd4fac14b8, DockerTestAPI)"
        2015-03-17 17:28:52.627520,INFO,container,Anonymous,"Create container (docker, 0298a0baef28, DockerTestAPI2)"
        2015-03-17 17:28:53.927315,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-17 17:28:54.565384,INFO,container,Anonymous,"Start container (lxc, utest)"
        2015-03-17 17:28:54.677423,INFO,container,Anonymous,"Stop container (docker, 08fd4fac14b8, DockerTestAPI)"
        2015-03-17 17:28:54.965939,INFO,container,Anonymous,"Start container (docker, 08fd4fac14b8, DockerTestAPI)"
        2015-03-17 17:29:00.982942,INFO,container,Anonymous,"Restart container (lxc, utest)"
        2015-03-17 17:29:01.476932,INFO,container,Anonymous,"Restart container (docker, 08fd4fac14b8, DockerTestAPI)"
        2015-03-17 17:29:07.041758,INFO,container,Anonymous,"Stop container (lxc, utest)"
        2015-03-17 17:29:07.148922,INFO,container,Anonymous,"Stop container (docker, 08fd4fac14b8, DockerTestAPI)"
        2015-03-17 17:29:07.559385,INFO,container,Anonymous,"Destroy container (lxc, utest)"
        2015-03-17 17:29:07.733255,INFO,container,Anonymous,"Stop container (docker, 0298a0baef28, DockerTestAPI2)"
        2015-03-17 17:29:08.518340,INFO,container,Anonymous,"Destroy container (docker, 0298a0baef28, DockerTestAPI2)"
        2015-03-17 17:29:10.006046,INFO,container,Anonymous,"Destroy container (lxc, ctest)"
        2015-03-17 17:29:10.120757,INFO,container,Anonymous,"Start to create container (lxc, ctest)"
        2015-03-17 17:29:10.223305,INFO,container,Anonymous,"Stop container (docker, f3ba3b9a079f, dtest)"
        2015-03-17 17:29:13.502721,INFO,container,Anonymous,"Create container (lxc, ctest)"
        2015-03-17 17:29:14.565402,INFO,container,Anonymous,"Destroy container (docker, f3ba3b9a079f, dtest)"
        2015-03-17 17:29:14.618659,INFO,container,Anonymous,"Finished create container (lxc, ctest) (return=0)"
        2015-03-17 17:29:14.724246,INFO,container,Anonymous,"Start to create container (docker, dtest)"
        2015-03-17 17:29:14.981256,INFO,container,Anonymous,Create task logs are cleared
        2015-03-17 17:29:15.137088,INFO,container,Anonymous,"Create container (docker, 07843f620541, dtest)"
        2015-03-17 17:29:15.303737,INFO,container,Anonymous,"Finished create container (docker, dtest) (return=0)"
        2015-03-17 17:29:25.639896,INFO,image,Anonymous,"Start to download image from dockerhub (docker, lgsd/diamond:latest)"
        2015-03-17 17:29:28.294731,INFO,container,Anonymous,"Create container (lxc, utest)"
        2015-03-17 17:29:28.944782,INFO,export,Anonymous,"Start to export container (lxc, utest) to (/test/c.tgz)"
        2015-03-17 17:29:32.366949,INFO,export,Anonymous,Export task logs are cleared
        2015-03-17 17:29:39.865558,INFO,export,Anonymous,"Finished export container (lxc, utest) to (/test/c.tgz) (return=0)"
        2015-03-17 17:29:39.880940,INFO,export,Anonymous,"Start to export container (docker, 08fd4fac14b8, DockerTestAPI) to (/test/d.tgz)"
        2015-03-17 17:29:43.462705,INFO,image,Anonymous,"Finished to download image from dockerhub (docker, lgsd/diamond:latest)"
        2015-03-17 17:29:57.059271,INFO,container,Anonymous,"Destroy container (lxc, utest_import)"
        2015-03-17 17:29:57.755285,INFO,export,Anonymous,"Finished export container (docker, 08fd4fac14b8, DockerTestAPI) to (/test/d.tgz) (return=0)"
        2015-03-17 17:30:00.154228,INFO,import,Anonymous,"Start to import container (lxc, utest_import) from (/test/c.tgz)"
        2015-03-17 17:30:01.081171,INFO,import,Anonymous,Import task logs are cleared
        2015-03-17 17:30:08.269564,INFO,system,Anonymous,Create a new folder at /home/vagrant/container-station-web/test/new_folder
        2015-03-17 17:30:12.508515,INFO,import,Anonymous,"Finished import container (lxc, utest_import) from (/test/c.tgz) (return=0)"
        
        
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
            "index": 56,
            "messages": [
                "import:Anonymous:{\"state\": \"completed\", \"result\": 0, \"cid\": \"utest_import\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"stop\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "import:Anonymous:{\"tid\": 1, \"path\": \"/test/c.tgz\", \"state\": \"running\", \"type\": \"lxc\", \"cid\": \"utest_import\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "container:all:{\"container\": \"utest_import\", \"state\": \"destroy\", \"type\": \"lxc\"}",
                "image:Anonymous:{\"from\": \"dockerhub\", \"name\": \"lgsd/diamond\", \"state\": \"success\", \"tag\": \"latest\", \"action\": \"download\", \"type\": \"docker\"}",
                "image:all:{\"action\": \"update\", \"type\": \"docker\", \"state\": \"pull\", \"from\": \"local\", \"id\": \"lgsd/diamond:latest\"}",
                "export:Anonymous:{\"container\": \"DockerTestAPI\", \"cid\": \"08fd4fac14b85af65da4a7d9c4f9d8feb5f3ef39f2ccd978c753151de9a42765\", \"compress\": true, \"state\": \"running\", \"tid\": 2, \"path\": \"/test/d.tgz\", \"type\": \"docker\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"completed\", \"result\": 0, \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"type\": \"lxc\", \"port\": \"add\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"start\", \"type\": \"lxc\"}",
                "export:Anonymous:{\"container\": \"utest\", \"cid\": \"utest\", \"compress\": true, \"state\": \"running\", \"tid\": 1, \"path\": \"/test/c.tgz\", \"type\": \"lxc\"}",
                "container:all:{\"container\": \"utest\", \"state\": \"create\", \"type\": \"lxc\"}",
                "image:all:{\"action\": \"update\", \"from\": \"local\", \"type\": \"lxc\"}",
                "image:Anonymous:{\"action\": \"delete\", \"state\": \"error\", \"type\": \"docker\", \"name\": \"lgsd/diamond\"}",
                "container:all:{\"container\": \"ctest\", \"type\": \"lxc\", \"port\": \"add\"}"
            ],
            "offset": 76
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
                "10.0.3.177"
            ],
            "memory": 10870784,
            "name": "utest",
            "rx": 0,
            "state": "running",
            "tx": 0,
            "type": "lxc"
        }
        
        
