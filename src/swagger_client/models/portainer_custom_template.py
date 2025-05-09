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


class PortainerCustomTemplate(object):
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
        'created_by_user_id': 'int',
        'description': 'str',
        'entry_point': 'str',
        'git_config': 'GittypesRepoConfig',
        'id': 'int',
        'logo': 'str',
        'note': 'str',
        'platform': 'int',
        'project_path': 'str',
        'resource_control': 'PortainerResourceControl',
        'title': 'str',
        'type': 'int',
        'edge_template': 'bool',
        'is_compose_format': 'bool',
        'variables': 'list[PortainerCustomTemplateVariableDefinition]'
    }

    attribute_map = {
        'created_by_user_id': 'CreatedByUserId',
        'description': 'Description',
        'entry_point': 'EntryPoint',
        'git_config': 'GitConfig',
        'id': 'Id',
        'logo': 'Logo',
        'note': 'Note',
        'platform': 'Platform',
        'project_path': 'ProjectPath',
        'resource_control': 'ResourceControl',
        'title': 'Title',
        'type': 'Type',
        'edge_template': 'edgeTemplate',
        'is_compose_format': 'isComposeFormat',
        'variables': 'variables'
    }

    def __init__(self, created_by_user_id=None, description=None, entry_point=None, git_config=None, id=None, logo=None, note=None, platform=None, project_path=None, resource_control=None, title=None, type=None, edge_template=None, is_compose_format=None, variables=None, _configuration=None):  # noqa: E501
        """PortainerCustomTemplate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by_user_id = None
        self._description = None
        self._entry_point = None
        self._git_config = None
        self._id = None
        self._logo = None
        self._note = None
        self._platform = None
        self._project_path = None
        self._resource_control = None
        self._title = None
        self._type = None
        self._edge_template = None
        self._is_compose_format = None
        self._variables = None
        self.discriminator = None

        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if description is not None:
            self.description = description
        if entry_point is not None:
            self.entry_point = entry_point
        if git_config is not None:
            self.git_config = git_config
        if id is not None:
            self.id = id
        if logo is not None:
            self.logo = logo
        if note is not None:
            self.note = note
        if platform is not None:
            self.platform = platform
        if project_path is not None:
            self.project_path = project_path
        if resource_control is not None:
            self.resource_control = resource_control
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if edge_template is not None:
            self.edge_template = edge_template
        if is_compose_format is not None:
            self.is_compose_format = is_compose_format
        if variables is not None:
            self.variables = variables

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this PortainerCustomTemplate.  # noqa: E501

        User identifier who created this template  # noqa: E501

        :return: The created_by_user_id of this PortainerCustomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this PortainerCustomTemplate.

        User identifier who created this template  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this PortainerCustomTemplate.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def description(self):
        """Gets the description of this PortainerCustomTemplate.  # noqa: E501

        Description of the template  # noqa: E501

        :return: The description of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PortainerCustomTemplate.

        Description of the template  # noqa: E501

        :param description: The description of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def entry_point(self):
        """Gets the entry_point of this PortainerCustomTemplate.  # noqa: E501

        Path to the Stack file  # noqa: E501

        :return: The entry_point of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this PortainerCustomTemplate.

        Path to the Stack file  # noqa: E501

        :param entry_point: The entry_point of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def git_config(self):
        """Gets the git_config of this PortainerCustomTemplate.  # noqa: E501


        :return: The git_config of this PortainerCustomTemplate.  # noqa: E501
        :rtype: GittypesRepoConfig
        """
        return self._git_config

    @git_config.setter
    def git_config(self, git_config):
        """Sets the git_config of this PortainerCustomTemplate.


        :param git_config: The git_config of this PortainerCustomTemplate.  # noqa: E501
        :type: GittypesRepoConfig
        """

        self._git_config = git_config

    @property
    def id(self):
        """Gets the id of this PortainerCustomTemplate.  # noqa: E501

        CustomTemplate Identifier  # noqa: E501

        :return: The id of this PortainerCustomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PortainerCustomTemplate.

        CustomTemplate Identifier  # noqa: E501

        :param id: The id of this PortainerCustomTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def logo(self):
        """Gets the logo of this PortainerCustomTemplate.  # noqa: E501

        URL of the template's logo  # noqa: E501

        :return: The logo of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this PortainerCustomTemplate.

        URL of the template's logo  # noqa: E501

        :param logo: The logo of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def note(self):
        """Gets the note of this PortainerCustomTemplate.  # noqa: E501

        A note that will be displayed in the UI. Supports HTML content  # noqa: E501

        :return: The note of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this PortainerCustomTemplate.

        A note that will be displayed in the UI. Supports HTML content  # noqa: E501

        :param note: The note of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def platform(self):
        """Gets the platform of this PortainerCustomTemplate.  # noqa: E501

        Platform associated to the template. Valid values are: 1 - 'linux', 2 - 'windows'  # noqa: E501

        :return: The platform of this PortainerCustomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PortainerCustomTemplate.

        Platform associated to the template. Valid values are: 1 - 'linux', 2 - 'windows'  # noqa: E501

        :param platform: The platform of this PortainerCustomTemplate.  # noqa: E501
        :type: int
        """

        self._platform = platform

    @property
    def project_path(self):
        """Gets the project_path of this PortainerCustomTemplate.  # noqa: E501

        Path on disk to the repository hosting the Stack file  # noqa: E501

        :return: The project_path of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._project_path

    @project_path.setter
    def project_path(self, project_path):
        """Sets the project_path of this PortainerCustomTemplate.

        Path on disk to the repository hosting the Stack file  # noqa: E501

        :param project_path: The project_path of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._project_path = project_path

    @property
    def resource_control(self):
        """Gets the resource_control of this PortainerCustomTemplate.  # noqa: E501


        :return: The resource_control of this PortainerCustomTemplate.  # noqa: E501
        :rtype: PortainerResourceControl
        """
        return self._resource_control

    @resource_control.setter
    def resource_control(self, resource_control):
        """Sets the resource_control of this PortainerCustomTemplate.


        :param resource_control: The resource_control of this PortainerCustomTemplate.  # noqa: E501
        :type: PortainerResourceControl
        """

        self._resource_control = resource_control

    @property
    def title(self):
        """Gets the title of this PortainerCustomTemplate.  # noqa: E501

        Title of the template  # noqa: E501

        :return: The title of this PortainerCustomTemplate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PortainerCustomTemplate.

        Title of the template  # noqa: E501

        :param title: The title of this PortainerCustomTemplate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this PortainerCustomTemplate.  # noqa: E501

        Type of created stack: * 1 - swarm * 2 - compose * 3 - kubernetes  # noqa: E501

        :return: The type of this PortainerCustomTemplate.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PortainerCustomTemplate.

        Type of created stack: * 1 - swarm * 2 - compose * 3 - kubernetes  # noqa: E501

        :param type: The type of this PortainerCustomTemplate.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def edge_template(self):
        """Gets the edge_template of this PortainerCustomTemplate.  # noqa: E501

        EdgeTemplate indicates if this template purpose for Edge Stack  # noqa: E501

        :return: The edge_template of this PortainerCustomTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._edge_template

    @edge_template.setter
    def edge_template(self, edge_template):
        """Sets the edge_template of this PortainerCustomTemplate.

        EdgeTemplate indicates if this template purpose for Edge Stack  # noqa: E501

        :param edge_template: The edge_template of this PortainerCustomTemplate.  # noqa: E501
        :type: bool
        """

        self._edge_template = edge_template

    @property
    def is_compose_format(self):
        """Gets the is_compose_format of this PortainerCustomTemplate.  # noqa: E501

        IsComposeFormat indicates if the Kubernetes template is created from a Docker Compose file  # noqa: E501

        :return: The is_compose_format of this PortainerCustomTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._is_compose_format

    @is_compose_format.setter
    def is_compose_format(self, is_compose_format):
        """Sets the is_compose_format of this PortainerCustomTemplate.

        IsComposeFormat indicates if the Kubernetes template is created from a Docker Compose file  # noqa: E501

        :param is_compose_format: The is_compose_format of this PortainerCustomTemplate.  # noqa: E501
        :type: bool
        """

        self._is_compose_format = is_compose_format

    @property
    def variables(self):
        """Gets the variables of this PortainerCustomTemplate.  # noqa: E501


        :return: The variables of this PortainerCustomTemplate.  # noqa: E501
        :rtype: list[PortainerCustomTemplateVariableDefinition]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this PortainerCustomTemplate.


        :param variables: The variables of this PortainerCustomTemplate.  # noqa: E501
        :type: list[PortainerCustomTemplateVariableDefinition]
        """

        self._variables = variables

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
        if issubclass(PortainerCustomTemplate, dict):
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
        if not isinstance(other, PortainerCustomTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortainerCustomTemplate):
            return True

        return self.to_dict() != other.to_dict()
