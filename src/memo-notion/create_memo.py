from notion_client import Client

# ノーションAPIキーを設定
notion = Client(auth="あなたのノーションAPIキー")

# ページを追加するデータベースのID
database_id = "あなたのデータベースID"

# データベースに新しいページを追加
new_page = notion.pages.create(
    parent={"database_id": database_id},
    properties={
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "ChatGPTとの会話"
                    }
                }
            ]
        },
        "Description": {
            "rich_text": [
                {
                    "text": {
                        "content": "これはテストの記録です。"
                    }
                }
            ]
        }
    }
)
独自
print("新しいページが追加されました:", new_page)
