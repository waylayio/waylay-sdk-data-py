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
    Literal,
    TypeVar,
    overload,
)

from pydantic import (
    StrictBool,
    TypeAdapter,
)

from waylay.sdk.api import (
    HeaderTypes,
    QueryParamTypes,
    Response,
)
from waylay.sdk.api._models import Model
from waylay.sdk.plugin import WithApiClient

if TYPE_CHECKING:
    from waylay.services.data.models import VersionResponse
    from waylay.services.data.queries.about_api import GetQuery


try:
    from waylay.services.data.models import VersionResponse
    from waylay.services.data.queries.about_api import GetQuery

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        GetQuery = dict
        VersionResponse = Model


T = TypeVar("T")


class AboutApi(WithApiClient):
    """AboutApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> VersionResponse: ...

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get(
        self,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        validate_request: StrictBool = True,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> VersionResponse | T | Response | Model:
        """Get Service Status.

        Get the status and version of the service.
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param validate_request: If set to false, the request body and query parameters are NOT validated against the models in the service types package, even when available.
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

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and MODELS_AVAILABLE and validate_request:
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": VersionResponse if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/data/v1/",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_type=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )
