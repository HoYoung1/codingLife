// useEffect Hook 기본 사용법 - 시스템 모니터링 대시보드 예제

import { useState, useEffect } from 'react'

function EffectExample() {
  // 시스템 모니터링 상태들
  const [serverStatus, setServerStatus] = useState('checking')
  const [cpuUsage, setCpuUsage] = useState(0)
  const [memoryUsage, setMemoryUsage] = useState(0)
  const [lastUpdate, setLastUpdate] = useState(null)
  const [connectionCount, setConnectionCount] = useState(0)
  const [systemLogs, setSystemLogs] = useState([])
  const [autoRefresh, setAutoRefresh] = useState(true)

  // 가짜 시스템 데이터 생성 함수들
  const generateSystemData = () => {
    return {
      cpu: Math.floor(Math.random() * 100),
      memory: Math.floor(Math.random() * 100),
      connections: Math.floor(Math.random() * 50) + 10,
      status: Math.random() > 0.1 ? 'healthy' : 'warning'
    }
  }

  const addSystemLog = (message, type = 'info') => {
    const newLog = {
      id: Date.now(),
      timestamp: new Date().toLocaleTimeString(),
      message,
      type
    }
    setSystemLogs(prev => [newLog, ...prev.slice(0, 9)]) // 최근 10개만 유지
  }

  // 1. 컴포넌트 마운트 시 한 번만 실행 (dependency array가 빈 배열)
  useEffect(() => {
    console.log('🚀 대시보드 컴포넌트가 마운트되었습니다!')
    
    // 초기 시스템 상태 체크
    setServerStatus('initializing')
    addSystemLog('시스템 모니터링 시작', 'info')
    
    // 초기 데이터 로드 시뮬레이션
    setTimeout(() => {
      const initialData = generateSystemData()
      setCpuUsage(initialData.cpu)
      setMemoryUsage(initialData.memory)
      setConnectionCount(initialData.connections)
      setServerStatus(initialData.status)
      setLastUpdate(new Date())
      addSystemLog('초기 시스템 데이터 로드 완료', 'success')
    }, 1000)

    // 컴포넌트가 언마운트될 때 실행되는 클린업 함수
    return () => {
      console.log('🔄 대시보드 컴포넌트가 언마운트됩니다!')
      addSystemLog('시스템 모니터링 종료', 'warning')
    }
  }, []) // 빈 dependency array = 마운트 시 한 번만 실행

  // 2. 특정 상태가 변경될 때마다 실행 (dependency array에 상태 포함)
  useEffect(() => {
    console.log(`📊 CPU 사용률이 ${cpuUsage}%로 변경되었습니다`)
    
    // CPU 사용률에 따른 경고 로직
    if (cpuUsage > 80) {
      addSystemLog(`⚠️ CPU 사용률 높음: ${cpuUsage}%`, 'warning')
      setServerStatus('warning')
    } else if (cpuUsage > 95) {
      addSystemLog(`🚨 CPU 사용률 위험: ${cpuUsage}%`, 'error')
      setServerStatus('critical')
    }
  }, [cpuUsage]) // cpuUsage가 변경될 때마다 실행

  // 3. 여러 상태를 감시
  useEffect(() => {
    console.log(`💾 메모리 사용률: ${memoryUsage}%, 연결 수: ${connectionCount}`)
    
    // 메모리와 연결 수를 종합적으로 판단
    if (memoryUsage > 90 && connectionCount > 40) {
      addSystemLog('시스템 부하 높음 - 메모리 및 연결 수 확인 필요', 'warning')
    }
  }, [memoryUsage, connectionCount]) // 두 상태 중 하나라도 변경되면 실행

  // 4. dependency array 없음 - 매 렌더링마다 실행 (비추천)
  useEffect(() => {
    // 이 방법은 성능상 좋지 않습니다!
    // 매번 렌더링될 때마다 실행되므로 주의해서 사용해야 합니다
    console.log('🔄 컴포넌트가 렌더링되었습니다 (매번 실행)')
  }) // dependency array 없음 = 매 렌더링마다 실행

  // 5. 자동 새로고침 기능 (조건부 useEffect)
  useEffect(() => {
    let intervalId

    if (autoRefresh) {
      console.log('⏰ 자동 새로고침 시작')
      addSystemLog('자동 새로고침 활성화', 'info')
      
      intervalId = setInterval(() => {
        const newData = generateSystemData()
        setCpuUsage(newData.cpu)
        setMemoryUsage(newData.memory)
        setConnectionCount(newData.connections)
        setLastUpdate(new Date())
        
        console.log('🔄 시스템 데이터 자동 업데이트')
      }, 3000) // 3초마다 업데이트
    } else {
      console.log('⏸️ 자동 새로고침 중지')
      addSystemLog('자동 새로고침 비활성화', 'info')
    }

    // 클린업 함수 - 인터벌 정리
    return () => {
      if (intervalId) {
        clearInterval(intervalId)
        console.log('🧹 인터벌 정리됨')
      }
    }
  }, [autoRefresh]) // autoRefresh 상태가 변경될 때마다 실행

  // 수동 새로고침 함수
  const handleManualRefresh = () => {
    addSystemLog('수동 새로고침 실행', 'info')
    const newData = generateSystemData()
    setCpuUsage(newData.cpu)
    setMemoryUsage(newData.memory)
    setConnectionCount(newData.connections)
    setServerStatus(newData.status)
    setLastUpdate(new Date())
  }

  // 시스템 상태에 따른 색상 결정
  const getStatusColor = (status) => {
    switch (status) {
      case 'healthy': return '#52c41a'
      case 'warning': return '#faad14'
      case 'critical': return '#ff4d4f'
      case 'checking': return '#1890ff'
      default: return '#d9d9d9'
    }
  }

  const getUsageColor = (usage) => {
    if (usage > 90) return '#ff4d4f'
    if (usage > 70) return '#faad14'
    return '#52c41a'
  }

  return (
    <div className="effect-example">
      <h2>useEffect Hook 학습 - 시스템 모니터링 대시보드</h2>

      {/* 시스템 상태 개요 */}
      <div className="dashboard-header">
        <div className="status-card">
          <h3>서버 상태</h3>
          <div 
            className="status-indicator"
            style={{ backgroundColor: getStatusColor(serverStatus) }}
          >
            {serverStatus.toUpperCase()}
          </div>
          <p>마지막 업데이트: {lastUpdate ? lastUpdate.toLocaleTimeString() : '확인 중...'}</p>
        </div>

        <div className="control-panel">
          <button 
            onClick={() => setAutoRefresh(!autoRefresh)}
            className={`refresh-toggle ${autoRefresh ? 'active' : ''}`}
          >
            {autoRefresh ? '⏸️ 자동새로고침 중지' : '▶️ 자동새로고침 시작'}
          </button>
          <button onClick={handleManualRefresh} className="manual-refresh">
            🔄 수동 새로고침
          </button>
        </div>
      </div>

      {/* 시스템 메트릭 */}
      <div className="metrics-grid">
        <div className="metric-card">
          <h4>CPU 사용률</h4>
          <div className="metric-value" style={{ color: getUsageColor(cpuUsage) }}>
            {cpuUsage}%
          </div>
          <div className="metric-bar">
            <div 
              className="metric-fill"
              style={{ 
                width: `${cpuUsage}%`,
                backgroundColor: getUsageColor(cpuUsage)
              }}
            />
          </div>
        </div>

        <div className="metric-card">
          <h4>메모리 사용률</h4>
          <div className="metric-value" style={{ color: getUsageColor(memoryUsage) }}>
            {memoryUsage}%
          </div>
          <div className="metric-bar">
            <div 
              className="metric-fill"
              style={{ 
                width: `${memoryUsage}%`,
                backgroundColor: getUsageColor(memoryUsage)
              }}
            />
          </div>
        </div>

        <div className="metric-card">
          <h4>활성 연결</h4>
          <div className="metric-value" style={{ color: '#1890ff' }}>
            {connectionCount}
          </div>
          <div className="connection-status">
            {connectionCount > 30 ? '높음' : connectionCount > 15 ? '보통' : '낮음'}
          </div>
        </div>
      </div>

      {/* 시스템 로그 */}
      <div className="system-logs">
        <h3>시스템 로그 (실시간)</h3>
        <div className="log-container">
          {systemLogs.length === 0 ? (
            <p className="no-logs">로그가 없습니다.</p>
          ) : (
            systemLogs.map(log => (
              <div key={log.id} className={`log-entry log-${log.type}`}>
                <span className="log-time">{log.timestamp}</span>
                <span className="log-message">{log.message}</span>
              </div>
            ))
          )}
        </div>
      </div>

      {/* useEffect 패턴 설명 */}
      <div className="effect-patterns">
        <h3>💡 useEffect 패턴 설명</h3>
        <div className="pattern-grid">
          <div className="pattern-card">
            <h4>1. 마운트 시 한 번 실행</h4>
            <code>useEffect(() => {`{}`}, [])</code>
            <p>컴포넌트가 처음 렌더링될 때만 실행</p>
            <p>예: 초기 데이터 로드, API 호출</p>
          </div>

          <div className="pattern-card">
            <h4>2. 특정 상태 변경 시 실행</h4>
            <code>useEffect(() => {`{}`}, [state])</code>
            <p>지정한 상태가 변경될 때마다 실행</p>
            <p>예: CPU 사용률 변경 감지</p>
          </div>

          <div className="pattern-card">
            <h4>3. 여러 상태 감시</h4>
            <code>useEffect(() => {`{}`}, [state1, state2])</code>
            <p>여러 상태 중 하나라도 변경되면 실행</p>
            <p>예: 메모리 + 연결 수 종합 판단</p>
          </div>

          <div className="pattern-card">
            <h4>4. 클린업 함수</h4>
            <code>useEffect(() => {`{ return () => {} }`})</code>
            <p>컴포넌트 언마운트 시 정리 작업</p>
            <p>예: 타이머 정리, 이벤트 리스너 제거</p>
          </div>
        </div>
      </div>

      {/* 실시간 디버깅 정보 */}
      <div className="debug-section">
        <h3>🔍 실시간 useEffect 동작 상황</h3>
        <div className="debug-info">
          <p><strong>현재 상태:</strong></p>
          <ul>
            <li>서버 상태: {serverStatus}</li>
            <li>CPU: {cpuUsage}%</li>
            <li>메모리: {memoryUsage}%</li>
            <li>연결 수: {connectionCount}</li>
            <li>자동 새로고침: {autoRefresh ? 'ON' : 'OFF'}</li>
            <li>로그 개수: {systemLogs.length}</li>
          </ul>
          
          <p><strong>useEffect 실행 상황:</strong></p>
          <p>브라우저 개발자 도구 콘솔을 확인해보세요!</p>
          <p>각 useEffect가 언제 실행되는지 로그로 확인할 수 있습니다.</p>
        </div>
      </div>

      {/* 주의사항 */}
      <div className="warning-section">
        <h3>⚠️ useEffect 사용 시 주의사항</h3>
        <ul>
          <li><strong>무한 루프 방지:</strong> dependency array를 올바르게 설정</li>
          <li><strong>메모리 누수 방지:</strong> 클린업 함수로 타이머/이벤트 정리</li>
          <li><strong>성능 최적화:</strong> 불필요한 재실행 방지</li>
          <li><strong>비동기 처리:</strong> useEffect 내에서 async/await 직접 사용 금지</li>
        </ul>
      </div>
    </div>
  )
}

export default EffectExample