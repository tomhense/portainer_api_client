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


class UsersUserUpdatePayload(object):
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
        'new_password': 'str',
        'password': 'str',
        'role': 'int',
        'theme': 'UsersThemePayload',
        'use_cache': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'new_password': 'newPassword',
        'password': 'password',
        'role': 'role',
        'theme': 'theme',
        'use_cache': 'useCache',
        'username': 'username'
    }

    def __init__(self, new_password=None, password=None, role=None, theme=None, use_cache=None, username=None, _configuration=None):  # noqa: E501
        """UsersUserUpdatePayload - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._new_password = None
        self._password = None
        self._role = None
        self._theme = None
        self._use_cache = None
        self._username = None
        self.discriminator = None

        self.new_password = new_password
        self.password = password
        self.role = role
        if theme is not None:
            self.theme = theme
        self.use_cache = use_cache
        self.username = username

    @property
    def new_password(self):
        """Gets the new_password of this UsersUserUpdatePayload.  # noqa: E501


        :return: The new_password of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this UsersUserUpdatePayload.


        :param new_password: The new_password of this UsersUserUpdatePayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

    @property
    def password(self):
        """Gets the password of this UsersUserUpdatePayload.  # noqa: E501


        :return: The password of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsersUserUpdatePayload.


        :param password: The password of this UsersUserUpdatePayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def role(self):
        """Gets the role of this UsersUserUpdatePayload.  # noqa: E501

        User role (1 for administrator account and 2 for regular account)  # noqa: E501

        :return: The role of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UsersUserUpdatePayload.

        User role (1 for administrator account and 2 for regular account)  # noqa: E501

        :param role: The role of this UsersUserUpdatePayload.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def theme(self):
        """Gets the theme of this UsersUserUpdatePayload.  # noqa: E501


        :return: The theme of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: UsersThemePayload
        """
        return self._theme

    @theme.setter
    def theme(self, theme):
        """Sets the theme of this UsersUserUpdatePayload.


        :param theme: The theme of this UsersUserUpdatePayload.  # noqa: E501
        :type: UsersThemePayload
        """

        self._theme = theme

    @property
    def use_cache(self):
        """Gets the use_cache of this UsersUserUpdatePayload.  # noqa: E501


        :return: The use_cache of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: bool
        """
        return self._use_cache

    @use_cache.setter
    def use_cache(self, use_cache):
        """Sets the use_cache of this UsersUserUpdatePayload.


        :param use_cache: The use_cache of this UsersUserUpdatePayload.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and use_cache is None:
            raise ValueError("Invalid value for `use_cache`, must not be `None`")  # noqa: E501

        self._use_cache = use_cache

    @property
    def username(self):
        """Gets the username of this UsersUserUpdatePayload.  # noqa: E501


        :return: The username of this UsersUserUpdatePayload.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsersUserUpdatePayload.


        :param username: The username of this UsersUserUpdatePayload.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(UsersUserUpdatePayload, dict):
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
        if not isinstance(other, UsersUserUpdatePayload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UsersUserUpdatePayload):
            return True

        return self.to_dict() != other.to_dict()
