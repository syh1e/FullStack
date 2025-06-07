# 스터디 앱

FLutter를 이용하여 개발한 스터디 앱입니다. 스터디장은 출석인증 코드를 생성하여 스터디원의 출결 현황을 확인할 수 있습니다.

## 기술 스택

### 클라이언트
- Flutter (크로스 플랫폼 프레임워크)
- Dart
- Provider (상태 관리)
- SQLite (로컬 데이터베이스)

### 서버
- Python 3.8+
- Flask (웹 프레임워크)
- SQLite (데이터베이스)
- Docker (컨테이너화)

## 시작하기

### 필수 요구사항
- Flutter SDK
- Python 3.8 이상
- Docker (선택사항)
- Git

### 설치 및 실행

1. 저장소 클론:
```bash
git clone [repository-url]
cd myapp
```
2. 클라이언트 설정:
```bash
cd client
flutter pub get
flutter run
```

3. 서버 설정:
```bash
cd server
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## 주요 기능

### 클라이언트
- 사용자 인증 (로그인/회원가입)
- 출결 현황 확인
- 스터디 생성
- 스터디 가입

### 서버
- RESTful API 제공
- 사용자 관리
- 출결 인증 관련
- 데이터베이스 관리

### 테스트
```bash
# 클라이언트 테스트
cd client
flutter test

# 서버 테스트
cd server
python -m pytest
```

## 배포

### 클라이언트 배포
- Web: 웹 서버

### 서버 배포
- Docker 컨테이너

## 문제 해결
- 클라이언트: `flutter doctor` 실행
- 서버: 로그 확인 및 데이터베이스 연결 상태 점검
- 공통: 의존성 문제는 `flutter clean` 또는 `pip cache clean`으로 해결

## 기여 방법
1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 연락처
- 이메일: [syh040113@khu.ac.kr]
- GitHub: [syh1e] 
