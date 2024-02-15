from notion_client import Client
import os
import dotenv
dotenv.load_dotenv()


# ノーションAPIキーを設定
notion_api_key = os.getenv("NOTION_API_KEY")
notion = Client(auth=notion_api_key)

# ページを追加するデータベースのID
database_id = os.getenv("test_db")

# データベースに新しいページを追加
new_page = notion.pages.create(
    **{
        "parent": {"database_id": database_id},
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": "ChatGPTとの会話"
                        }
                    }
                ]
            },
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "これはテストの記録です。"
                            }
                        }
                    ]
                }
            },
        ]
        # "children": {
        #     "rich_text": [
        #         {
        #             "text": {
        #                 "content": "# これはテストの記録です。"
        #             }
        #         }
        #     ]
        # }
    }
)

print("新しいページが追加されました:", new_page)
