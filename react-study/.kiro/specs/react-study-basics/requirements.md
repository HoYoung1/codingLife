# Requirements Document

## Introduction

백엔드 개발자를 위한 React 기초 스터디 프로젝트입니다. JavaScript 기반으로 React의 핵심 개념들을 단계별로 학습하고, 실제 회사 프로젝트에서 사용하는 도구들(Ant Design, styled-components, pnpm, Vite)을 활용하여 실무에 바로 적용할 수 있는 기초를 다집니다.

## Requirements

### Requirement 1

**User Story:** 백엔드 개발자로서, React의 기본 개념들을 체계적으로 학습하고 싶어서, 단계별 학습 환경을 구축하고 싶다.

#### Acceptance Criteria

1. WHEN 프로젝트를 시작할 때 THEN 시스템은 Vite + React + JavaScript 환경을 제공해야 한다
2. WHEN 개발 환경을 설정할 때 THEN 시스템은 pnpm을 패키지 매니저로 사용해야 한다
3. WHEN 프로젝트 구조를 생성할 때 THEN 시스템은 src/components, src/pages, src/utils 폴더 구조를 제공해야 한다

### Requirement 2

**User Story:** React 초보자로서, useState와 같은 핵심 Hook들을 실습하고 싶어서, 간단한 예제들을 통해 학습하고 싶다.

#### Acceptance Criteria

1. WHEN useState를 학습할 때 THEN 시스템은 카운터, 입력 폼, 토글 버튼 예제를 제공해야 한다
2. WHEN useEffect를 학습할 때 THEN 시스템은 API 호출, 타이머, 클린업 예제를 제공해야 한다
3. WHEN Hook을 사용할 때 THEN 시스템은 각 Hook의 동작 원리를 주석으로 설명해야 한다

### Requirement 3

**User Story:** 컴포넌트 기반 개발을 이해하고 싶어서, 재사용 가능한 컴포넌트들을 만들어보고 싶다.

#### Acceptance Criteria

1. WHEN 컴포넌트를 생성할 때 THEN 시스템은 props를 통한 데이터 전달 방식을 보여줘야 한다
2. WHEN 컴포넌트를 구성할 때 THEN 시스템은 부모-자식 컴포넌트 관계를 명확히 보여줘야 한다
3. WHEN 컴포넌트를 재사용할 때 THEN 시스템은 다양한 props로 같은 컴포넌트를 활용하는 예제를 제공해야 한다

### Requirement 4

**User Story:** 회사에서 사용하는 도구들에 익숙해지고 싶어서, Ant Design과 styled-components를 활용한 UI 개발을 학습하고 싶다.

#### Acceptance Criteria

1. WHEN UI를 개발할 때 THEN 시스템은 Ant Design 컴포넌트들(Button, Input, Card, Table 등)을 활용해야 한다
2. WHEN 스타일링을 할 때 THEN 시스템은 styled-components를 사용한 커스텀 스타일링을 보여줘야 한다
3. WHEN 레이아웃을 구성할 때 THEN 시스템은 Ant Design의 Grid 시스템을 활용해야 한다

### Requirement 5

**User Story:** 백엔드와의 통신을 이해하고 싶어서, axios를 사용한 HTTP 통신을 실습하고 싶다.

#### Acceptance Criteria

1. WHEN API를 호출할 때 THEN 시스템은 axios를 사용한 GET, POST, PUT, DELETE 요청을 보여줘야 한다
2. WHEN 데이터를 받아올 때 THEN 시스템은 로딩 상태와 에러 처리를 포함해야 한다
3. WHEN FastAPI와 통신할 때 THEN 시스템은 CORS 설정과 JSON 데이터 처리를 보여줘야 한다

### Requirement 6

**User Story:** 실무에서 사용하는 프로젝트 구조를 이해하고 싶어서, 환경 변수와 라우팅을 포함한 실제적인 프로젝트 구조를 학습하고 싶다.

#### Acceptance Criteria

1. WHEN 환경 설정을 할 때 THEN 시스템은 .env, .env.dev, .env.prod 파일을 활용해야 한다
2. WHEN 라우팅을 구현할 때 THEN 시스템은 React Router를 사용한 페이지 네비게이션을 제공해야 한다
3. WHEN 프로젝트를 구성할 때 THEN 시스템은 pages, components, utils 폴더의 역할을 명확히 구분해야 한다