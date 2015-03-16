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

    .. runcode:: json

        (echo "import log.log as ctlog\nctlog.info('Hello container station', 'TestUser1', 'container')\nctlog.warn('Hello container station', 'TestUser2', 'container')\nctlog.error('Hello container station', 'TestUser3', 'container')" | sudo VIRTUAL_ENV=$VIRTUAL_ENV PATH=$PATH python -);
        http_proxy= curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/log?limit=5" | python -mjson.tool


.. http:get:: /api/v1/log/export

    Export logs to csv format.
    
    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/log/export

    **Example response**

    .. runcode:: text

        http_proxy= curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/log/export

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

    .. runcode:: json

        curl -sq -XGET -b cookies.txt http://${QIP}:${QPORT}/api/v1/event | python -mjson.tool


.. http:get:: /api/v1/event/wait/(string:container_type)/(string:container_id)/(string:state)

    :param container_type: ``lxc``, ``docker``
    :param container_id: container id
    :param state: ``running``, ``stopped``
    :query duration: timeout in seconds (default: 60)

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/stopped?duration=5"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"type": "lxc", "name": "utest", "image": "ubuntu-trusty", "tag": "latest"}' http://${QIP}:${QPORT}/api/v1/container  -o /dev/null; 
        curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/event/wait/lxc/utest/stopped?duration=5" | python -mjson.tool