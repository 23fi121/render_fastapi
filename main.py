from typing import Optional

from fastapi import FastAPI

from fastapi.responses import HTMLResponse #インポート


import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1 style="color: #ff0000">unityroomで遊ぼう！</h1>
            <a href="https://unityroom.com/games/piggy_bank_shooter" title="検索">サイトへ</a>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/present")
async def give_present(score):
    return {"response": f"中間考査お疲れさまでした。点数は {score}点です。"}  # f文字列というPythonの機能を使っている