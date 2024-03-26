# coding: utf-8
"""Waylay Broker api.

This code was generated from the OpenAPI documentation of 'Waylay Broker'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Literal,
    Optional,
    TypeVar,
    overload,
)

from pydantic import (
    Field,
    StrictBool,
    StrictStr,
    TypeAdapter,
)
from typing_extensions import (
    Annotated,  # >=3.9,
)
from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.data.models import (
        DeleteMessages200Response,
        ErrorResponse,
        MessageQuery,
        MessageQueryResult,
        TimestampedEvent,
    )
    from waylay.services.data.queries.messages_api import (
        DeleteMessagesQuery,
        GetLatestDocumentQuery,
        GetLatestMessagesQuery,
        QueryMessagesQuery,
    )


try:
    from waylay.services.data.models import (
        DeleteMessages200Response,
        ErrorResponse,
        MessageQuery,
        MessageQueryResult,
        TimestampedEvent,
    )
    from waylay.services.data.queries.messages_api import (
        DeleteMessagesQuery,
        GetLatestDocumentQuery,
        GetLatestMessagesQuery,
        QueryMessagesQuery,
    )

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        DeleteMessagesQuery = dict
        DeleteMessages200Response = Model

        GetLatestDocumentQuery = dict
        TimestampedEvent = Model

        ErrorResponse = Model

        GetLatestMessagesQuery = dict
        TimestampedEvent = Model

        MessageQuery = Model

        QueryMessagesQuery = dict
        MessageQueryResult = Model

        ErrorResponse = Model


T = TypeVar("T")


class MessagesApi(WithApiClient):
    """MessagesApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> DeleteMessages200Response: ...

    @overload
    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def delete_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: DeleteMessagesQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> DeleteMessages200Response | T | Response | Model:
        """Remove Messages For Resource.

        Removes all messages associated with a resource.
        :param resource_id: Uniquely identifies a resource. (required)
        :type resource_id: str
        :param query: URL Query parameters.
        :type query: DeleteMessagesQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "resourceId": str(resource_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(DeleteMessagesQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": DeleteMessages200Response if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="DELETE",
            resource_path="/data/v1/messages/{resourceId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TimestampedEvent: ...

    @overload
    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get_latest_document(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestDocumentQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> TimestampedEvent | T | Response | Model:
        """Retrieve Latest Message.

        Retrieves the latest (i.e. most recent) message for a resource.
        :param resource_id: Uniquely identifies a resource. (required)
        :type resource_id: str
        :param query: URL Query parameters.
        :type query: GetLatestDocumentQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "resourceId": str(resource_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(GetLatestDocumentQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": TimestampedEvent if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "404": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/data/v1/messages/{resourceId}/current",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> List[TimestampedEvent]: ...

    @overload
    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get_latest_messages(
        self,
        resource_id: Annotated[
            StrictStr, Field(description="Uniquely identifies a resource.")
        ],
        *,
        query: GetLatestMessagesQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> List[TimestampedEvent] | T | Response | Model:
        """Retrieve Messages For Resource.

        Retrieves the last n messages for a resource.
        :param resource_id: Uniquely identifies a resource. (required)
        :type resource_id: str
        :param query: URL Query parameters.
        :type query: GetLatestMessagesQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "resourceId": str(resource_id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(GetLatestMessagesQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": List[TimestampedEvent] if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/data/v1/messages/{resourceId}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> MessageQueryResult: ...

    @overload
    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def query_messages(
        self,
        *,
        json: MessageQuery | None = None,
        query: QueryMessagesQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> MessageQueryResult | T | Response | Model:
        """Query Messages.

        Executes an ad-hoc messages query.
        :param json: The json request body.
        :type json: MessageQuery, optional
        :param query: URL Query parameters.
        :type query: QueryMessagesQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}
        if json is not None and should_validate:
            body_adapter = TypeAdapter(Optional[MessageQuery])
            json = body_adapter.validate_python(json)  # type: ignore # https://github.com/pydantic/pydantic/discussions/7094
        body_args["json"] = json

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(QueryMessagesQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": MessageQueryResult if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {
            "400": ErrorResponse,
        }
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="POST",
            resource_path="/data/v1/messages/query",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
