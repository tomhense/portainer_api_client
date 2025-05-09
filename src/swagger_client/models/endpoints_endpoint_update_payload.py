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


class EndpointsEndpointUpdatePayload(object):
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
        'azure_application_id': 'str',
        'azure_authentication_key': 'str',
        'azure_tenant_id': 'str',
        'edge_checkin_interval': 'int',
        'gpus': 'list[PortainerPair]',
        'group_id': 'int',
        'kubernetes': 'PortainerKubernetesData',
        'name': 'str',
        'public_url': 'str',
        'status': 'int',
        'tag_ids': 'list[int]',
        'team_access_policies': 'PortainerTeamAccessPolicies',
        'tls': 'bool',
        'tlsskip_client_verify': 'bool',
        'tlsskip_verify': 'bool',
        'url': 'str',
        'user_access_policies': 'PortainerUserAccessPolicies'
    }

    attribute_map = {
        'azure_application_id': 'azureApplicationID',
        'azure_authentication_key': 'azureAuthenticationKey',
        'azure_tenant_id': 'azureTenantID',
        'edge_checkin_interval': 'edgeCheckinInterval',
        'gpus': 'gpus',
        'group_id': 'groupID',
        'kubernetes': 'kubernetes',
        'name': 'name',
        'public_url': 'publicURL',
        'status': 'status',
        'tag_ids': 'tagIDs',
        'team_access_policies': 'teamAccessPolicies',
        'tls': 'tls',
        'tlsskip_client_verify': 'tlsskipClientVerify',
        'tlsskip_verify': 'tlsskipVerify',
        'url': 'url',
        'user_access_policies': 'userAccessPolicies'
    }

    def __init__(self, azure_application_id=None, azure_authentication_key=None, azure_tenant_id=None, edge_checkin_interval=None, gpus=None, group_id=None, kubernetes=None, name=None, public_url=None, status=None, tag_ids=None, team_access_policies=None, tls=None, tlsskip_client_verify=None, tlsskip_verify=None, url=None, user_access_policies=None, _configuration=None):  # noqa: E501
        """EndpointsEndpointUpdatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._azure_application_id = None
        self._azure_authentication_key = None
        self._azure_tenant_id = None
        self._edge_checkin_interval = None
        self._gpus = None
        self._group_id = None
        self._kubernetes = None
        self._name = None
        self._public_url = None
        self._status = None
        self._tag_ids = None
        self._team_access_policies = None
        self._tls = None
        self._tlsskip_client_verify = None
        self._tlsskip_verify = None
        self._url = None
        self._user_access_policies = None
        self.discriminator = None

        if azure_application_id is not None:
            self.azure_application_id = azure_application_id
        if azure_authentication_key is not None:
            self.azure_authentication_key = azure_authentication_key
        if azure_tenant_id is not None:
            self.azure_tenant_id = azure_tenant_id
        if edge_checkin_interval is not None:
            self.edge_checkin_interval = edge_checkin_interval
        if gpus is not None:
            self.gpus = gpus
        if group_id is not None:
            self.group_id = group_id
        if kubernetes is not None:
            self.kubernetes = kubernetes
        if name is not None:
            self.name = name
        if public_url is not None:
            self.public_url = public_url
        if status is not None:
            self.status = status
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if team_access_policies is not None:
            self.team_access_policies = team_access_policies
        if tls is not None:
            self.tls = tls
        if tlsskip_client_verify is not None:
            self.tlsskip_client_verify = tlsskip_client_verify
        if tlsskip_verify is not None:
            self.tlsskip_verify = tlsskip_verify
        if url is not None:
            self.url = url
        if user_access_policies is not None:
            self.user_access_policies = user_access_policies

    @property
    def azure_application_id(self):
        """Gets the azure_application_id of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Azure application ID  # noqa: E501

        :return: The azure_application_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._azure_application_id

    @azure_application_id.setter
    def azure_application_id(self, azure_application_id):
        """Sets the azure_application_id of this EndpointsEndpointUpdatePayload.

        Azure application ID  # noqa: E501

        :param azure_application_id: The azure_application_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._azure_application_id = azure_application_id

    @property
    def azure_authentication_key(self):
        """Gets the azure_authentication_key of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Azure authentication key  # noqa: E501

        :return: The azure_authentication_key of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._azure_authentication_key

    @azure_authentication_key.setter
    def azure_authentication_key(self, azure_authentication_key):
        """Sets the azure_authentication_key of this EndpointsEndpointUpdatePayload.

        Azure authentication key  # noqa: E501

        :param azure_authentication_key: The azure_authentication_key of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._azure_authentication_key = azure_authentication_key

    @property
    def azure_tenant_id(self):
        """Gets the azure_tenant_id of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Azure tenant ID  # noqa: E501

        :return: The azure_tenant_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._azure_tenant_id

    @azure_tenant_id.setter
    def azure_tenant_id(self, azure_tenant_id):
        """Sets the azure_tenant_id of this EndpointsEndpointUpdatePayload.

        Azure tenant ID  # noqa: E501

        :param azure_tenant_id: The azure_tenant_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._azure_tenant_id = azure_tenant_id

    @property
    def edge_checkin_interval(self):
        """Gets the edge_checkin_interval of this EndpointsEndpointUpdatePayload.  # noqa: E501

        The check in interval for edge agent (in seconds)  # noqa: E501

        :return: The edge_checkin_interval of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._edge_checkin_interval

    @edge_checkin_interval.setter
    def edge_checkin_interval(self, edge_checkin_interval):
        """Sets the edge_checkin_interval of this EndpointsEndpointUpdatePayload.

        The check in interval for edge agent (in seconds)  # noqa: E501

        :param edge_checkin_interval: The edge_checkin_interval of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: int
        """

        self._edge_checkin_interval = edge_checkin_interval

    @property
    def gpus(self):
        """Gets the gpus of this EndpointsEndpointUpdatePayload.  # noqa: E501

        GPUs information  # noqa: E501

        :return: The gpus of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: list[PortainerPair]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this EndpointsEndpointUpdatePayload.

        GPUs information  # noqa: E501

        :param gpus: The gpus of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: list[PortainerPair]
        """

        self._gpus = gpus

    @property
    def group_id(self):
        """Gets the group_id of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Group identifier  # noqa: E501

        :return: The group_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this EndpointsEndpointUpdatePayload.

        Group identifier  # noqa: E501

        :param group_id: The group_id of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def kubernetes(self):
        """Gets the kubernetes of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Associated Kubernetes data  # noqa: E501

        :return: The kubernetes of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: PortainerKubernetesData
        """
        return self._kubernetes

    @kubernetes.setter
    def kubernetes(self, kubernetes):
        """Sets the kubernetes of this EndpointsEndpointUpdatePayload.

        Associated Kubernetes data  # noqa: E501

        :param kubernetes: The kubernetes of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: PortainerKubernetesData
        """

        self._kubernetes = kubernetes

    @property
    def name(self):
        """Gets the name of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Name that will be used to identify this environment(endpoint)  # noqa: E501

        :return: The name of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EndpointsEndpointUpdatePayload.

        Name that will be used to identify this environment(endpoint)  # noqa: E501

        :param name: The name of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public_url(self):
        """Gets the public_url of this EndpointsEndpointUpdatePayload.  # noqa: E501

        URL or IP address where exposed containers will be reachable.\\ Defaults to URL if not specified  # noqa: E501

        :return: The public_url of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._public_url

    @public_url.setter
    def public_url(self, public_url):
        """Sets the public_url of this EndpointsEndpointUpdatePayload.

        URL or IP address where exposed containers will be reachable.\\ Defaults to URL if not specified  # noqa: E501

        :param public_url: The public_url of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._public_url = public_url

    @property
    def status(self):
        """Gets the status of this EndpointsEndpointUpdatePayload.  # noqa: E501

        The status of the environment(endpoint) (1 - up, 2 - down)  # noqa: E501

        :return: The status of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointsEndpointUpdatePayload.

        The status of the environment(endpoint) (1 - up, 2 - down)  # noqa: E501

        :param status: The status of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def tag_ids(self):
        """Gets the tag_ids of this EndpointsEndpointUpdatePayload.  # noqa: E501

        List of tag identifiers to which this environment(endpoint) is associated  # noqa: E501

        :return: The tag_ids of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this EndpointsEndpointUpdatePayload.

        List of tag identifiers to which this environment(endpoint) is associated  # noqa: E501

        :param tag_ids: The tag_ids of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: list[int]
        """

        self._tag_ids = tag_ids

    @property
    def team_access_policies(self):
        """Gets the team_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501


        :return: The team_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: PortainerTeamAccessPolicies
        """
        return self._team_access_policies

    @team_access_policies.setter
    def team_access_policies(self, team_access_policies):
        """Sets the team_access_policies of this EndpointsEndpointUpdatePayload.


        :param team_access_policies: The team_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: PortainerTeamAccessPolicies
        """

        self._team_access_policies = team_access_policies

    @property
    def tls(self):
        """Gets the tls of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Require TLS to connect against this environment(endpoint)  # noqa: E501

        :return: The tls of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._tls

    @tls.setter
    def tls(self, tls):
        """Sets the tls of this EndpointsEndpointUpdatePayload.

        Require TLS to connect against this environment(endpoint)  # noqa: E501

        :param tls: The tls of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: bool
        """

        self._tls = tls

    @property
    def tlsskip_client_verify(self):
        """Gets the tlsskip_client_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Skip client verification when using TLS  # noqa: E501

        :return: The tlsskip_client_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._tlsskip_client_verify

    @tlsskip_client_verify.setter
    def tlsskip_client_verify(self, tlsskip_client_verify):
        """Sets the tlsskip_client_verify of this EndpointsEndpointUpdatePayload.

        Skip client verification when using TLS  # noqa: E501

        :param tlsskip_client_verify: The tlsskip_client_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: bool
        """

        self._tlsskip_client_verify = tlsskip_client_verify

    @property
    def tlsskip_verify(self):
        """Gets the tlsskip_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501

        Skip server verification when using TLS  # noqa: E501

        :return: The tlsskip_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._tlsskip_verify

    @tlsskip_verify.setter
    def tlsskip_verify(self, tlsskip_verify):
        """Sets the tlsskip_verify of this EndpointsEndpointUpdatePayload.

        Skip server verification when using TLS  # noqa: E501

        :param tlsskip_verify: The tlsskip_verify of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: bool
        """

        self._tlsskip_verify = tlsskip_verify

    @property
    def url(self):
        """Gets the url of this EndpointsEndpointUpdatePayload.  # noqa: E501

        URL or IP address of a Docker host  # noqa: E501

        :return: The url of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EndpointsEndpointUpdatePayload.

        URL or IP address of a Docker host  # noqa: E501

        :param url: The url of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user_access_policies(self):
        """Gets the user_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501


        :return: The user_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :rtype: PortainerUserAccessPolicies
        """
        return self._user_access_policies

    @user_access_policies.setter
    def user_access_policies(self, user_access_policies):
        """Sets the user_access_policies of this EndpointsEndpointUpdatePayload.


        :param user_access_policies: The user_access_policies of this EndpointsEndpointUpdatePayload.  # noqa: E501
        :type: PortainerUserAccessPolicies
        """

        self._user_access_policies = user_access_policies

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
        if issubclass(EndpointsEndpointUpdatePayload, dict):
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
        if not isinstance(other, EndpointsEndpointUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointsEndpointUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
