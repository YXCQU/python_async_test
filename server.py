import asyncio

from fastapi import FastAPI
import uvicorn as u

app = FastAPI()


@app.get("/api")
def web_api():
    asyncio.sleep(1.5)
    return {"msg": "python服务器数据"}


@app.get("/{name}")
def demo1(name: str):
    return {"Hello": name}


if __name__ == '__main__':
    # 模拟服务器程序
    u.run(app, host="0.0.0.0", port=5000)
