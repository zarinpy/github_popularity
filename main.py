import uvicorn
from fastapi import FastAPI, HTTPException, Request

from api import api
from setting import setting
from utility.custom_renderer import CustomResponse

app = FastAPI(
    title="fast-API Github App",
    version="0.0.1",
    docs_url=setting.DOC_URL,
)


@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return CustomResponse(
        status_code=exc.status_code,
        message=exc.detail,
        content={},
    )


app.include_router(router=api, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host=setting.HOST, port=setting.GENERAL_URL_PORT)
