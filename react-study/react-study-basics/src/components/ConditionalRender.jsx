// 조건부 렌더링 패턴 학습을 위한 컴포넌트

import { useState } from 'react'

function ConditionalRender() {
  // 다양한 상태들을 관리
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [userRole, setUserRole] = useState('guest') // 'guest', 'user', 'admin'
  const [showDetails, setShowDetails] = useState(false)
  const [notifications, setNotifications] = useState([
    { id: 1, message: "새로운 메시지가 있습니다", type: "info" },
    { id: 2, message: "시스템 업데이트 완료", type: "success" },
    { id: 3, message: "주의: 디스크 용량 부족", type: "warning" }
  ])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  // 가짜 로딩 시뮬레이션
  const simulateLoading = () => {
    setLoading(true)
    setError(null)
    
    setTimeout(() => {
      // 50% 확률로 에러 발생
      if (Math.random() > 0.5) {
        setError("데이터를 불러오는데 실패했습니다.")
      }
      setLoading(false)
    }, 2000)
  }

  return (
    <div className="conditional-render">
      <h2>조건부 렌더링 패턴 학습</h2>
      
      {/* 1. 기본 조건부 렌더링 - && 연산자 */}
      <div className="section">
        <h3>1. && 연산자를 사용한 조건부 렌더링</h3>
        <button onClick={() => setIsLoggedIn(!isLoggedIn)}>
          {isLoggedIn ? '로그아웃' : '로그인'}
        </button>
        
        {/* 로그인 상태일 때만 보여줌 */}
        {isLoggedIn && (
          <div className="welcome-message">
            <p>✅ 환영합니다! 로그인되었습니다.</p>
          </div>
        )}
        
        {/* 알림이 있을 때만 보여줌 */}
        {notifications.length > 0 && (
          <div className="notification-badge">
            📢 {notifications.length}개의 알림이 있습니다
          </div>
        )}
      </div>

      {/* 2. 삼항 연산자를 사용한 조건부 렌더링 */}
      <div className="section">
        <h3>2. 삼항 연산자를 사용한 조건부 렌더링</h3>
        <div className="user-status">
          상태: {isLoggedIn ? (
            <span className="status online">🟢 온라인</span>
          ) : (
            <span className="status offline">🔴 오프라인</span>
          )}
        </div>
        
        <div className="content">
          {isLoggedIn ? (
            <div className="dashboard">
              <h4>대시보드</h4>
              <p>사용자 전용 컨텐츠입니다.</p>
            </div>
          ) : (
            <div className="login-prompt">
              <h4>로그인이 필요합니다</h4>
              <p>서비스를 이용하려면 로그인해주세요.</p>
            </div>
          )}
        </div>
      </div>

      {/* 3. 다중 조건 렌더링 */}
      <div className="section">
        <h3>3. 다중 조건 렌더링 (역할 기반)</h3>
        <div className="role-selector">
          <label>사용자 역할: </label>
          <select 
            value={userRole} 
            onChange={(e) => setUserRole(e.target.value)}
          >
            <option value="guest">게스트</option>
            <option value="user">일반 사용자</option>
            <option value="admin">관리자</option>
          </select>
        </div>

        {/* 역할에 따른 다른 컨텐츠 표시 */}
        <div className="role-content">
          {userRole === 'guest' && (
            <div className="guest-content">
              <p>👋 게스트님, 회원가입을 해보세요!</p>
              <button>회원가입</button>
            </div>
          )}
          
          {userRole === 'user' && (
            <div className="user-content">
              <p>📚 일반 사용자 메뉴</p>
              <ul>
                <li>프로필 보기</li>
                <li>설정 변경</li>
                <li>고객 지원</li>
              </ul>
            </div>
          )}
          
          {userRole === 'admin' && (
            <div className="admin-content">
              <p>⚙️ 관리자 메뉴</p>
              <ul>
                <li>사용자 관리</li>
                <li>시스템 설정</li>
                <li>통계 보기</li>
                <li>로그 관리</li>
              </ul>
            </div>
          )}
        </div>
      </div>

      {/* 4. 로딩 상태와 에러 처리 */}
      <div className="section">
        <h3>4. 로딩 상태와 에러 처리</h3>
        <button onClick={simulateLoading} disabled={loading}>
          {loading ? '로딩 중...' : '데이터 불러오기'}
        </button>

        {/* 로딩 중일 때 */}
        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>데이터를 불러오는 중입니다...</p>
          </div>
        )}

        {/* 에러가 있을 때 */}
        {error && (
          <div className="error">
            <p>❌ {error}</p>
            <button onClick={() => setError(null)}>에러 닫기</button>
          </div>
        )}

        {/* 로딩도 아니고 에러도 없을 때 */}
        {!loading && !error && (
          <div className="success">
            <p>✅ 데이터를 성공적으로 불러왔습니다!</p>
          </div>
        )}
      </div>

      {/* 5. 복잡한 조건부 렌더링 */}
      <div className="section">
        <h3>5. 복잡한 조건부 렌더링</h3>
        <button onClick={() => setShowDetails(!showDetails)}>
          {showDetails ? '상세 정보 숨기기' : '상세 정보 보기'}
        </button>

        {showDetails && (
          <div className="details">
            <h4>상세 정보</h4>
            
            {/* 로그인 상태와 역할을 모두 고려한 조건부 렌더링 */}
            {isLoggedIn ? (
              userRole === 'admin' ? (
                <div className="admin-details">
                  <p>🔐 관리자 전용 상세 정보</p>
                  <p>시스템 상태: 정상</p>
                  <p>활성 사용자: 1,234명</p>
                </div>
              ) : (
                <div className="user-details">
                  <p>👤 사용자 상세 정보</p>
                  <p>가입일: 2024-01-15</p>
                  <p>마지막 로그인: 방금 전</p>
                </div>
              )
            ) : (
              <div className="guest-details">
                <p>🚫 로그인이 필요한 정보입니다</p>
              </div>
            )}
          </div>
        )}
      </div>

      {/* 조건부 렌더링 팁 */}
      <div className="section tips">
        <h3>💡 조건부 렌더링 팁</h3>
        <ul>
          <li><strong>&&</strong>: 조건이 true일 때만 렌더링</li>
          <li><strong>삼항연산자</strong>: true/false에 따라 다른 컴포넌트 렌더링</li>
          <li><strong>즉시실행함수</strong>: 복잡한 조건 로직이 필요할 때</li>
          <li><strong>조기 반환</strong>: 컴포넌트 함수에서 조건에 따라 일찍 return</li>
          <li><strong>null 반환</strong>: 아무것도 렌더링하지 않을 때</li>
        </ul>
      </div>
    </div>
  )
}

export default ConditionalRender