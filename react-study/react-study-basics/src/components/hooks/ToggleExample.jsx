// 불린 상태 토글 기능 학습을 위한 컴포넌트

import { useState } from 'react'

function ToggleExample() {
  // 1. 기본 불린 상태들
  const [isVisible, setIsVisible] = useState(false)
  const [isEnabled, setIsEnabled] = useState(true)
  const [isDarkMode, setIsDarkMode] = useState(false)
  const [isExpanded, setIsExpanded] = useState(false)
  const [notifications, setNotifications] = useState({
    email: true,
    sms: false,
    push: true,
    marketing: false
  })

  // 2. 복합 토글 상태
  const [settings, setSettings] = useState({
    autoSave: true,
    showTips: true,
    soundEnabled: false,
    animationsEnabled: true
  })

  // 3. 다중 선택 상태 (배열로 관리)
  const [selectedFeatures, setSelectedFeatures] = useState(['feature1', 'feature3'])
  const availableFeatures = [
    { id: 'feature1', name: '자동 백업', description: '데이터를 자동으로 백업합니다' },
    { id: 'feature2', name: '실시간 동기화', description: '여러 기기 간 실시간 동기화' },
    { id: 'feature3', name: '오프라인 모드', description: '인터넷 없이도 사용 가능' },
    { id: 'feature4', name: '고급 분석', description: '상세한 사용 통계 제공' }
  ]

  // 4. 상태에 따른 스타일 변경
  const [theme, setTheme] = useState('light')
  const themes = ['light', 'dark', 'blue', 'green']

  // 토글 함수들
  const toggleVisibility = () => {
    setIsVisible(!isVisible)
  }

  const toggleEnabled = () => {
    setIsEnabled(prevEnabled => !prevEnabled)
  }

  // 객체 내 특정 속성 토글
  const toggleNotification = (type) => {
    setNotifications(prev => ({
      ...prev,
      [type]: !prev[type]
    }))
  }

  const toggleSetting = (key) => {
    setSettings(prev => ({
      ...prev,
      [key]: !prev[key]
    }))
  }

  // 배열 상태 토글 (다중 선택)
  const toggleFeature = (featureId) => {
    setSelectedFeatures(prev => {
      if (prev.includes(featureId)) {
        return prev.filter(id => id !== featureId)
      } else {
        return [...prev, featureId]
      }
    })
  }

  // 모든 기능 선택/해제
  const toggleAllFeatures = () => {
    if (selectedFeatures.length === availableFeatures.length) {
      setSelectedFeatures([])  // 모두 해제
    } else {
      setSelectedFeatures(availableFeatures.map(f => f.id))  // 모두 선택
    }
  }

  // 테마 순환 변경
  const cycleTheme = () => {
    const currentIndex = themes.indexOf(theme)
    const nextIndex = (currentIndex + 1) % themes.length
    setTheme(themes[nextIndex])
  }

  return (
    <div className={`toggle-example theme-${theme}`}>
      <h2>불린 상태 토글 학습</h2>

      {/* 1. 기본 토글 예제 */}
      <div className="section">
        <h3>1. 기본 토글 기능</h3>
        
        <div className="toggle-group">
          <div className="toggle-item">
            <button onClick={toggleVisibility} className="toggle-btn">
              {isVisible ? '숨기기' : '보이기'}
            </button>
            <span className="toggle-status">
              상태: {isVisible ? '보임' : '숨김'}
            </span>
          </div>

          {/* 조건부 렌더링 */}
          {isVisible && (
            <div className="revealed-content">
              <p>🎉 이 내용이 토글로 보여지고 있습니다!</p>
              <p>isVisible 상태가 true일 때만 렌더링됩니다.</p>
            </div>
          )}
        </div>

        <div className="toggle-group">
          <div className="toggle-item">
            <label className="switch">
              <input
                type="checkbox"
                checked={isEnabled}
                onChange={toggleEnabled}
              />
              <span className="slider"></span>
            </label>
            <span className="toggle-label">
              기능 {isEnabled ? '활성화' : '비활성화'}
            </span>
          </div>
        </div>
      </div>

      {/* 2. 다크모드 토글 */}
      <div className="section">
        <h3>2. 다크모드 토글</h3>
        <div className="dark-mode-toggle">
          <button 
            onClick={() => setIsDarkMode(!isDarkMode)}
            className={`mode-btn ${isDarkMode ? 'dark' : 'light'}`}
          >
            {isDarkMode ? '🌙 다크모드' : '☀️ 라이트모드'}
          </button>
          <div className={`demo-area ${isDarkMode ? 'dark' : 'light'}`}>
            <p>이 영역의 스타일이 모드에 따라 변경됩니다</p>
            <p>현재 모드: {isDarkMode ? '다크' : '라이트'}</p>
          </div>
        </div>
      </div>

      {/* 3. 확장/축소 토글 */}
      <div className="section">
        <h3>3. 확장/축소 토글</h3>
        <div className="expandable-section">
          <button 
            onClick={() => setIsExpanded(!isExpanded)}
            className="expand-btn"
          >
            {isExpanded ? '▼ 축소하기' : '▶ 더 보기'}
          </button>
          
          <div className={`expandable-content ${isExpanded ? 'expanded' : 'collapsed'}`}>
            <h4>상세 정보</h4>
            <p>이 섹션은 토글로 확장/축소됩니다.</p>
            <p>CSS 트랜지션과 함께 사용하면 부드러운 애니메이션 효과를 만들 수 있습니다.</p>
            <ul>
              <li>useState로 확장 상태 관리</li>
              <li>조건부 클래스명으로 스타일 변경</li>
              <li>CSS transition으로 애니메이션</li>
            </ul>
          </div>
        </div>
      </div>

      {/* 4. 알림 설정 (객체 상태 토글) */}
      <div className="section">
        <h3>4. 알림 설정 (객체 상태 토글)</h3>
        <div className="notification-settings">
          {Object.entries(notifications).map(([type, enabled]) => (
            <div key={type} className="notification-item">
              <label className="notification-label">
                <input
                  type="checkbox"
                  checked={enabled}
                  onChange={() => toggleNotification(type)}
                />
                <span className="checkmark"></span>
                {type === 'email' && '이메일 알림'}
                {type === 'sms' && 'SMS 알림'}
                {type === 'push' && '푸시 알림'}
                {type === 'marketing' && '마케팅 알림'}
              </label>
              <span className={`status ${enabled ? 'on' : 'off'}`}>
                {enabled ? 'ON' : 'OFF'}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* 5. 앱 설정 (복합 토글) */}
      <div className="section">
        <h3>5. 앱 설정</h3>
        <div className="app-settings">
          {Object.entries(settings).map(([key, value]) => (
            <div key={key} className="setting-item">
              <div className="setting-info">
                <span className="setting-name">
                  {key === 'autoSave' && '자동 저장'}
                  {key === 'showTips' && '도움말 표시'}
                  {key === 'soundEnabled' && '사운드 효과'}
                  {key === 'animationsEnabled' && '애니메이션 효과'}
                </span>
                <span className="setting-description">
                  {key === 'autoSave' && '변경사항을 자동으로 저장합니다'}
                  {key === 'showTips' && '사용법 도움말을 표시합니다'}
                  {key === 'soundEnabled' && '버튼 클릭 시 사운드를 재생합니다'}
                  {key === 'animationsEnabled' && '부드러운 애니메이션을 사용합니다'}
                </span>
              </div>
              <label className="switch">
                <input
                  type="checkbox"
                  checked={value}
                  onChange={() => toggleSetting(key)}
                />
                <span className="slider round"></span>
              </label>
            </div>
          ))}
        </div>
      </div>

      {/* 6. 다중 선택 토글 */}
      <div className="section">
        <h3>6. 기능 선택 (다중 토글)</h3>
        <div className="feature-selection">
          <div className="selection-header">
            <button onClick={toggleAllFeatures} className="select-all-btn">
              {selectedFeatures.length === availableFeatures.length ? '모두 해제' : '모두 선택'}
            </button>
            <span className="selection-count">
              {selectedFeatures.length}/{availableFeatures.length} 선택됨
            </span>
          </div>
          
          <div className="feature-list">
            {availableFeatures.map(feature => (
              <div key={feature.id} className="feature-item">
                <label className="feature-label">
                  <input
                    type="checkbox"
                    checked={selectedFeatures.includes(feature.id)}
                    onChange={() => toggleFeature(feature.id)}
                  />
                  <span className="feature-info">
                    <span className="feature-name">{feature.name}</span>
                    <span className="feature-description">{feature.description}</span>
                  </span>
                </label>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 7. 테마 선택 */}
      <div className="section">
        <h3>7. 테마 변경</h3>
        <div className="theme-selector">
          <button onClick={cycleTheme} className="theme-cycle-btn">
            🎨 테마 변경 (현재: {theme})
          </button>
          <div className="theme-options">
            {themes.map(themeName => (
              <button
                key={themeName}
                onClick={() => setTheme(themeName)}
                className={`theme-option ${theme === themeName ? 'active' : ''}`}
              >
                {themeName}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* 실시간 상태 표시 */}
      <div className="debug-section">
        <h3>🔍 실시간 토글 상태</h3>
        <pre className="debug-info">
{`기본 토글 상태:
- isVisible: ${isVisible}
- isEnabled: ${isEnabled}
- isDarkMode: ${isDarkMode}
- isExpanded: ${isExpanded}

알림 설정:
${JSON.stringify(notifications, null, 2)}

앱 설정:
${JSON.stringify(settings, null, 2)}

선택된 기능: [${selectedFeatures.join(', ')}]
현재 테마: ${theme}`}
        </pre>
      </div>

      {/* 토글 사용 팁 */}
      <div className="tips-section">
        <h3>💡 토글 상태 관리 팁</h3>
        <div className="tips-grid">
          <div className="tip">
            <h4>1. 불린 토글</h4>
            <code>setState(!state)</code>
            <p>또는 함수형: setState(prev => !prev)</p>
          </div>
          <div className="tip">
            <h4>2. 객체 내 토글</h4>
            <code>setState({`{...prev, key: !prev.key}`})</code>
          </div>
          <div className="tip">
            <h4>3. 배열 토글</h4>
            <p>includes로 확인 후 filter/spread 사용</p>
          </div>
          <div className="tip">
            <h4>4. 조건부 렌더링</h4>
            <p>토글 상태에 따른 UI 변경</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ToggleExample