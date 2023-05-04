"""Response model."""

from typing import Optional

from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Response(BaseModel):
    """Responde model using pydantic."""

    app: Optional[str]
    package_name: Optional[str]
    version: Optional[str]
    size: Optional[int]
    sha256: Optional[str]
