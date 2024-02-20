from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
async def register():
    # 本当のユーザー登録処理はここに実装されますが、
    # プロトタイピングではダミーデータを返すだけにします。
    return {"message": "ユーザー登録が成功しました。"}


@app.post("/login")
async def login():
    # OAuth認証後にトークンを返すことになりますが、
    # 今はダミーのトークンを返します。
    return {"token": "dummytoken"}


@app.post("/create_memo")
async def create_memo():
    # ここでメモを作成しますが、プロトタイピングでは
    # 作成成功のメッセージのみを返します。
    return {"message": "メモの作成に成功しました。"}
