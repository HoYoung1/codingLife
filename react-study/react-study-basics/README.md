# 🚀 React 기초 스터디

백엔드 개발자를 위한 React 학습 프로젝트입니다.

## 📚 학습 목표

- React 기본 개념 (JSX, Props, State)
- Hook 사용법 (useState, useEffect)
- 컴포넌트 패턴 및 재사용성
- UI 라이브러리 (Ant Design, styled-components)
- API 통신 (axios, React Query)
- 실무 프로젝트 구조

## 🛠 기술 스택

- **빌드 도구**: Vite
- **패키지 매니저**: pnpm
- **프레임워크**: React (JavaScript)
- **UI 라이브러리**: Ant Design
- **스타일링**: styled-components
- **HTTP 클라이언트**: axios
- **서버 상태 관리**: TanStack Query (React Query)
- **라우팅**: React Router

## 📁 프로젝트 구조

```
src/
├── components/     # 재사용 가능한 컴포넌트
│   ├── hooks/      # Hook 실습 컴포넌트들
│   ├── patterns/   # 컴포넌트 패턴 학습
│   ├── ui/         # UI 라이브러리 활용
│   ├── api/        # API 통신 관련
│   └── query/      # React Query 관련
├── pages/          # 페이지 컴포넌트
├── utils/          # 유틸리티 함수
├── App.jsx         # 메인 앱 컴포넌트
└── main.jsx        # 앱 진입점
```

## 🚀 시작하기

### 1. 의존성 설치
```bash
pnpm install
```

### 2. 개발 서버 실행
```bash
pnpm run dev
```

### 3. 빌드
```bash
pnpm run build
```

## 📖 학습 단계

### 1단계: 환경 설정 ✅
- [x] Vite + React 프로젝트 생성
- [x] pnpm 패키지 매니저 설정
- [x] 기본 폴더 구조 생성

### 2단계: React 기본 개념
- [ ] JSX 문법 학습
- [ ] Props를 통한 데이터 전달
- [ ] 조건부 렌더링
- [ ] 리스트 렌더링

### 3단계: Hook 실습
- [ ] useState로 상태 관리
- [ ] useEffect로 사이드 이펙트 처리
- [ ] 커스텀 Hook 만들기

### 4단계: 컴포넌트 패턴
- [ ] 재사용 가능한 컴포넌트 설계
- [ ] 컴포넌트 합성 패턴
- [ ] Render Props 패턴

### 5단계: UI 라이브러리
- [ ] Ant Design 컴포넌트 활용
- [ ] styled-components 스타일링
- [ ] 테마 시스템 구축

### 6단계: API 통신
- [ ] axios를 사용한 HTTP 요청
- [ ] 로딩 상태 및 에러 처리
- [ ] React Query로 서버 상태 관리

### 7단계: 라우팅
- [ ] React Router 설정
- [ ] 페이지 네비게이션
- [ ] 동적 라우팅

### 8단계: 실무 구조
- [ ] 환경 변수 설정
- [ ] 코드 분할 및 최적화
- [ ] 테스트 작성

## 💡 학습 팁

1. **단계별 학습**: 각 단계를 완료한 후 다음 단계로 진행
2. **실습 중심**: 코드를 직접 작성하며 학습
3. **문서 참고**: 각 폴더의 README.md 파일 참고
4. **질문하기**: 이해되지 않는 부분은 언제든 질문

## 📝 참고 자료

- [React 공식 문서](https://react.dev/)
- [Vite 공식 문서](https://vitejs.dev/)
- [Ant Design 공식 문서](https://ant.design/)
- [styled-components 공식 문서](https://styled-components.com/)
- [TanStack Query 공식 문서](https://tanstack.com/query/latest)