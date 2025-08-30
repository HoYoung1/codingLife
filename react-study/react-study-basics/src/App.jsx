import { useState } from 'react'
import './App.css'
import HelloWorld from './components/HelloWorld'
import PropsExample from './components/PropsExample'
import ConditionalRender from './components/ConditionalRender'
import ListRender from './components/ListRender'

function App() {
  // 현재 보여줄 컴포넌트를 관리하는 상태
  const [currentComponent, setCurrentComponent] = useState('intro')

  // 컴포넌트 렌더링 함수
  const renderComponent = () => {
    switch (currentComponent) {
      case 'hello':
        return <HelloWorld />
      case 'props':
        return <PropsExample />
      case 'conditional':
        return <ConditionalRender />
      case 'list':
        return <ListRender />
      default:
        return (
          <div>
            <div className="study-info">
              <h2>학습 목표</h2>
              <ul>
                <li>React 기본 개념 (JSX, Props, State)</li>
                <li>Hook 사용법 (useState, useEffect)</li>
                <li>컴포넌트 패턴</li>
                <li>UI 라이브러리 (Ant Design, styled-components)</li>
                <li>API 통신 (axios, React Query)</li>
                <li>실무 프로젝트 구조</li>
              </ul>
            </div>

            <div className="project-structure">
              <h2>프로젝트 구조</h2>
              <pre>
                {`src/
├── components/  # 재사용 가능한 컴포넌트
├── pages/       # 페이지 컴포넌트
├── utils/       # 유틸리티 함수
├── App.jsx      # 메인 앱 컴포넌트
└── main.jsx     # 앱 진입점`}
              </pre>
            </div>
          </div>
        )
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 React 기초 스터디</h1>
        <p>백엔드 개발자를 위한 React 학습 프로젝트</p>
        
        {/* 네비게이션 버튼들 */}
        <nav className="study-nav">
          <button 
            onClick={() => setCurrentComponent('intro')}
            className={currentComponent === 'intro' ? 'active' : ''}
          >
            소개
          </button>
          <button 
            onClick={() => setCurrentComponent('hello')}
            className={currentComponent === 'hello' ? 'active' : ''}
          >
            JSX 기본
          </button>
          <button 
            onClick={() => setCurrentComponent('props')}
            className={currentComponent === 'props' ? 'active' : ''}
          >
            Props 사용법
          </button>
          <button 
            onClick={() => setCurrentComponent('conditional')}
            className={currentComponent === 'conditional' ? 'active' : ''}
          >
            조건부 렌더링
          </button>
          <button 
            onClick={() => setCurrentComponent('list')}
            className={currentComponent === 'list' ? 'active' : ''}
          >
            리스트 렌더링
          </button>
        </nav>
      </header>

      {/* 선택된 컴포넌트 렌더링 */}
      <main className="App-main">
        {renderComponent()}
      </main>
    </div>
  )
  
}

export default App
