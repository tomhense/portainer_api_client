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


class EndpointedgeEndpointEdgeStatusInspectResponse(object):
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
        'checkin': 'int',
        'credentials': 'str',
        'port': 'int',
        'schedules': 'list[EndpointedgeEdgeJobResponse]',
        'stacks': 'list[EndpointedgeStackStatusResponse]',
        'status': 'str'
    }

    attribute_map = {
        'checkin': 'checkin',
        'credentials': 'credentials',
        'port': 'port',
        'schedules': 'schedules',
        'stacks': 'stacks',
        'status': 'status'
    }

    def __init__(self, checkin=None, credentials=None, port=None, schedules=None, stacks=None, status=None, _configuration=None):  # noqa: E501
        """EndpointedgeEndpointEdgeStatusInspectResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._checkin = None
        self._credentials = None
        self._port = None
        self._schedules = None
        self._stacks = None
        self._status = None
        self.discriminator = None

        if checkin is not None:
            self.checkin = checkin
        if credentials is not None:
            self.credentials = credentials
        if port is not None:
            self.port = port
        if schedules is not None:
            self.schedules = schedules
        if stacks is not None:
            self.stacks = stacks
        if status is not None:
            self.status = status

    @property
    def checkin(self):
        """Gets the checkin of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501

        The current value of CheckinInterval  # noqa: E501

        :return: The checkin of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: int
        """
        return self._checkin

    @checkin.setter
    def checkin(self, checkin):
        """Sets the checkin of this EndpointedgeEndpointEdgeStatusInspectResponse.

        The current value of CheckinInterval  # noqa: E501

        :param checkin: The checkin of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: int
        """

        self._checkin = checkin

    @property
    def credentials(self):
        """Gets the credentials of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501


        :return: The credentials of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this EndpointedgeEndpointEdgeStatusInspectResponse.


        :param credentials: The credentials of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: str
        """

        self._credentials = credentials

    @property
    def port(self):
        """Gets the port of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501

        The tunnel port  # noqa: E501

        :return: The port of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this EndpointedgeEndpointEdgeStatusInspectResponse.

        The tunnel port  # noqa: E501

        :param port: The port of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def schedules(self):
        """Gets the schedules of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501

        List of requests for jobs to run on the environment(endpoint)  # noqa: E501

        :return: The schedules of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: list[EndpointedgeEdgeJobResponse]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this EndpointedgeEndpointEdgeStatusInspectResponse.

        List of requests for jobs to run on the environment(endpoint)  # noqa: E501

        :param schedules: The schedules of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: list[EndpointedgeEdgeJobResponse]
        """

        self._schedules = schedules

    @property
    def stacks(self):
        """Gets the stacks of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501

        List of stacks to be deployed on the environments(endpoints)  # noqa: E501

        :return: The stacks of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: list[EndpointedgeStackStatusResponse]
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        """Sets the stacks of this EndpointedgeEndpointEdgeStatusInspectResponse.

        List of stacks to be deployed on the environments(endpoints)  # noqa: E501

        :param stacks: The stacks of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: list[EndpointedgeStackStatusResponse]
        """

        self._stacks = stacks

    @property
    def status(self):
        """Gets the status of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501

        Status represents the environment(endpoint) status  # noqa: E501

        :return: The status of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EndpointedgeEndpointEdgeStatusInspectResponse.

        Status represents the environment(endpoint) status  # noqa: E501

        :param status: The status of this EndpointedgeEndpointEdgeStatusInspectResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(EndpointedgeEndpointEdgeStatusInspectResponse, dict):
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
        if not isinstance(other, EndpointedgeEndpointEdgeStatusInspectResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointedgeEndpointEdgeStatusInspectResponse):
            return True

        return self.to_dict() != other.to_dict()
