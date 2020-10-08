# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SubscriptionOperationsOperations(object):
    """SubscriptionOperationsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~microsoft.marketplace.saas.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_operations(
        self,
        subscription_id,  # type: str
        request_id_parameter=None,  # type: Optional[str]
        correlation_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.OperationList"]
        """List outstanding operations.

        Lists the outstanding operations for the current publisher.

        :param subscription_id:
        :type subscription_id: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationList, or the result of cls(response)
        :rtype: ~microsoft.marketplace.saas.models.OperationList or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.OperationList"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        # Construct URL
        url = self.list_operations.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('OperationList', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    list_operations.metadata = {'url': '/saas/subscriptions/{subscriptionId}/operations'}  # type: ignore

    def get_operation_status(
        self,
        subscription_id,  # type: str
        operation_id,  # type: str
        request_id_parameter=None,  # type: Optional[str]
        correlation_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["models.Operation"]
        """Get operation status.

        Enables the publisher to track the status of the specified triggered async operation (such as
        Subscribe, Unsubscribe, ChangePlan, or ChangeQuantity).

        :param subscription_id:
        :type subscription_id: str
        :param operation_id:
        :type operation_id: str
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Operation, or the result of cls(response)
        :rtype: ~microsoft.marketplace.saas.models.Operation or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["models.Operation"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        accept = "application/json"

        # Construct URL
        url = self.get_operation_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 403, 404, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Operation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_operation_status.metadata = {'url': '/saas/subscriptions/{subscriptionId}/operations/{operationId}'}  # type: ignore

    def update_operation_status(
        self,
        subscription_id,  # type: str
        operation_id,  # type: str
        body,  # type: "models.UpdateOperation"
        request_id_parameter=None,  # type: Optional[str]
        correlation_id=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the status of an operation.

        Update the status of an operation to indicate success or failure with the provided values.

        :param subscription_id:
        :type subscription_id: str
        :param operation_id:
        :type operation_id: str
        :param body:
        :type body: ~microsoft.marketplace.saas.models.UpdateOperation
        :param request_id_parameter: A unique string value for tracking the request from the client,
         preferably a GUID. If this value isn't provided, one will be generated and provided in the
         response headers.
        :type request_id_parameter: str
        :param correlation_id: A unique string value for operation on the client. This parameter
         correlates all events from client operation with events on the server side. If this value isn't
         provided, one will be generated and provided in the response headers.
        :type correlation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-08-31"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_operation_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if request_id_parameter is not None:
            header_parameters['x-ms-requestid'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
        if correlation_id is not None:
            header_parameters['x-ms-correlationid'] = self._serialize.header("correlation_id", correlation_id, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'UpdateOperation')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 400, 403, 404, 409, 500]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    update_operation_status.metadata = {'url': '/saas/subscriptions/{subscriptionId}/operations/{operationId}'}  # type: ignore
