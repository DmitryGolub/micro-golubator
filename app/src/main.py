from fastapi import FastAPI

from faststream.rabbit.fastapi import RabbitRouter

from src.config import settings


app = FastAPI()
rabbit_router = RabbitRouter(settings.RABBIT_URL)


@app.post("/order")
async def make_order(name: str):
    await rabbit_router.broker.publish(
        f"New order: {name}",
        queue="orders",
    )

    return {"data": "OK"}


app.include_router(rabbit_router)
