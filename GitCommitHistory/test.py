from notion_client import Client

# Notion API 키 설정
NOTION_API_KEY = "secret_IZnicBvyEhRNsMS5zzPROQ6cXEO1hyKBn7TRGJ4xDNP"

# Notion 데이터베이스 URL 설정
NOTION_DATABASE_URL = "73241157846945c0ac690f53fd74fc50"

# Notion 클라이언트 초기화
client = Client(auth=NOTION_API_KEY)

# Notion 데이터베이스 가져오기
database = client.databases.retrieve(NOTION_DATABASE_URL)

# 데이터베이스의 제목 출력


# 데이터베이스의 레코드(행) 출력
print("데이터베이스 레코드:")
records = client.databases.query(database_id=NOTION_DATABASE_URL)["results"]
for record in records:
    properties = record["properties"]
    title = properties["Title"]["title"][0]["plain_text"]
    message = properties["Message"]["rich_text"][0]["plain_text"]
    author = properties["Author"]["people"][2]["id"]
    #date = properties["date"]["date"]["start"]
    print("제목:", title)
    print("메시지:", message)
    print("작성자:", author)
  
    print("---")
