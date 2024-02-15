import os
from pprint import pprint
import dotenv
dotenv.load_dotenv()
from notion_client import Client


# ノーションAPIキーを設定
notion_api_key = os.getenv("NOTION_API_KEY")
notion = Client(auth=notion_api_key)

# ページを追加するデータベースのID
database_id = os.getenv("NOTION_DATABASE_ID")

# データベース接続確認
# db = notion.databases.query(
#     **{
#         'database_id' : database_id  # データベースID
#        }
# )
# pprint(db)

# データベースに新しいページを追加

TEST_TXT = """
# test

## test2

aaea

"""

new_page = notion.pages.create(
    **{
        "parent": {"database_id": database_id},
        "properties": {
            "名前": {
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
                                "content": TEST_TXT
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
