import subprocess
from datetime import datetime, timedelta
from notion_client import Client
from github import Github
from datetime import datetime, timedelta
import re
import sys

# GitHub API 접근을 위한 개인 액세스 토큰
ACCESS_TOKEN = "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"

# 조회할 GitHub 저장소 정보
OWNER = "vmscloud"
REPO = "Aleatorik"

# Notion API 키 설정
NOTION_API_KEY = "secret_IZnicBvyEhRNsMS5zzPROQ6cXEO1hyKBn7TRGJ4xDNP"

# Notion 데이터베이스 URL 설정
# Notion 데이터베이스 URL 설정
NOTION_DATABASE_URL = "73241157846945c0ac690f53fd74fc50"

#"https://www.notion.so/vmssolutions/73241157846945c0ac690f53fd74fc50"

# Notion 클라이언트 초기화
client = Client(auth=NOTION_API_KEY)

# Notion 데이터베이스 가져오기
database = client.databases.retrieve(NOTION_DATABASE_URL)


url_pattern = r"https?://\S+"

def extract_urls_from_message(message):
    # 정규표현식 패턴을 사용하여 URL 추출    
    urls = re.findall(url_pattern, message)
    return urls

# 커밋 정보를 Notion 데이터베이스에 추가
def add_commit_to_notion(author, date, title, message,hash,link):
     
    properties = {
        "Title": {"title": [{"text": {"content": title}}]},        
        "Author": {"people": [{"id": author}]},  # 리스트로 변경
        "date": {"date": {"start": date.isoformat()}},
        "Hash": {"rich_text": [{"text": {"content": hash, "link": {"url": link}}}]}        
    }

    # URL과 메시지를 분리
    urls = extract_urls_from_message(message)
    if urls:
        url = urls[0]
        # URL을 링크 정보로 변환하여 rich_text 형태로 설정
        link_property = {"type": "url", "url": url}
        # URL을 제외한 메시지 생성
        new_message = message.replace(url, '').strip() + "\n"
        properties["Message"] = {"rich_text": [{"text": {"content": new_message}}, {"text": {"content": url, "link": link_property}}]}
    else:
        properties["Message"] = {"rich_text": [{"text": {"content": message}}]}   
    
    
    client.pages.create( parent = {"database_id": NOTION_DATABASE_URL},
                         properties=properties)
     
def get_commits_since(minutes_ago):
    # 현재 시간에서 minutes_ago 분 만큼을 빼서 반환
    return datetime.now() - timedelta(minutes=minutes_ago)

if __name__ == "__main__":
    # 명령줄에서 전달된 인자 확인
    if len(sys.argv) < 2:
        print("사용법: python main.py 시간(분)")
        sys.exit(1)

    try:
        minutes_ago = int(sys.argv[1])  # 첫 번째 인자를 정수로 변환
        days_ago = get_commits_since(minutes_ago)
        print(days_ago)  # minutes_ago 분 이전의 시간이 출력됨
    except ValueError:
        print("잘못된 입력입니다. 시간(분)은 정수로 입력하세요.")
        sys.exit(1)

# GitHub API에 연결
g = Github(ACCESS_TOKEN)

# 저장소 가져오기
repo = g.get_repo(f"{OWNER}/{REPO}") 

# 커밋 로그 가져오기
commits = repo.get_commits(since=days_ago)
 
# 특정 author들 지정 => 추후 사용자별 맵핑 작업 필요
target_authors = ["yuseohee", "prowonseok", "ddifa86"]

print("start commits upload!")
print("조회된 커밋 개수:", commits.totalCount)

# 각 커밋 정보 출력
for commit in commits:    
    author = commit.author.login
    date = commit.commit.author.date    
    hash = commit.sha[:7]
    link = commit.html_url

    #title = commit.commit.message

    lines = commit.commit.message.split('\n', 1)  # 첫 번째 줄만 분리
    title = lines[0]
    message = lines[1] if len(lines) > 1 else ""
    
    print("Author:", author)
    print("Date:", date)
    print("Title:", title)
    print("Contents:", message)
    print("Hash:", hash)
    print("Link:", link)
    print("---")
    # Notion 데이터베이스에 추가
    if( "prowonseok" in  author):
        author = "53663555-5d2e-4edf-9e71-1507426bf4b6"
    elif("yuseohee" in author):
        author = "205c1ceb-31b4-4b04-9b45-9f25ae8ea725"
    elif("ddifa86" in author):
        author = "14218a6a-52fd-42e3-9338-80ef1c1049e1"
    else:
        continue

   # add_commit_to_notion(author, date, title, message, hash,link)
   # break

print("end commits upload!")

