from github import Github
from datetime import datetime, timedelta

# GitHub API 접근을 위한 개인 액세스 토큰
ACCESS_TOKEN = "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"

# 조회할 GitHub 저장소 정보
OWNER = "vmscloud"
REPO = "Aleatorik"
BRANCH_NAME = "main"  # 원하는 브랜치 이름

# GitHub API에 연결
g = Github(ACCESS_TOKEN)

# 저장소 가져오기
repo = g.get_repo(f"{OWNER}/{REPO}")

# 브랜치 정보 가져오기
branch = repo.get_branch(BRANCH_NAME)

# 브랜치의 최근 커밋 시점 가져오기
since = branch.commit.commit.author.date

# 브랜치의 커밋 로그 가져오기
commits = repo.get_commits(since=since, sha=BRANCH_NAME)

# 각 커밋 정보 출력
for commit in commits:
    author = commit.author.name
    date = commit.commit.author.date
    full_message = commit.commit.message
    
    # 커밋 제목과 내용 분리
    lines = full_message.split('\n', 1)  # 첫 번째 줄만 분리
    title = lines[0]
    content = lines[1] if len(lines) > 1 else ""  # 첫 번째 줄을 제외한 나머지를 내용으로 설정
    
    hash = commit.sha[:7]
    link = commit.html_url
    
    print("Author:", author)
    print("Date:", date)
    print("Commit Title:", title)
    print("Commit Content:", content)
    print("Hash:", hash)
    print("Link:", link)
    print("---")
