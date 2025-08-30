# Pages 폴더

이 폴더는 **페이지 컴포넌트**들을 저장하는 곳입니다.

## 페이지 vs 컴포넌트

- **Pages**: 라우팅으로 접근하는 전체 페이지 (예: Home, About, Users)
- **Components**: 페이지 내에서 사용되는 재사용 가능한 부품

## 폴더 구조 예시

```
pages/
├── Home.jsx            # 홈 페이지
├── About.jsx           # 소개 페이지
├── Users/              # 사용자 관련 페이지들
│   ├── UserList.jsx    # 사용자 목록
│   └── UserDetail.jsx  # 사용자 상세
└── NotFound.jsx        # 404 페이지
```

## 페이지 컴포넌트 작성 규칙

1. **라우팅**: React Router와 연결
2. **레이아웃**: 공통 레이아웃 적용
3. **데이터 페칭**: 페이지 레벨에서 데이터 로드
4. **SEO**: 페이지별 메타 정보 설정

## 학습 목표

- React Router를 사용한 SPA 라우팅
- 페이지 간 네비게이션
- URL 파라미터 처리
- 페이지별 상태 관리