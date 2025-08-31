# Implementation Plan

- [x] 1. 개발 환경 설정 및 기본 프로젝트 구조 생성
  - Vite + React + JavaScript 프로젝트 초기화
  - pnpm을 사용한 패키지 매니저 설정
  - src/components, src/pages, src/utils 폴더 구조 생성
  - 기본 App.jsx와 main.jsx 파일 작성
  - _Requirements: 1.1, 1.2, 1.3_

- [ ] 2. React 기본 개념 학습 컴포넌트 구현
- [x] 2.1 JSX와 Props 기본 컴포넌트 작성
  - HelloWorld.jsx 컴포넌트로 JSX 기본 문법 학습
  - PropsExample.jsx로 부모-자식 컴포넌트 데이터 전달 구현
  - _Requirements: 3.1, 3.2_

- [x] 2.2 조건부 렌더링과 리스트 렌더링 구현
  - ConditionalRender.jsx로 조건부 렌더링 패턴 구현
  - ListRender.jsx로 배열 데이터 렌더링 및 key props 학습
  - _Requirements: 3.3_

- [ ] 3. useState Hook 실습 컴포넌트 구현
- [x] 3.1 기본 상태 관리 컴포넌트 작성
  - CounterExample.jsx로 숫자 상태 증감 기능 구현
  - 상태 업데이트 함수와 리렌더링 동작 원리 주석으로 설명
  - _Requirements: 2.1_

- [x] 3.2 폼 상태 관리 컴포넌트 구현
  - FormExample.jsx로 입력 필드 상태 관리 구현
  - ToggleExample.jsx로 불린 상태 토글 기능 구현
  - 각 Hook의 동작 원리를 상세한 주석으로 설명
  - _Requirements: 2.1, 2.3_

- [ ] 4. useEffect Hook 실습 컴포넌트 구현
- [ ] 4.1 기본 사이드 이펙트 처리 구현
  - EffectExample.jsx로 컴포넌트 생명주기와 useEffect 관계 학습
  - dependency array의 동작 방식을 예제로 구현
  - _Requirements: 2.2, 2.3_

- [ ] 4.2 API 호출과 클린업 패턴 구현
  - ApiExample.jsx로 useEffect 내에서 API 호출 구현
  - TimerExample.jsx로 타이머 설정과 클린업 함수 구현
  - 메모리 누수 방지를 위한 클린업 패턴 설명
  - _Requirements: 2.2, 2.3_

- [ ] 5. 재사용 가능한 컴포넌트 패턴 구현
- [ ] 5.1 Button 컴포넌트 패턴 구현
  - components/patterns/Button/Button.jsx 재사용 가능한 버튼 컴포넌트 작성
  - 다양한 props(size, color, disabled 등)를 받아 동적으로 스타일링
  - Button.stories.jsx로 다양한 사용 예제 작성
  - _Requirements: 3.1, 3.3_

- [ ] 5.2 Card와 Modal 컴포넌트 패턴 구현
  - Card.jsx로 재사용 가능한 카드 레이아웃 컴포넌트 구현
  - Modal.jsx로 모달 컴포넌트와 Portal 패턴 구현
  - 각 컴포넌트의 stories 파일로 사용법 문서화
  - _Requirements: 3.1, 3.3_

- [ ] 6. Ant Design UI 라이브러리 통합
- [ ] 6.1 Ant Design 설치 및 기본 설정
  - antd 패키지 설치 및 CSS 임포트 설정
  - 한국어 locale 설정 구현
  - _Requirements: 4.1_

- [ ] 6.2 Ant Design 컴포넌트 활용 예제 구현
  - AntdBasics.jsx로 Button, Input, Card, Table 등 기본 컴포넌트 사용법 구현
  - Grid 시스템을 활용한 레이아웃 구성 예제 작성
  - _Requirements: 4.1, 4.3_

- [ ] 7. styled-components 스타일링 구현
- [ ] 7.1 styled-components 설치 및 기본 사용법 구현
  - styled-components 패키지 설치
  - StyledComponents.jsx로 기본 스타일링 패턴 구현
  - props를 활용한 동적 스타일링 예제 작성
  - _Requirements: 4.2_

- [ ] 7.2 테마 시스템 구현
  - ThemeProvider를 사용한 전역 테마 설정 구현
  - ThemeExample.jsx로 테마 기반 컴포넌트 스타일링 구현
  - 다크/라이트 모드 토글 기능 구현
  - _Requirements: 4.2_

- [ ] 8. axios를 사용한 기본 API 통신 구현
- [ ] 8.1 axios 설치 및 기본 HTTP 요청 구현
  - axios 패키지 설치 및 기본 설정
  - BasicApiExample.jsx로 GET, POST, PUT, DELETE 요청 구현
  - _Requirements: 5.1_

- [ ] 8.2 CRUD 작업과 에러 처리 구현
  - CrudExample.jsx로 사용자 데이터 CRUD 작업 구현
  - ErrorHandling.jsx로 로딩 상태, 에러 상태 처리 구현
  - FastAPI와의 통신을 위한 CORS 설정 예제 포함
  - _Requirements: 5.1, 5.2, 5.3_

- [ ] 9. React Query(TanStack Query) 서버 상태 관리 구현
- [ ] 9.1 React Query 설치 및 기본 설정
  - @tanstack/react-query 패키지 설치
  - QueryClient 설정 및 Provider 구성
  - _Requirements: 5.1_

- [ ] 9.2 useQuery 기본 사용법 구현
  - QueryBasics.jsx로 useQuery를 사용한 데이터 페칭 구현
  - 캐싱, 백그라운드 업데이트, 자동 재시도 기능 학습
  - axios와 useQuery를 함께 사용하는 패턴 구현
  - _Requirements: 5.1, 5.2_

- [ ] 9.3 useMutation과 고급 패턴 구현
  - MutationExample.jsx로 데이터 변경 작업 구현
  - CacheExample.jsx로 쿼리 캐시 무효화 및 업데이트 구현
  - OptimisticUpdate.jsx로 낙관적 업데이트 패턴 구현
  - _Requirements: 5.1, 5.2_

- [ ] 10. React Router를 사용한 라우팅 구현
- [ ] 10.1 React Router 설치 및 기본 라우팅 설정
  - react-router-dom 패키지 설치
  - BrowserRouter, Routes, Route 컴포넌트 설정
  - 기본 페이지 네비게이션 구현
  - _Requirements: 6.2_

- [ ] 10.2 페이지 컴포넌트와 네비게이션 구현
  - pages 폴더에 Home, About, Users 페이지 컴포넌트 작성
  - Link, NavLink를 사용한 네비게이션 메뉴 구현
  - 동적 라우팅과 URL 파라미터 처리 구현
  - _Requirements: 6.2, 6.3_

- [ ] 11. 환경 변수와 실무 프로젝트 구조 구현
- [ ] 11.1 환경 변수 설정 구현
  - .env, .env.dev, .env.prod 파일 생성
  - 환경별 API URL 및 설정값 관리 구현
  - Vite 환경 변수 사용법 구현
  - _Requirements: 6.1_

- [ ] 11.2 실무 프로젝트 구조 완성
  - utils 폴더에 공통 유틸리티 함수 작성
  - API 호출을 위한 서비스 레이어 구현
  - 상수 관리를 위한 constants 폴더 구성
  - pages, components, utils 폴더의 역할 명확화 및 문서화
  - _Requirements: 6.3_

- [ ] 12. 학습 진행 상태 추적 시스템 구현
- [ ] 12.1 학습 진행 상태 컴포넌트 구현
  - StudyProgress 컴포넌트로 현재 학습 단계 표시
  - localStorage를 사용한 학습 진행 상태 저장
  - 완료된 단계 체크리스트 UI 구현
  - _Requirements: 전체 요구사항 검증_

- [ ] 12.2 최종 통합 테스트 및 문서화
  - 모든 컴포넌트가 정상 작동하는지 통합 테스트
  - README.md 파일에 학습 가이드 및 실행 방법 문서화
  - 각 단계별 학습 목표와 체크포인트 정리
  - _Requirements: 전체 요구사항 검증_