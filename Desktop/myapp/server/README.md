# Study App Server

## English

### Overview
This is the backend server for the Study App, built with Python Flask. The server provides RESTful APIs for user management, study session tracking, and data analytics.

### Project Structure
```
server/
├── models/         # Database models and schemas
├── repositories/   # Data access layer
├── services/       # Business logic layer
├── utils/          # Utility functions and helpers
├── app.py         # Main application entry point
├── schema.sql     # Database schema
└── Dockerfile     # Container configuration
```

### Prerequisites
- Python 3.8 or higher
- SQLite3
- Docker (optional)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd server
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
sqlite3 study_app.db < schema.sql
```

### Running the Server

#### Local Development
```bash
python app.py
```
The server will start on `http://localhost:5000`

#### Using Docker
```bash
docker build -t study-app-server .
docker run -p 5000:5000 study-app-server
```

### API Endpoints

#### User Management
- `POST /api/users/register` - Register new user
- `POST /api/users/login` - User login
- `GET /api/users/profile` - Get user profile

#### Study Sessions
- `POST /api/sessions` - Create study session
- `GET /api/sessions` - Get study sessions
- `PUT /api/sessions/<id>` - Update study session
- `DELETE /api/sessions/<id>` - Delete study session

### Testing
```bash
python -m pytest
```

---

## 한국어

### 개요
이 프로젝트는 Python Flask로 구축된 Study App의 백엔드 서버입니다. 사용자 관리, 학습 세션 추적, 데이터 분석을 위한 RESTful API를 제공합니다.

### 프로젝트 구조
```
server/
├── models/         # 데이터베이스 모델 및 스키마
├── repositories/   # 데이터 접근 계층
├── services/       # 비즈니스 로직 계층
├── utils/          # 유틸리티 함수 및 헬퍼
├── app.py         # 메인 애플리케이션 진입점
├── schema.sql     # 데이터베이스 스키마
└── Dockerfile     # 컨테이너 설정
```

### 필수 요구사항
- Python 3.8 이상
- SQLite3
- Docker (선택사항)

### 설치 방법

1. 저장소 클론:
```bash
git clone [repository-url]
cd server
```

2. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 의존성 설치:
```bash
pip install -r requirements.txt
```

4. 데이터베이스 초기화:
```bash
sqlite3 study_app.db < schema.sql
```

### 서버 실행

#### 로컬 개발 환경
```bash
python app.py
```
서버는 `http://localhost:5000`에서 실행됩니다.

#### Docker 사용
```bash
docker build -t study-app-server .
docker run -p 5000:5000 study-app-server
```

### API 엔드포인트

#### 사용자 관리
- `POST /api/users/register` - 새 사용자 등록
- `POST /api/users/login` - 사용자 로그인
- `GET /api/users/profile` - 사용자 프로필 조회

#### 학습 세션
- `POST /api/sessions` - 학습 세션 생성
- `GET /api/sessions` - 학습 세션 조회
- `PUT /api/sessions/<id>` - 학습 세션 수정
- `DELETE /api/sessions/<id>` - 학습 세션 삭제

### 테스트
```bash
python -m pytest
```
