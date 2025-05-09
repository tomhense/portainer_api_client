# coding: utf-8

"""
    PortainerCE API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://documentation.portainer.io/api/api-examples/ You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API environments(endpoints) require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example:  ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API environment(endpoint) has an associated access policy, it is documented in the description of each environment(endpoint).  Different access policies are available:  - Public access - Authenticated access - Restricted access - Administrator access  ### Public access  No authentication is required to access the environments(endpoints) with this access policy.  ### Authenticated access  Authentication is required to access the environments(endpoints) with this access policy.  ### Restricted access  Authentication is required to access the environments(endpoints) with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the environments(endpoints) with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific environments(endpoints) to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API environment(endpoint) (which is not documented below due to Swagger limitations). This environment(endpoint) has a restricted access policy so you still need to be authenticated to be able to query this environment(endpoint). Any query on this environment(endpoint) will be proxied to the Docker API of the associated environment(endpoint) (requests and responses objects are the same as documented in the Docker API).  # Private Registry  Using private registry, you will need to pass a based64 encoded JSON string ‘{\"registryId\":\\<registryID value\\>}’ inside the Request Header. The parameter name is \"X-Registry-Auth\". \\<registryID value\\> - The registry ID where the repository was created.  Example:  ``` eyJyZWdpc3RyeUlkIjoxfQ== ```  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://documentation.portainer.io/api/api-examples/).   # noqa: E501

    OpenAPI spec version: 2.21.5
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EndpointGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def endpoint_group_add_endpoint(self, id, endpoint_id, **kwargs):  # noqa: E501
        """Add an environment(endpoint) to an environment(endpoint) group  # noqa: E501

        Add an environment(endpoint) to an environment(endpoint) group **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_add_endpoint(id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param int endpoint_id: Environment(Endpoint) identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_group_add_endpoint_with_http_info(id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_group_add_endpoint_with_http_info(id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def endpoint_group_add_endpoint_with_http_info(self, id, endpoint_id, **kwargs):  # noqa: E501
        """Add an environment(endpoint) to an environment(endpoint) group  # noqa: E501

        Add an environment(endpoint) to an environment(endpoint) group **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_add_endpoint_with_http_info(id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param int endpoint_id: Environment(Endpoint) identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_group_add_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `endpoint_group_add_endpoint`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if self.api_client.client_side_validation and ('endpoint_id' not in params or
                                                       params['endpoint_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint_id` when calling `endpoint_group_add_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpointId'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups/{id}/endpoints/{endpointId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_group_delete(self, id, **kwargs):  # noqa: E501
        """Remove an environment(endpoint) group  # noqa: E501

        Remove an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_group_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_group_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def endpoint_group_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Remove an environment(endpoint) group  # noqa: E501

        Remove an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `endpoint_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_group_delete_endpoint(self, id, endpoint_id, **kwargs):  # noqa: E501
        """Removes environment(endpoint) from an environment(endpoint) group  # noqa: E501

        **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_delete_endpoint(id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param int endpoint_id: Environment(Endpoint) identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_group_delete_endpoint_with_http_info(id, endpoint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_group_delete_endpoint_with_http_info(id, endpoint_id, **kwargs)  # noqa: E501
            return data

    def endpoint_group_delete_endpoint_with_http_info(self, id, endpoint_id, **kwargs):  # noqa: E501
        """Removes environment(endpoint) from an environment(endpoint) group  # noqa: E501

        **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_delete_endpoint_with_http_info(id, endpoint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param int endpoint_id: Environment(Endpoint) identifier (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'endpoint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_group_delete_endpoint" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `endpoint_group_delete_endpoint`")  # noqa: E501
        # verify the required parameter 'endpoint_id' is set
        if self.api_client.client_side_validation and ('endpoint_id' not in params or
                                                       params['endpoint_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `endpoint_id` when calling `endpoint_group_delete_endpoint`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'endpoint_id' in params:
            path_params['endpointId'] = params['endpoint_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups/{id}/endpoints/{endpointId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_group_list(self, **kwargs):  # noqa: E501
        """List Environment(Endpoint) groups  # noqa: E501

        List all environment(endpoint) groups based on the current user authorizations. Will return all environment(endpoint) groups if using an administrator account otherwise it will only return authorized environment(endpoint) groups. **Access policy**: restricted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PortainerEndpointGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_group_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_group_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def endpoint_group_list_with_http_info(self, **kwargs):  # noqa: E501
        """List Environment(Endpoint) groups  # noqa: E501

        List all environment(endpoint) groups based on the current user authorizations. Will return all environment(endpoint) groups if using an administrator account otherwise it will only return authorized environment(endpoint) groups. **Access policy**: restricted  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[PortainerEndpointGroup]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_group_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PortainerEndpointGroup]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_group_update(self, id, body, **kwargs):  # noqa: E501
        """Update an environment(endpoint) group  # noqa: E501

        Update an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_update(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param EndpointgroupsEndpointGroupUpdatePayload body: EndpointGroup details (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_group_update_with_http_info(id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_group_update_with_http_info(id, body, **kwargs)  # noqa: E501
            return data

    def endpoint_group_update_with_http_info(self, id, body, **kwargs):  # noqa: E501
        """Update an environment(endpoint) group  # noqa: E501

        Update an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_group_update_with_http_info(id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: EndpointGroup identifier (required)
        :param EndpointgroupsEndpointGroupUpdatePayload body: EndpointGroup details (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_group_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `endpoint_group_update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `endpoint_group_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortainerEndpointGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_groups_id_get(self, id, **kwargs):  # noqa: E501
        """Inspect an Environment(Endpoint) group  # noqa: E501

        Retrieve details abont an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_groups_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) group identifier (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_groups_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_groups_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def endpoint_groups_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Inspect an Environment(Endpoint) group  # noqa: E501

        Retrieve details abont an environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_groups_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Environment(Endpoint) group identifier (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_groups_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `endpoint_groups_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortainerEndpointGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def endpoint_groups_post(self, body, **kwargs):  # noqa: E501
        """Create an Environment(Endpoint) Group  # noqa: E501

        Create a new environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_groups_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndpointgroupsEndpointGroupCreatePayload body: Environment(Endpoint) Group details (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.endpoint_groups_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.endpoint_groups_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def endpoint_groups_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create an Environment(Endpoint) Group  # noqa: E501

        Create a new environment(endpoint) group. **Access policy**: administrator  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.endpoint_groups_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EndpointgroupsEndpointGroupCreatePayload body: Environment(Endpoint) Group details (required)
        :return: PortainerEndpointGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method endpoint_groups_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `endpoint_groups_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth', 'jwt']  # noqa: E501

        return self.api_client.call_api(
            '/endpoint_groups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortainerEndpointGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
