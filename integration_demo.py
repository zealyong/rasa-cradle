import json
import time
import asyncio

from rasa.core.agent import Agent
from flask import Flask, request, Response

app = Flask(__name__)

# rasa model agent
agent = Agent.load(model_path="model_zy/20221111-155928-moist-specular.tar.gz")


@app.route("/model/parse", methods=["POST"])
async def get_intent():
    """
    获取意图
    :return:
    """
    data = json.loads(request.data)
    ret = await agent.handle_text(data.get("text"))
    return Response(str(ret))


@app.route("/sleep", methods=["GET"])
def test_sleep():
    time.sleep(5)
    return Response("sleep 5 secs")


@app.route("/async_sleep", methods=["GET"])
async def test_async_sleep():
    await asyncio.sleep(5)
    return Response("sleep 5 secs")


if __name__ == '__main__':
    app.run()
