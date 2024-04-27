import time
from fastapi import FastAPI, Request
from routers import user
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(user.router)
#app.include_router(auth.router)
