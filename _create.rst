Draft for create container 
============================

New create container procedure:
  * pre-inspect image information
  * add create container task

Other function:
  * Get create task list
  * Delete all completed/aborted task
  * Container Clone




.. http:post:: /api/v1/image/create/(string:image_repository)/(string:image_type)

    .. autosimple:: api.container_create
    
    :param image_repository: ``local``, ``dockerhub``, ``appcenter``
    :param image_type: ``lxc``, ``docker``

    :reqjson string name: container name **[required]**
    :reqjson string image: image name **[required]**
    :reqjson string tag: image tag. For LXC is ``latest``  **[required]**
    :reqjson string type: ``lxc``, ``docker`` **[required]**

    Create an create container task if name is given. The JSON parameters are the same as :http:post:`/api/v1/container`.


**Example request of LXC**

    .. sourcecode:: bash

        $ curl -sq -XPOST -d \
            '{"type": "lxc", "name": "ctest", "image": "ubuntu-trusty", "tag": "latest"}' \
            http://${QIP}:${QPORT}/api/v1/image/create/appcenter/lxc

**Example response of LXC**

    .. sourcecode:: json

        {
            "create_params": {
                "image": "ubuntu-trusty",
                "name": "ctest",
                "tag": "latest",
                "type": "lxc"
            },
            "detail_state": "",
            "from": "appcenter",
            "id": 1,
            "image": "ubuntu-trusty",
            "init": 1426526921,
            "name": "ctest",
            "state": "waiting",
            "tag": "latest",
            "type": "lxc",
            "user": "Anonymous"
        }
        
        

        curl -sq -XPUT  http://${QIP}:${QPORT}/api/v1/container/lxc/ctest/stop -o /dev/null;
        curl -sq -XDELETE  http://${QIP}:${QPORT}/api/v1/container/lxc/ctest -o /dev/null;
        curl -sq -XPOST  -d
            '{"type": "lxc", "name": "ctest", "image": "ubuntu-trusty", "tag": "latest"}'
            http://${QIP}:${QPORT}/api/v1/image/create/appcenter/lxc
            | python -m json.tool;

**Example request of Docker**

    .. sourcecode:: bash
        
        $ curl -sq -XPOST  -d \
            '{"type": "docker", "name": "dtest", "image": "ubuntu", "tag": "latest"}' \
            http://${QIP}:${QPORT}/api/v1/image/create/dockerhub/docker

**Example response of Docker**

    .. sourcecode:: json

        {
            "create_params": {
                "image": "ubuntu",
                "name": "dtest",
                "tag": "latest",
                "type": "docker"
            },
            "detail_state": "",
            "from": "dockerhub",
            "id": 2,
            "image": "ubuntu",
            "init": 1426526922,
            "name": "dtest",
            "state": "waiting",
            "tag": "latest",
            "type": "docker",
            "user": "Anonymous"
        }
        
        

        id=`curl -sq -XGET  http://${QIP}:${QPORT}/api/v1/container/docker/getid/dtest`;
        echo $id | grep -q error || curl -sq -XPUT  http://${QIP}:${QPORT}/api/v1/container/docker/${id}/stop -o /dev/null;
        echo $id | grep -q error || curl -sq -XDELETE  http://${QIP}:${QPORT}/api/v1/container/docker/${id} -o /dev/null;
        curl -sq -XPOST  -d 
            '{"type": "docker", "name": "dtest", "image": "ubuntu", "tag": "latest"}'
            http://${QIP}:${QPORT}/api/v1/image/create/dockerhub/docker
            | python -m json.tool;


.. http:get:: /api/v1/image/create/

    Get create tasks list.

    :resjson int id: unique task id 
    :resjson int init: time of initial request
    :resjson int start: time of starting in epoch
    :resjson int end: time of completion in epoch
    :resjson int result: 0 means success
    :resjson string from: one of ``dockerhub``, ``appcenter``, ``local``
    :resjson string state: one of ``waiting``, ``running``, ``completed``, ``aborted``
    :resjson string detail_state: xx
    :resjson string type: container type
    :resjson string user: request user name
    :resjson string image: image name
    :resjson string tag: image tag
    :resjson string create_params: create parameters

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET  http://${QIP}:${QPORT}/api/v1/image/create/

    **Example response**

    .. sourcecode:: json

        [
            {
                "create_params": "{u'image': u'ubuntu', u'tag': u'latest', u'type': u'docker', u'name': u'dtest'}",
                "detail_state": "",
                "from": "dockerhub",
                "id": 2,
                "image": "ubuntu",
                "init": 1426526922,
                "name": "dtest",
                "state": "waiting",
                "tag": "latest",
                "type": "docker",
                "user": "Anonymous"
            },
            {
                "create_params": "{u'image': u'ubuntu-trusty', u'tag': u'latest', u'type': u'lxc', u'name': u'ctest'}",
                "detail_state": "creating",
                "from": "appcenter",
                "id": 1,
                "image": "ubuntu-trusty",
                "init": 1426526921,
                "name": "ctest",
                "start": 1426526921,
                "state": "running",
                "tag": "latest",
                "type": "lxc",
                "user": "Anonymous"
            }
        ]
        
        

        curl -sq -XGET  http://${QIP}:${QPORT}/api/v1/image/create/ | python -m json.tool

    
.. http:delete:: /api/v1/image/create/

    Clear completed/aborted tasks in database.

    :resjson array object: task ID which have been deleted.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE  http://${QIP}:${QPORT}/api/v1/image/create/

    **Example response**

    .. sourcecode:: json

        []
        
        

        curl -sq -XDELETE  http://${QIP}:${QPORT}/api/v1/image/create/ | python -m json.tool


