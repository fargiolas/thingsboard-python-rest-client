# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class OwnerControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def change_owner_to_customer_using_post(self, owner_id, entity_type, entity_id, **kwargs):  # noqa: E501
        """changeOwnerToCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_owner_to_customer_using_post(owner_id, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_id: ownerId (required)
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_owner_to_customer_using_post_with_http_info(owner_id, entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_owner_to_customer_using_post_with_http_info(owner_id, entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def change_owner_to_customer_using_post_with_http_info(self, owner_id, entity_type, entity_id, **kwargs):  # noqa: E501
        """changeOwnerToCustomer  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_owner_to_customer_using_post_with_http_info(owner_id, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_id: ownerId (required)
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_id', 'entity_type', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_owner_to_customer_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `change_owner_to_customer_using_post`")  # noqa: E501
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `change_owner_to_customer_using_post`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `change_owner_to_customer_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/owner/CUSTOMER/{ownerId}/{entityType}/{entityId}', 'POST',
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

    def change_owner_to_tenant_using_post(self, owner_id, entity_type, entity_id, **kwargs):  # noqa: E501
        """changeOwnerToTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_owner_to_tenant_using_post(owner_id, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_id: ownerId (required)
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.change_owner_to_tenant_using_post_with_http_info(owner_id, entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.change_owner_to_tenant_using_post_with_http_info(owner_id, entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def change_owner_to_tenant_using_post_with_http_info(self, owner_id, entity_type, entity_id, **kwargs):  # noqa: E501
        """changeOwnerToTenant  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_owner_to_tenant_using_post_with_http_info(owner_id, entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str owner_id: ownerId (required)
        :param str entity_type: entityType (required)
        :param str entity_id: entityId (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner_id', 'entity_type', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method change_owner_to_tenant_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner_id' is set
        if ('owner_id' not in params or
                params['owner_id'] is None):
            raise ValueError("Missing the required parameter `owner_id` when calling `change_owner_to_tenant_using_post`")  # noqa: E501
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `change_owner_to_tenant_using_post`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `change_owner_to_tenant_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'owner_id' in params:
            path_params['ownerId'] = params['owner_id']  # noqa: E501
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/owner/TENANT/{ownerId}/{entityType}/{entityId}', 'POST',
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
