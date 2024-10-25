from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Book(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str
    description: str

from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int | None
    title: str
    author: str
    description: str

    class Config:
        orm_mode = True  # Enables ORM mode for compatibility with SQLModel
