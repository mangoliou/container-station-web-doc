Compose application
===================

 - `Docker Compose full document <https://docs.docker.com/compose/>`_ 
 - `Docker Compose Github <https://github.com/docker/compose>`_ 
 - `Docker Compose roadmap <https://github.com/docker/compose/blob/master/ROADMAP.md>`_ 

.. http:get:: /api/v1/compose/

   List all compose application information. 

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/compose/"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt
            "http://${QIP}:${QPORT}/api/v1/compose/"
            | python -m json.tool


.. http:get:: /api/v1/compose/(string:application)/description

    Get application full description with markdown format.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/description"

    **Example response**

    .. runcode:: text

        curl -sq -XGET -b cookies.txt 
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/description"


.. http:get:: /api/v1/compose/(string:application)/define

    Get application full YAML definition.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/define"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt 
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/define" | python -m json.tool


.. http:post:: /api/v1/compose/(string:application)/pull

    Pulls images for containers.

    :param application: Application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/pull"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt 
            "http://${QIP}:${QPORT}/api/v1/compose/gitlab/pull" | python -m json.tool


.. http:post:: /api/v1/compose/up

    Create and start containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/up"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/up" | python -m json.tool


.. http:post:: /api/v1/compose/restart

    Restart running application.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/restart"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/restart" | python -m json.tool


.. http:post:: /api/v1/compose/kill

    Force stop application containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/kill"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/kill" | python -m json.tool


.. http:post:: /api/v1/compose/start

    Start existing application.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/start"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/start" | python -m json.tool


.. http:post:: /api/v1/compose/stop

    Stop running application without removing them.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/stop"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/stop" | python -m json.tool


.. http:post:: /api/v1/compose/rm

    Remove stopped application containers.

    :reqjson string application: Application name
    :reqjson string name: Custom application name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' \
            "http://${QIP}:${QPORT}/api/v1/compose/rm"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt -d '{"application": "gitlab", "name": "test"}' 
            "http://${QIP}:${QPORT}/api/v1/compose/rm" | python -m json.tool


