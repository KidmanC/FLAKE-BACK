from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response


class errorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI)-> None:
        super().__init__(app)

    async def dispatch(self, request:Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return Response(content=f"Internal server error: {e}", status_code=500)