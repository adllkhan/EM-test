import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import Config
from api.v1 import router_products

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=list(Config().origins)
)

app.include_router(router=router_products, prefix="/api/v1")

if __name__ == "__main__":
    try:
        uvicorn.run(
            app="main:app",
            host=Config().host,
            port=Config().port,
            reload=Config().reload,
            reload_delay=0,
        )
    except KeyboardInterrupt:
        print("exiting...")
