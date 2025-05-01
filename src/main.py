from typing import Union

from fastapi import FastAPI
from .controllers import hello_world_controller, cat_facts_controller

app = FastAPI()
app.include_router(hello_world_controller.router)
app.include_router(cat_facts_controller.router)