# Design Document

## Overview

React 기초 스터디 프로젝트는 백엔드 개발자가 React를 체계적으로 학습할 수 있도록 설계된 단계별 학습 환경입니다. 실무에서 사용하는 도구들과 패턴들을 활용하여 실제 프로젝트에 바로 적용할 수 있는 기초를 다집니다.

## Architecture

### 학습 단계별 구조

```
react-study-basics/
├── 01-environment-setup/     # 개발 환경 설정
├── 02-basic-concepts/        # React 기본 개념
├── 03-hooks-practice/        # Hook 실습
├── 04-component-patterns/    # 컴포넌트 패턴
├── 05-ui-libraries/          # UI 라이브러리 활용
├── 06-api-integration/       # API 통신 (axios 기본)
├── 07-server-state/          # 서버 상태 관리 (React Query)
└── 08-project-structure/     # 실무 프로젝트 구조
```

### 기술 스택

- **빌드 도구**: Vite (빠른 개발 서버, HMR 지원)
- **패키지 매니저**: pnpm (빠른 설치, 디스크 효율성)
- **UI 라이브러리**: Ant Design (풍부한 컴포넌트, 한국어 지원)
- **스타일링**: styled-components (CSS-in-JS, 동적 스타일링)
- **HTTP 클라이언트**: axios (Promise 기반, 인터셉터 지원)
- **서버 상태 관리**: TanStack Query (React Query) (캐싱, 동기화, 백그라운드 업데이트)
- **라우팅**: React Router (SPA 라우팅)

## Components and Interfaces

### 1. 학습 단계별 컴포넌트

#### 01-environment-setup
```javascript
// 기본 Vite + React 프로젝트 구조
src/
├── App.jsx
├── main.jsx
├── components/
├── pages/
└── utils/
```

#### 02-basic-concepts
```javascript
// 기본 개념 학습 컴포넌트들
components/
├── HelloWorld.jsx          # JSX 기본 문법
├── PropsExample.jsx        # Props 전달
├── ConditionalRender.jsx   # 조건부 렌더링
└── ListRender.jsx          # 리스트 렌더링
```

#### 03-hooks-practice
```javascript
// Hook 실습 컴포넌트들
components/hooks/
├── CounterExample.jsx      # useState 기본
├── FormExample.jsx         # useState + 폼 처리
├── ToggleExample.jsx       # useState + 불린 상태
├── EffectExample.jsx       # useEffect 기본
├── ApiExample.jsx          # useEffect + API 호출
└── TimerExample.jsx        # useEffect + 클린업
```

#### 04-component-patterns
```javascript
// 컴포넌트 패턴 학습
components/patterns/
├── Button/
│   ├── Button.jsx          # 재사용 가능한 버튼
│   └── Button.stories.jsx  # 사용 예제
├── Card/
│   ├── Card.jsx            # 카드 컴포넌트
│   └── Card.stories.jsx
└── Modal/
    ├── Modal.jsx           # 모달 컴포넌트
    └── Modal.stories.jsx
```

#### 05-ui-libraries
```javascript
// UI 라이브러리 활용
components/ui/
├── AntdBasics.jsx          # Ant Design 기본 컴포넌트
├── StyledComponents.jsx    # styled-components 활용
└── ThemeExample.jsx        # 테마 적용

#### 06-api-integration
```javascript
// 기본 axios 사용법
components/api/
├── BasicApiExample.jsx     # axios 기본 사용법
├── CrudExample.jsx         # CRUD 작업
└── ErrorHandling.jsx       # 에러 처리

#### 07-server-state
```javascript
// React Query 활용
components/query/
├── QueryBasics.jsx         # useQuery 기본
├── MutationExample.jsx     # useMutation 사용
├── CacheExample.jsx        # 캐싱 전략
└── OptimisticUpdate.jsx    # 낙관적 업데이트
```

### 2. 데이터 흐름 패턴

```javascript
// 상태 관리 패턴
const [state, setState] = useState(initialValue);

// Props 전달 패턴
<ChildComponent 
  data={parentData} 
  onAction={handleAction} 
/>

// 이벤트 처리 패턴
const handleClick = (event) => {
  // 이벤트 처리 로직
};
```

## Data Models

### 1. 학습 진행 상태 모델

```javascript
const StudyProgress = {
  currentStep: number,
  completedSteps: number[],
  totalSteps: number,
  startDate: Date,
  lastAccessDate: Date
};
```

### 2. 예제 데이터 모델

```javascript
// 사용자 데이터 (API 통신 예제용)
const User = {
  id: number,
  name: string,
  email: string,
  role: string
};

// 할일 데이터 (CRUD 예제용)
const Todo = {
  id: number,
  title: string,
  completed: boolean,
  createdAt: Date
};
```

### 3. 환경 설정 모델

```javascript
// 환경별 설정
const Config = {
  development: {
    API_BASE_URL: 'http://localhost:8000',
    DEBUG: true
  },
  production: {
    API_BASE_URL: 'https://api.example.com',
    DEBUG: false
  }
};
```

## Error Handling

### 1. React 에러 경계 (Error Boundary)

```javascript
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <h1>문제가 발생했습니다.</h1>;
    }
    return this.props.children;
  }
}
```

### 2. API 에러 처리

```javascript
// axios 인터셉터를 통한 전역 에러 처리
axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response?.status === 401) {
      // 인증 에러 처리
    }
    return Promise.reject(error);
  }
);

// 컴포넌트 레벨 에러 처리
const [error, setError] = useState(null);
const [loading, setLoading] = useState(false);

const fetchData = async () => {
  try {
    setLoading(true);
    setError(null);
    const response = await api.getData();
    setData(response.data);
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
};
```

### 3. 폼 유효성 검사

```javascript
// 간단한 폼 유효성 검사
const validateForm = (values) => {
  const errors = {};
  
  if (!values.email) {
    errors.email = '이메일을 입력해주세요';
  } else if (!/\S+@\S+\.\S+/.test(values.email)) {
    errors.email = '올바른 이메일 형식이 아닙니다';
  }
  
  return errors;
};
```

## Testing Strategy

### 1. 단위 테스트 (Jest + React Testing Library)

```javascript
// 컴포넌트 테스트 예제
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

test('카운터가 올바르게 증가한다', () => {
  render(<Counter />);
  const button = screen.getByText('증가');
  const count = screen.getByText('0');
  
  fireEvent.click(button);
  expect(screen.getByText('1')).toBeInTheDocument();
});
```

### 2. 통합 테스트

```javascript
// API 통신 테스트
import { render, screen, waitFor } from '@testing-library/react';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import UserList from './UserList';

const server = setupServer(
  rest.get('/api/users', (req, res, ctx) => {
    return res(ctx.json([
      { id: 1, name: '홍길동', email: 'hong@example.com' }
    ]));
  })
);

test('사용자 목록을 불러온다', async () => {
  render(<UserList />);
  
  await waitFor(() => {
    expect(screen.getByText('홍길동')).toBeInTheDocument();
  });
});
```

### 3. E2E 테스트 (Cypress)

```javascript
// 전체 플로우 테스트
describe('사용자 관리', () => {
  it('사용자를 추가하고 목록에서 확인할 수 있다', () => {
    cy.visit('/users');
    cy.get('[data-testid="add-user-button"]').click();
    cy.get('[data-testid="name-input"]').type('새 사용자');
    cy.get('[data-testid="email-input"]').type('new@example.com');
    cy.get('[data-testid="submit-button"]').click();
    cy.contains('새 사용자').should('be.visible');
  });
});
```

### 4. 학습 진행 검증

각 단계별로 다음과 같은 검증 포인트를 둡니다:

1. **환경 설정**: 프로젝트가 정상적으로 실행되는가?
2. **기본 개념**: JSX, Props, 조건부 렌더링이 작동하는가?
3. **Hook 실습**: useState, useEffect가 예상대로 동작하는가?
4. **컴포넌트 패턴**: 재사용 가능한 컴포넌트가 만들어졌는가?
5. **UI 라이브러리**: Ant Design, styled-components가 적용되었는가?
6. **API 통신**: axios를 통한 CRUD 작업이 가능한가?
7. **프로젝트 구조**: 실무에 적용 가능한 구조가 완성되었는가?

## 학습 경로 및 난이도 조절

### 초급 단계 (1-3주)
- 환경 설정 및 기본 개념
- useState, useEffect 기본 사용법
- 간단한 컴포넌트 작성

### 중급 단계 (4-6주)
- 컴포넌트 패턴 및 재사용성
- UI 라이브러리 활용
- 기본적인 상태 관리

### 고급 단계 (7-8주)
- API 통신 및 에러 처리
- 실무 프로젝트 구조
- 테스트 작성 기초

각 단계마다 실습 과제와 체크포인트를 두어 학습 진도를 확인할 수 있도록 합니다.