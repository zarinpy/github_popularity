from typing import Any

from fastapi import status
from fastapi.responses import JSONResponse
from starlette.background import BackgroundTask


__all__ = ["CustomResponse"]


class CustomResponse(JSONResponse):
    content: Any = None

    def __init__(
            self,
            content: Any = None,
            message: str = "success",
            details: Any = None,
            status_code: int = status.HTTP_200_OK,
            headers: dict = None,
            media_type: str = None,
            background: BackgroundTask = None,
    ) -> None:
        self.content = content
        self.message = message
        self.details = details
        super(CustomResponse, self).__init__(
            content, status_code, headers, media_type, background,
        )

    def clean(self):
        if not self.content:
            self.content = {}
        if not self.details:
            self.details = {}

        result = {
            "info": {
                "message": self.message,
                "details": self.details,
            },
            "data": self.content,
        }
        return result

    def render(self, content: Any) -> bytes:
        content = self.clean()
        return super(CustomResponse, self).render(content)
