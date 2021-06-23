# SPDX-FileCopyrightText: © 2021 Kyurenpoto <heal9179@gmail.com>

# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import Union

from pydantic import AnyHttpUrl, BaseModel
from pydantic.fields import Field
from submodules.fastapi_haljson.src.halmodel import HALBase


class LearnerEnvironment(BaseModel):
    url: AnyHttpUrl


class LearnerRepository(BaseModel):
    url: AnyHttpUrl


class LearnerInternal(BaseModel):
    env: LearnerEnvironment
    model: LearnerRepository
    report: LearnerRepository
    trajectory: LearnerRepository
    routes: dict[str, str]


class LearnerAPIInfo(BaseModel):
    name: str
    method: str


class LearnerModelInfo(BaseModel):
    url: AnyHttpUrl


class LearnerTrainRequest(BaseModel):
    model: LearnerModelInfo
    algorithm: str


class LearnerReportInfo(BaseModel):
    url: AnyHttpUrl


class LearnerTrainResponse(HALBase):
    report: LearnerReportInfo


class LearnerErrorResponse(HALBase):
    message: str = Field(
        ...,
        description="Error message",
    )
    location: str = Field(
        ...,
        description="Error location",
    )
    param: str = Field(
        ...,
        description="Parameters of request",
    )
    value: Union[
        tuple[list[str], int],
    ] = Field(
        ...,
        description="Values of request",
    )
    error: str = Field(
        ...,
        description="Error type",
    )
