import json

from flask import Flask, request, Response
from rasa.core.agent import Agent

app = Flask(__name__)

# rasa model agent
agent = Agent.load(model_path="zy_test/20221111-110129-rosy-commander.tar.gz")


@app.route("/model/parse", methods=["POST"])
async def get_intent():
    """
    获取意图
    :return:
    """
    data = json.loads(request.data)
    ret = await agent.handle_text(data.get("text"))
    return Response(str(ret))


if __name__ == '__main__':
    app.run()
