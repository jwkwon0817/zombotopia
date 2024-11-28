from fastapi import FastAPI
from zombotopia.core.database import Base, engine
from zombotopia.core.router import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix='/api/v1')
