# generated by datamodel-codegen:
#   filename:  openapi.yaml
#   timestamp: 2023-07-22T06:07:58+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class GetTodoResponse(BaseModel):
    todos: Optional[List[str]] = Field(None, description='The list of todos')


class PostTodoRequest(BaseModel):
    todo: Optional[str] = Field(None, description='The todo to add')


class PostTodoResponse(BaseModel):
    todos: Optional[List[str]] = Field(None, description='The list of todos')
