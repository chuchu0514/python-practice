# # === Python 필수 .gitignore ===

# # Python 캐시 파일들
# __pycache__/
# *.pyc
# *.pyo
# *.pyd
# .Python

# # 가상환경
# venv/
# env/
# .venv/
# .env/

# # IDE 설정 파일들
# .vscode/
# .idea/
# *.swp
# *.swo
# *~

# # 운영체제 파일들
# .DS_Store       # macOS
# Thumbs.db      # Windows
# *.log

# # 프로젝트별 데이터 파일들 (선택적)
# file_storage/   # 일기장 프로젝트 데이터
# *.json          # JSON 데이터 파일들
# *.txt           # 텍스트 데이터 파일들

# # 민감한 정보 파일들
# .env            # 환경변수 (비밀번호, API 키 등)
# config.ini      # 설정 파일
# secrets.json    # 비밀 정보

# # 테스트 결과물들
# .coverage
# htmlcov/
# .pytest_cache/

# # 문서 빌드 결과물
# docs/_build/

# # === 추가 팁 ===
# # 특정 파일만 제외하고 폴더는 추가하고 싶다면:
# # logs/
# # !logs/.gitkeep

# # 파일 패턴 예시:
# # *.tmp          # 모든 .tmp 파일
# # test_*.py      # test_로 시작하는 파이썬 파일
# # **/temp/       # 모든 하위 폴더의 temp 폴더



# # === 커밋 컨벤션 완전 가이드 ===

# ## 기본 형식:
# <type>: <description>

# [optional body]
# [optional footer]

# ## 주요 타입들:

# ### 🚀 feat: 새로운 기능 추가
# feat: Add diary search by date range
# feat: Implement user authentication system
# feat: Add export to PDF feature

# ### 🐛 fix: 버그 수정  
# fix: Resolve crash when deleting last diary
# fix: Handle empty diary list display
# fix: Fix date validation for leap years

# ### 📚 docs: 문서 관련
# docs: Add installation guide to README
# docs: Update API documentation  
# docs: Add code comments for diary functions

# ### 🎨 style: 코드 포맷팅 (기능 변경 없음)
# style: Fix indentation in diary_list function
# style: Remove trailing whitespace
# style: Apply PEP8 formatting

# ### ♻️ refactor: 코드 리팩토링 (기능 변경 없음)
# refactor: Extract date validation to separate function
# refactor: Simplify diary loading logic
# refactor: Rename variables for better readability

# ### ⚡ perf: 성능 개선
# perf: Optimize diary search algorithm
# perf: Cache frequently accessed data
# perf: Reduce memory usage in large files

# ### ✅ test: 테스트 추가/수정
# test: Add unit tests for diary functions
# test: Fix failing integration tests
# test: Add edge case tests for date validation

# ### 🔧 chore: 빌드, 설정 관련
# chore: Update dependencies
# chore: Add .gitignore for Python projects
# chore: Configure development environment

# ## 실제 예시 (진성님 프로젝트 적용):

# # Phase 4 일기장 프로젝트
# feat: Add diary writing functionality
# feat: Implement diary list display  
# feat: Add diary deletion with confirmation
# fix: Resolve JSON file encoding issue
# style: Format code according to PEP8
# docs: Add README for diary project

# # Phase 5 알고리즘 프로젝트 (미래)
# feat: Implement bubble sort algorithm
# feat: Add binary search function  
# fix: Handle empty array in merge sort
# perf: Optimize quicksort performance
# test: Add comprehensive sorting tests

# ## 고급 팁:

# ### 1. 본문이 필요한 경우:
# feat: Add user authentication system

# - Implement login/logout functionality
# - Add password hashing with bcrypt
# - Create user session management
# - Add input validation for credentials

# ### 2. 이슈 번호 연결:
# fix: Resolve login timeout issue

# Fixes #123

# ### 3. Breaking Changes (중요한 변경):
# feat!: Change diary data structure

# BREAKING CHANGE: diary.json structure changed from array to object


# # 진성님이 아는 것
# git log --oneline

# # 🚀 프로들이 쓰는 고급 버전들
# git log --oneline --graph --all    # 브랜치 그래프로 시각화
# git log --since="2 weeks ago"      # 2주 전부터의 커밋들
# git log --author="진성"             # 특정 작성자의 커밋만
# git log --grep="feat"               # "feat"가 포함된 커밋만

# git log --oneline diary.py         # 특정 파일의 변경 이력
# git log -p diary.py                # 실제 코드 변경사항까지 보기
# git blame diary.py                 # 각 줄을 누가 언제 작성했는지
# git show HEAD~2                    # 2개 전 커밋의 상세 내용

# # ~/.gitconfig 파일에 추가하거나 명령어로 설정
# git config --global alias.lg "log --oneline --graph --all"
# git config --global alias.st "status"  
# git config --global alias.co "checkout"
# git config --global alias.br "branch"

# # 사용: git lg (git log --oneline --graph --all와 동일)

# # 커밋 메시지 수정 (진성님 이미 알고 있음)
# git commit --amend -m "새로운 메시지"

# # 파일 추가 깜빡했을 때
# git add 깜빡한파일.py
# git commit --amend --no-edit      # 메시지 수정 없이 파일만 추가

# # 커밋을 완전히 취소하고 싶을 때  
# git reset --soft HEAD~1           # 코드는 유지, 커밋만 취소
# git reset --hard HEAD~1           # ⚠️ 위험: 코드까지 모두 삭제

# # 특정 파일만 이전 상태로 되돌리기
# git checkout HEAD -- diary.py    # diary.py를 마지막 커밋 상태로