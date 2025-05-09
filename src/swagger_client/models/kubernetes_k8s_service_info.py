# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the environments(endpoints) with this access policy.  ### Authenticated access  Authentication is required to access the environments(endpoints) with this access policy.  ### Restricted access  Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).  # Private Registry  Using private registry, you will need to pass a based64 encoded JSON string ‘{\"registryId\":\\<registryID value\\>}’ inside the Request Header. The parameter name is \"X-Registry-Auth\". \\<registryID value\\> - The registry ID where the repository was created.  Example:  ``` eyJyZWdpc3RyeUlkIjoxfQ== ```  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.21.5
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class KubernetesK8sServiceInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allocate_load_balancer_node_ports': 'bool',
        'annotations': 'dict(str, str)',
        'applications': 'list[KubernetesK8sApplication]',
        'cluster_ips': 'list[str]',
        'creation_timestamp': 'str',
        'external_ips': 'list[str]',
        'external_name': 'str',
        'ingress_status': 'list[KubernetesK8sServiceIngress]',
        'labels': 'dict(str, str)',
        'name': 'str',
        'namespace': 'str',
        'ports': 'list[KubernetesK8sServicePort]',
        'selector': 'dict(str, str)',
        'type': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'allocate_load_balancer_node_ports': 'allocateLoadBalancerNodePorts',
        'annotations': 'annotations',
        'applications': 'applications',
        'cluster_ips': 'clusterIPs',
        'creation_timestamp': 'creationTimestamp',
        'external_ips': 'externalIPs',
        'external_name': 'externalName',
        'ingress_status': 'ingressStatus',
        'labels': 'labels',
        'name': 'name',
        'namespace': 'namespace',
        'ports': 'ports',
        'selector': 'selector',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, allocate_load_balancer_node_ports=None, annotations=None, applications=None, cluster_ips=None, creation_timestamp=None, external_ips=None, external_name=None, ingress_status=None, labels=None, name=None, namespace=None, ports=None, selector=None, type=None, uid=None, _configuration=None):  # noqa: E501
        """KubernetesK8sServiceInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allocate_load_balancer_node_ports = None
        self._annotations = None
        self._applications = None
        self._cluster_ips = None
        self._creation_timestamp = None
        self._external_ips = None
        self._external_name = None
        self._ingress_status = None
        self._labels = None
        self._name = None
        self._namespace = None
        self._ports = None
        self._selector = None
        self._type = None
        self._uid = None
        self.discriminator = None

        if allocate_load_balancer_node_ports is not None:
            self.allocate_load_balancer_node_ports = allocate_load_balancer_node_ports
        if annotations is not None:
            self.annotations = annotations
        if applications is not None:
            self.applications = applications
        if cluster_ips is not None:
            self.cluster_ips = cluster_ips
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if external_ips is not None:
            self.external_ips = external_ips
        if external_name is not None:
            self.external_name = external_name
        if ingress_status is not None:
            self.ingress_status = ingress_status
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if ports is not None:
            self.ports = ports
        if selector is not None:
            self.selector = selector
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid

    @property
    def allocate_load_balancer_node_ports(self):
        """Gets the allocate_load_balancer_node_ports of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The allocate_load_balancer_node_ports of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._allocate_load_balancer_node_ports

    @allocate_load_balancer_node_ports.setter
    def allocate_load_balancer_node_ports(self, allocate_load_balancer_node_ports):
        """Sets the allocate_load_balancer_node_ports of this KubernetesK8sServiceInfo.


        :param allocate_load_balancer_node_ports: The allocate_load_balancer_node_ports of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: bool
        """

        self._allocate_load_balancer_node_ports = allocate_load_balancer_node_ports

    @property
    def annotations(self):
        """Gets the annotations of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The annotations of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this KubernetesK8sServiceInfo.


        :param annotations: The annotations of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._annotations = annotations

    @property
    def applications(self):
        """Gets the applications of this KubernetesK8sServiceInfo.  # noqa: E501

        serviceList screen  # noqa: E501

        :return: The applications of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: list[KubernetesK8sApplication]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this KubernetesK8sServiceInfo.

        serviceList screen  # noqa: E501

        :param applications: The applications of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: list[KubernetesK8sApplication]
        """

        self._applications = applications

    @property
    def cluster_ips(self):
        """Gets the cluster_ips of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The cluster_ips of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._cluster_ips

    @cluster_ips.setter
    def cluster_ips(self, cluster_ips):
        """Sets the cluster_ips of this KubernetesK8sServiceInfo.


        :param cluster_ips: The cluster_ips of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: list[str]
        """

        self._cluster_ips = cluster_ips

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The creation_timestamp of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this KubernetesK8sServiceInfo.


        :param creation_timestamp: The creation_timestamp of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._creation_timestamp = creation_timestamp

    @property
    def external_ips(self):
        """Gets the external_ips of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The external_ips of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_ips

    @external_ips.setter
    def external_ips(self, external_ips):
        """Sets the external_ips of this KubernetesK8sServiceInfo.


        :param external_ips: The external_ips of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: list[str]
        """

        self._external_ips = external_ips

    @property
    def external_name(self):
        """Gets the external_name of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The external_name of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        """Sets the external_name of this KubernetesK8sServiceInfo.


        :param external_name: The external_name of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._external_name = external_name

    @property
    def ingress_status(self):
        """Gets the ingress_status of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The ingress_status of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: list[KubernetesK8sServiceIngress]
        """
        return self._ingress_status

    @ingress_status.setter
    def ingress_status(self, ingress_status):
        """Sets the ingress_status of this KubernetesK8sServiceInfo.


        :param ingress_status: The ingress_status of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: list[KubernetesK8sServiceIngress]
        """

        self._ingress_status = ingress_status

    @property
    def labels(self):
        """Gets the labels of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The labels of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this KubernetesK8sServiceInfo.


        :param labels: The labels of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The name of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KubernetesK8sServiceInfo.


        :param name: The name of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The namespace of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this KubernetesK8sServiceInfo.


        :param namespace: The namespace of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def ports(self):
        """Gets the ports of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The ports of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: list[KubernetesK8sServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this KubernetesK8sServiceInfo.


        :param ports: The ports of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: list[KubernetesK8sServicePort]
        """

        self._ports = ports

    @property
    def selector(self):
        """Gets the selector of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The selector of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this KubernetesK8sServiceInfo.


        :param selector: The selector of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def type(self):
        """Gets the type of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The type of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KubernetesK8sServiceInfo.


        :param type: The type of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this KubernetesK8sServiceInfo.  # noqa: E501


        :return: The uid of this KubernetesK8sServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this KubernetesK8sServiceInfo.


        :param uid: The uid of this KubernetesK8sServiceInfo.  # noqa: E501
        :type: str
        """

        self._uid = uid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(KubernetesK8sServiceInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubernetesK8sServiceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubernetesK8sServiceInfo):
            return True

        return self.to_dict() != other.to_dict()
