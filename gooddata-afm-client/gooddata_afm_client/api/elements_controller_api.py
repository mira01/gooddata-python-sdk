"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gooddata_afm_client.api_client import ApiClient, Endpoint as _Endpoint
from gooddata_afm_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gooddata_afm_client.model.elements_response import ElementsResponse


class ElementsControllerApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __compute_label_elements(
            self,
            workspace_id,
            label,
            **kwargs
        ):
            """Listing of label values.  # noqa: E501

            Returns paged list of elements (values) of given label satisfying given filtering criteria.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.compute_label_elements(workspace_id, label, async_req=True)
            >>> result = thread.get()

            Args:
                workspace_id (str): Workspace identifier
                label (str): Requested label.

            Keyword Args:
                sort_order (str): Sort order of returned items. Items are sorted by ```label``` title.. [optional] if omitted the server will use the default value of "ASC"
                include_total_without_filters (bool): Specify if ```totalCountWithoutFilters``` should be returned.. [optional] if omitted the server will use the default value of False
                complement_filter (bool): Inverse filter: * ```false``` - return items matching ```patternFilter``` * ```true``` - return items not matching ```patternFilter```. [optional] if omitted the server will use the default value of False
                pattern_filter (str): Return only items, whose ```label``` title case insensitively contains ```filter``` as substring.. [optional]
                offset (int): Request page with this offset.. [optional] if omitted the server will use the default value of 0
                limit (int): Return only this number of items.. [optional] if omitted the server will use the default value of 1000
                data_sampling_percentage (float): Specifies the percentage of rows from fact datasets to use during computation. This feature is available only for workspaces that use a Vertica Data Source without table views.. [optional]
                skip_cache (bool): Ignore all caches during execution of current request.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ElementsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['workspace_id'] = \
                workspace_id
            kwargs['label'] = \
                label
            return self.call_with_http_info(**kwargs)

        self.compute_label_elements = _Endpoint(
            settings={
                'response_type': (ElementsResponse,),
                'auth': [],
                'endpoint_path': '/api/actions/workspaces/{workspaceId}/execution/collectLabelElements',
                'operation_id': 'compute_label_elements',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'workspace_id',
                    'label',
                    'sort_order',
                    'include_total_without_filters',
                    'complement_filter',
                    'pattern_filter',
                    'offset',
                    'limit',
                    'data_sampling_percentage',
                    'skip_cache',
                ],
                'required': [
                    'workspace_id',
                    'label',
                ],
                'nullable': [
                ],
                'enum': [
                    'sort_order',
                ],
                'validation': [
                    'workspace_id',
                    'data_sampling_percentage',
                ]
            },
            root_map={
                'validations': {
                    ('workspace_id',): {

                        'regex': {
                            'pattern': r'^[.A-Za-z0-9_-]{1,255}$',  # noqa: E501
                        },
                    },
                    ('data_sampling_percentage',): {

                        'exclusive_maximum': 100,
                        'exclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('sort_order',): {

                        "ASC": "ASC",
                        "DESC": "DESC"
                    },
                },
                'openapi_types': {
                    'workspace_id':
                        (str,),
                    'label':
                        (str,),
                    'sort_order':
                        (str,),
                    'include_total_without_filters':
                        (bool,),
                    'complement_filter':
                        (bool,),
                    'pattern_filter':
                        (str,),
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'data_sampling_percentage':
                        (float,),
                    'skip_cache':
                        (bool,),
                },
                'attribute_map': {
                    'workspace_id': 'workspaceId',
                    'label': 'label',
                    'sort_order': 'sortOrder',
                    'include_total_without_filters': 'includeTotalWithoutFilters',
                    'complement_filter': 'complementFilter',
                    'pattern_filter': 'patternFilter',
                    'offset': 'offset',
                    'limit': 'limit',
                    'data_sampling_percentage': 'dataSamplingPercentage',
                    'skip_cache': 'skip-cache',
                },
                'location_map': {
                    'workspace_id': 'path',
                    'label': 'query',
                    'sort_order': 'query',
                    'include_total_without_filters': 'query',
                    'complement_filter': 'query',
                    'pattern_filter': 'query',
                    'offset': 'query',
                    'limit': 'query',
                    'data_sampling_percentage': 'query',
                    'skip_cache': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__compute_label_elements
        )
