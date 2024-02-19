from fastapi.testclient import TestClient

from src.memo_notion.api.stub import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# 他のエンドポイントに対するテストも同様に追加します。
def test_register():
    response = client.post("/register")
    assert response.status_code == 200
    assert response.json() == {"message": "ユーザー登録が成功しました。"}


def test_login():
    response = client.post("/login")
    assert response.status_code == 200
    assert response.json() == {"token": "dummytoken"}


def test_create_memo():
    response = client.post("/create_memo")
    assert response.status_code == 200
    assert response.json() == {"message": "メモの作成に成功しました。"}
