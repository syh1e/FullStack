# Study App 클라이언트

## 개요
이 프로젝트는 Flutter를 사용하여 개발된 Study App의 클라이언트 애플리케이션입니다. 사용자 친화적인 인터페이스를 통해 학습 세션을 관리하고 추적할 수 있습니다.

## 프로젝트 구조
```
client/
├── lib/           # 소스 코드
├── assets/        # 이미지, 폰트 등 리소스
├── test/          # 테스트 코드
├── android/       # 안드로이드 플랫폼 관련 파일
├── ios/          # iOS 플랫폼 관련 파일
├── web/          # 웹 플랫폼 관련 파일
└── pubspec.yaml   # 프로젝트 설정 및 의존성
```

## 필수 요구사항
- Flutter SDK (최신 버전)
- Dart SDK (최신 버전)
- Android Studio / VS Code
- Git

## 설치 방법

1. 저장소 클론:
```bash
git clone [repository-url]
cd client
```

2. 의존성 설치:
```bash
flutter pub get
```

3. 환경 설정:
```bash
flutter doctor
```

## 실행 방법

### 개발 모드
```bash
flutter run
```

### 릴리즈 빌드
```bash
flutter build apk     # 안드로이드
flutter build ios     # iOS
flutter build web     # 웹
```

## 주요 기능
- 사용자 인증 (로그인/회원가입)
- 학습 세션 관리
- 학습 통계 및 분석
- 알림 설정
- 다크 모드 지원

## 개발 가이드

### 코드 스타일
- Flutter 공식 스타일 가이드 준수
- Dart 분석 도구 사용
- 코드 포맷팅: `flutter format .`

### 테스트
```bash
flutter test
```

### 린트 검사
```bash
flutter analyze
```

## 배포

### 안드로이드
1. 키스토어 생성
2. `android/app/build.gradle` 설정
3. `flutter build appbundle` 또는 `flutter build apk`

### iOS
1. Xcode에서 인증서 설정
2. `flutter build ios`
3. App Store Connect에 업로드

## 문제 해결
- Flutter doctor로 환경 문제 확인
- pub cache clean으로 의존성 문제 해결
- flutter clean으로 빌드 문제 해결

## 기여 방법
1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.
