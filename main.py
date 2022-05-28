from fastapi import FastAPI, HTTPException, Request, status
from api import api
from setting import setting
import uvicorn


app = FastAPI(
    title="fast-API Github App",
    version="0.0.1",
    docs_url=setting.DOC_URL,
)

app.include_router(router=api, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host=setting.HOST, port=setting.GENERAL_URL_PORT)
