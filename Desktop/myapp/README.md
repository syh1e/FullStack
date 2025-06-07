# Study App 프로젝트

## 프로젝트 개요
Study App은 학습 시간을 효율적으로 관리하고 추적할 수 있는 통합 솔루션입니다. Flutter 기반의 크로스 플랫폼 클라이언트와 Python Flask 기반의 서버로 구성되어 있습니다.

## 프로젝트 구조
```
myapp/
├── client/         # Flutter 클라이언트 애플리케이션
│   ├── lib/       # 소스 코드
│   ├── assets/    # 리소스 파일
│   └── ...
│
└── server/         # Python Flask 서버
    ├── models/    # 데이터베이스 모델
    ├── services/  # 비즈니스 로직
    └── ...
```

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
- 학습 세션 관리
- 학습 통계 및 분석
- 알림 설정
- 다크 모드 지원

### 서버
- RESTful API 제공
- 사용자 관리
- 학습 데이터 처리
- 통계 분석
- 데이터베이스 관리

## 개발 가이드

### 코드 스타일
- Flutter/Dart 공식 스타일 가이드 준수
- Python PEP 8 스타일 가이드 준수
- ESLint 및 Flutter Lint 사용

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
- Android: Google Play Store
- iOS: App Store
- Web: 웹 서버

### 서버 배포
- Docker 컨테이너
- 클라우드 서비스 (AWS, GCP, Azure 등)

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
- 이메일: [이메일 주소]
- GitHub: [GitHub 프로필] 