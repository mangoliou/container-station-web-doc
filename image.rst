Image
==================

Images would be from the depots, including

* local: images had been downloaded in local disk
* appcenter: images located in QNAP AppCenter, which needs to be downloaded before using
* dockerhub: images located in Docker Hub, which needs to be downloaded before using

.. http:get:: /api/v1/image/

    Get image list from specific depots.
    If depots is from dockerhub, it will take a few seconds to search.
    Filter installed image functio only effect for depots from appcenter.

    :param filter_text: (optional) filter image name and description or query string for docker search
    :param type: (optional) one of ``lxc``, ``docker``, *empty_string*
    :param from: (optional) one of ``local``, ``appcenter``, ``official``, ``dockerhub``. **Default: local**
    
    From local repository:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=local"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt
            "http://${QIP}:${QPORT}/api/v1/image/?from=local"
            | python -m json.tool


    From App Center:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=appcenter"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt
            "http://${QIP}:${QPORT}/api/v1/image/?from=appcenter"
            | python -m json.tool
    
    
    From Docker Official Repositories:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt "http://${QIP}:${QPORT}/api/v1/image/?from=official"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt
            "http://${QIP}:${QPORT}/api/v1/image/?from=official"
            | python -m json.tool


    From Docker Hub:

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
              "http://${QIP}:${QPORT}/api/v1/image/?from=dockerhub&filter_text=dorowu"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt
            "http://${QIP}:${QPORT}/api/v1/image/?from=dockerhub&filter_text=dorowu"
            | python -m json.tool


.. http:get:: /api/v1/image/(string:image_type)/(string:image_name)/(string:image_tag)/inspect

    Inspect image information.

    :param image_type: ``docker``
    :param image_name: image name
    :param image_name: image tag, which is ``latest`` or other version number

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/image/docker/ubuntu/latest/inspect"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt 
            "http://${QIP}:${QPORT}/api/v1/image/docker/ubuntu/latest/inspect" | python -m json.tool


.. http:get:: /api/v1/image/dockerhub/docker/(string:is_official)/(string:image_name)/tags

    Get image tags from Docker Hub. It will take a few seconds to finish.
    
    :param is_official: if image is official, it should be ``1``. Otherwise it should be ``0``.
    :param image_name: image name

    :resjson array installed: tags have been installed in local
    :resjson array tags: all tags of request image

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET -b cookies.txt \
            "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/1/redis/tags"

    **Example response**

    .. runcode:: json

        curl -sq -XGET -b cookies.txt 
            "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/1/redis/tags" | python -m json.tool


.. http:post:: /api/v1/image/(string:from)/(string:image_type)/(string:image_name)/(string:image_tag)/download

    Download the image from app center or docker hub

    :param from: ``dockerhub``, ``appcenter``
    :param image_type: ``lxc``, ``docker``
    :param image_name: image name
    :param image_tag: image tag, which is ``latest`` or other version number

    :reqjson string description: description of this image
    :reqjson string location: url of this image
    :reqjson string icon: icon source of this image

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XPOST -b cookies.txt -d \
            '{
                "description": "I am description.", 
                "location": "https://registry.hub.docker.com/u/lgsd/diamond/",
                "icon": "http://download.qnap.com/QPKG/images/QPKG/container_icon.png"
            }' "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/lgsd/diamond/latest/download"

    **Example response**

    .. runcode:: json

        curl -sq -XPOST -b cookies.txt 
            -d '{"description": "I am description.", "location": "https://registry.hub.docker.com/u/lgsd/diamond/",
                "icon": "http://download.qnap.com/QPKG/images/QPKG/container_icon.png" }'
            "http://${QIP}:${QPORT}/api/v1/image/dockerhub/docker/lgsd/diamond/latest/download" | python -m json.tool


.. http:get:: /api/v1/image/downloadstatus

    Get all downloading image status.

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XGET "http://${QIP}:${QPORT}/api/v1/image/downloadstatus"
 

    **Example response**

    .. runcode:: json

        curl -sq -XGET "http://${QIP}:${QPORT}/api/v1/image/downloadstatus" | python -m json.tool


.. http:delete:: /api/v1/image/(string:from)/(string:image_type)/(string:image_name)

    Remove image function which is only used in ``local`` image.
    This request will take few seconds to finish. 

    :param from: ``dockerhub``, ``appcenter``
    :param image_type: ``lxc``, ``docker``
    :param image_name: image name

    **Example request**

    .. sourcecode:: bash

        $ curl -sq -XDELETE "http://${QIP}:${QPORT}/api/v1/image/local/docker/lgsd/diamond"

    **Example response**

    .. runcode:: json

        curl -sq -XDELETE 
            "http://${QIP}:${QPORT}/api/v1/image/local/docker/lgsd/diamond" | python -m json.tool
