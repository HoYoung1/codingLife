// 타이머와 클린업 패턴 학습 - 실시간 모니터링 시스템

import { useState, useEffect, useRef } from 'react'

function TimerExample() {
  // 타이머 상태들
  const [currentTime, setCurrentTime] = useState(new Date())
  const [systemUptime, setSystemUptime] = useState(0)
  const [alertCount, setAlertCount] = useState(0)
  const [isMonitoring, setIsMonitoring] = useState(false)
  
  // 성능 모니터링 상태
  const [cpuHistory, setCpuHistory] = useState([])
  const [memoryHistory, setMemoryHistory] = useState([])
  const [networkActivity, setNetworkActivity] = useState([])
  
  // 알림 시스템 상태
  const [notifications, setNotifications] = useState([])
  const [lastHeartbeat, setLastHeartbeat] = useState(null)
  const [connectionStatus, setConnectionStatus] = useState('disconnected')
  
  // 설정 상태
  const [monitoringInterval, setMonitoringInterval] = useState(1000) // 1초
  const [dataRetentionTime, setDataRetentionTime] = useState(60) // 60초
  const [alertThreshold, setAlertThreshold] = useState(80)

  // useRef로 타이머 ID들을 저장 (클린업을 위해)
  const clockTimerRef = useRef(null)
  const uptimeTimerRef = useRef(null)
  const monitoringTimerRef = useRef(null)
  const heartbeatTimerRef = useRef(null)
  const cleanupTimerRef = useRef(null)

  // 가짜 데이터 생성 함수들
  const generateMetricData = () => ({
    cpu: Math.floor(Math.random() * 100),
    memory: Math.floor(Math.random() * 100),
    network: Math.floor(Math.random() * 1000),
    timestamp: Date.now()
  })

  const generateNotification = (type, message) => ({
    id: Date.now() + Math.random(),
    type,
    message,
    timestamp: new Date().toLocaleTimeString(),
    read: false
  })

  // 1. 실시간 시계 (1초마다 업데이트)
  useEffect(() => {
    console.log('⏰ 실시간 시계 시작')
    
    clockTimerRef.current = setInterval(() => {
      setCurrentTime(new Date())
    }, 1000)

    // 클린업 함수
    return () => {
      console.log('🧹 실시간 시계 정리')
      if (clockTimerRef.current) {
        clearInterval(clockTimerRef.current)
      }
    }
  }, []) // 컴포넌트 마운트 시 한 번만 설정

  // 2. 시스템 업타임 카운터
  useEffect(() => {
    console.log('📊 업타임 카운터 시작')
    
    uptimeTimerRef.current = setInterval(() => {
      setSystemUptime(prev => prev + 1)
    }, 1000)

    return () => {
      console.log('🧹 업타임 카운터 정리')
      if (uptimeTimerRef.current) {
        clearInterval(uptimeTimerRef.current)
      }
    }
  }, [])

  // 3. 모니터링 시스템 (조건부 타이머)
  useEffect(() => {
    if (isMonitoring) {
      console.log(`📡 모니터링 시작 (${monitoringInterval}ms 간격)`)
      setConnectionStatus('connected')
      
      monitoringTimerRef.current = setInterval(() => {
        const data = generateMetricData()
        
        // CPU 히스토리 업데이트
        setCpuHistory(prev => {
          const newHistory = [...prev, { value: data.cpu, timestamp: data.timestamp }]
          return newHistory.slice(-dataRetentionTime) // 최근 N개만 유지
        })
        
        // 메모리 히스토리 업데이트
        setMemoryHistory(prev => {
          const newHistory = [...prev, { value: data.memory, timestamp: data.timestamp }]
          return newHistory.slice(-dataRetentionTime)
        })
        
        // 네트워크 활동 업데이트
        setNetworkActivity(prev => {
          const newActivity = [...prev, { value: data.network, timestamp: data.timestamp }]
          return newActivity.slice(-20) // 최근 20개만 유지
        })
        
        // 임계값 초과 시 알림 생성
        if (data.cpu > alertThreshold) {
          setAlertCount(prev => prev + 1)
          setNotifications(prev => [
            generateNotification('warning', `CPU 사용률 높음: ${data.cpu}%`),
            ...prev.slice(0, 9) // 최근 10개만 유지
          ])
        }
        
        if (data.memory > alertThreshold) {
          setAlertCount(prev => prev + 1)
          setNotifications(prev => [
            generateNotification('error', `메모리 사용률 위험: ${data.memory}%`),
            ...prev.slice(0, 9)
          ])
        }
        
        console.log(`📊 모니터링 데이터 업데이트: CPU ${data.cpu}%, Memory ${data.memory}%`)
      }, monitoringInterval)
    } else {
      console.log('⏸️ 모니터링 중지')
      setConnectionStatus('disconnected')
    }

    // 클린업 함수
    return () => {
      if (monitoringTimerRef.current) {
        console.log('🧹 모니터링 타이머 정리')
        clearInterval(monitoringTimerRef.current)
      }
    }
  }, [isMonitoring, monitoringInterval, alertThreshold, dataRetentionTime])

  // 4. 하트비트 시스템 (연결 상태 확인)
  useEffect(() => {
    if (isMonitoring) {
      console.log('💓 하트비트 시스템 시작')
      
      heartbeatTimerRef.current = setInterval(() => {
        setLastHeartbeat(new Date())
        
        // 가끔 연결 문제 시뮬레이션
        if (Math.random() < 0.05) { // 5% 확률
          setConnectionStatus('unstable')
          setNotifications(prev => [
            generateNotification('warning', '연결이 불안정합니다'),
            ...prev.slice(0, 9)
          ])
        } else {
          setConnectionStatus('connected')
        }
      }, 5000) // 5초마다 하트비트
    }

    return () => {
      if (heartbeatTimerRef.current) {
        console.log('🧹 하트비트 타이머 정리')
        clearInterval(heartbeatTimerRef.current)
      }
    }
  }, [isMonitoring])

  // 5. 데이터 정리 타이머 (메모리 관리)
  useEffect(() => {
    console.log('🧹 데이터 정리 시스템 시작')
    
    cleanupTimerRef.current = setInterval(() => {
      const now = Date.now()
      const retentionMs = dataRetentionTime * 1000
      
      // 오래된 데이터 정리
      setCpuHistory(prev => 
        prev.filter(item => now - item.timestamp < retentionMs)
      )
      
      setMemoryHistory(prev => 
        prev.filter(item => now - item.timestamp < retentionMs)
      )
      
      // 읽은 알림 정리 (30초 후)
      setNotifications(prev => 
        prev.filter(notification => {
          const notificationTime = new Date(`1970-01-01 ${notification.timestamp}`).getTime()
          return now - notificationTime < 30000 || !notification.read
        })
      )
      
      console.log('🧹 오래된 데이터 정리 완료')
    }, 10000) // 10초마다 정리

    return () => {
      if (cleanupTimerRef.current) {
        console.log('🧹 데이터 정리 타이머 정리')
        clearInterval(cleanupTimerRef.current)
      }
    }
  }, [dataRetentionTime])

  // 6. 컴포넌트 언마운트 시 모든 타이머 정리
  useEffect(() => {
    return () => {
      console.log('🔄 컴포넌트 언마운트 - 모든 타이머 정리')
      
      // 모든 타이머 정리
      const timers = [
        clockTimerRef.current,
        uptimeTimerRef.current,
        monitoringTimerRef.current,
        heartbeatTimerRef.current,
        cleanupTimerRef.current
      ]
      
      timers.forEach(timer => {
        if (timer) clearInterval(timer)
      })
    }
  }, [])

  // 유틸리티 함수들
  const formatUptime = (seconds) => {
    const hours = Math.floor(seconds / 3600)
    const minutes = Math.floor((seconds % 3600) / 60)
    const secs = seconds % 60
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`
  }

  const getConnectionStatusColor = (status) => {
    switch (status) {
      case 'connected': return '#52c41a'
      case 'unstable': return '#faad14'
      case 'disconnected': return '#ff4d4f'
      default: return '#d9d9d9'
    }
  }

  const markNotificationAsRead = (id) => {
    setNotifications(prev => 
      prev.map(notification => 
        notification.id === id 
          ? { ...notification, read: true }
          : notification
      )
    )
  }

  const clearAllNotifications = () => {
    setNotifications([])
    setAlertCount(0)
  }

  const toggleMonitoring = () => {
    setIsMonitoring(prev => !prev)
    if (!isMonitoring) {
      setNotifications(prev => [
        generateNotification('info', '모니터링 시스템이 시작되었습니다'),
        ...prev.slice(0, 9)
      ])
    } else {
      setNotifications(prev => [
        generateNotification('info', '모니터링 시스템이 중지되었습니다'),
        ...prev.slice(0, 9)
      ])
    }
  }

  return (
    <div className="timer-example">
      <h2>타이머와 클린업 패턴 - 실시간 모니터링 시스템</h2>

      {/* 시스템 상태 헤더 */}
      <div className="system-header">
        <div className="system-clock">
          <h3>시스템 시간</h3>
          <div className="clock-display">
            {currentTime.toLocaleTimeString()}
          </div>
          <div className="date-display">
            {currentTime.toLocaleDateString()}
          </div>
        </div>

        <div className="system-uptime">
          <h3>시스템 업타임</h3>
          <div className="uptime-display">
            {formatUptime(systemUptime)}
          </div>
          <div className="uptime-seconds">
            {systemUptime} 초
          </div>
        </div>

        <div className="connection-status">
          <h3>연결 상태</h3>
          <div 
            className="status-indicator"
            style={{ backgroundColor: getConnectionStatusColor(connectionStatus) }}
          >
            {connectionStatus.toUpperCase()}
          </div>
          {lastHeartbeat && (
            <div className="last-heartbeat">
              마지막 하트비트: {lastHeartbeat.toLocaleTimeString()}
            </div>
          )}
        </div>
      </div>

      {/* 모니터링 컨트롤 */}
      <div className="monitoring-controls">
        <button 
          onClick={toggleMonitoring}
          className={`monitoring-toggle ${isMonitoring ? 'active' : ''}`}
        >
          {isMonitoring ? '⏸️ 모니터링 중지' : '▶️ 모니터링 시작'}
        </button>

        <div className="control-group">
          <label>업데이트 간격:</label>
          <select 
            value={monitoringInterval} 
            onChange={(e) => setMonitoringInterval(Number(e.target.value))}
          >
            <option value={500}>0.5초</option>
            <option value={1000}>1초</option>
            <option value={2000}>2초</option>
            <option value={5000}>5초</option>
          </select>
        </div>

        <div className="control-group">
          <label>데이터 보관 시간:</label>
          <select 
            value={dataRetentionTime} 
            onChange={(e) => setDataRetentionTime(Number(e.target.value))}
          >
            <option value={30}>30초</option>
            <option value={60}>1분</option>
            <option value={120}>2분</option>
            <option value={300}>5분</option>
          </select>
        </div>

        <div className="control-group">
          <label>알림 임계값:</label>
          <input
            type="range"
            min="50"
            max="95"
            value={alertThreshold}
            onChange={(e) => setAlertThreshold(Number(e.target.value))}
          />
          <span>{alertThreshold}%</span>
        </div>
      </div>

      {/* 실시간 메트릭 차트 */}
      {isMonitoring && (
        <div className="metrics-charts">
          <div className="chart-container">
            <h4>CPU 사용률 히스토리</h4>
            <div className="mini-chart">
              {cpuHistory.map((point, index) => (
                <div
                  key={point.timestamp}
                  className="chart-bar"
                  style={{
                    height: `${point.value}%`,
                    backgroundColor: point.value > alertThreshold ? '#ff4d4f' : '#52c41a',
                    left: `${(index / Math.max(cpuHistory.length - 1, 1)) * 100}%`
                  }}
                />
              ))}
            </div>
            <div className="chart-info">
              현재: {cpuHistory[cpuHistory.length - 1]?.value || 0}%
              | 데이터 포인트: {cpuHistory.length}
            </div>
          </div>

          <div className="chart-container">
            <h4>메모리 사용률 히스토리</h4>
            <div className="mini-chart">
              {memoryHistory.map((point, index) => (
                <div
                  key={point.timestamp}
                  className="chart-bar"
                  style={{
                    height: `${point.value}%`,
                    backgroundColor: point.value > alertThreshold ? '#ff4d4f' : '#1890ff',
                    left: `${(index / Math.max(memoryHistory.length - 1, 1)) * 100}%`
                  }}
                />
              ))}
            </div>
            <div className="chart-info">
              현재: {memoryHistory[memoryHistory.length - 1]?.value || 0}%
              | 데이터 포인트: {memoryHistory.length}
            </div>
          </div>
        </div>
      )}

      {/* 알림 시스템 */}
      <div className="notification-system">
        <div className="notification-header">
          <h3>시스템 알림</h3>
          <div className="notification-controls">
            <span className="alert-count">
              총 알림: {alertCount}개
            </span>
            <button onClick={clearAllNotifications}>
              모든 알림 지우기
            </button>
          </div>
        </div>

        <div className="notifications-list">
          {notifications.length === 0 ? (
            <div className="no-notifications">
              알림이 없습니다.
            </div>
          ) : (
            notifications.map(notification => (
              <div
                key={notification.id}
                className={`notification-item notification-${notification.type} ${
                  notification.read ? 'read' : 'unread'
                }`}
                onClick={() => markNotificationAsRead(notification.id)}
              >
                <div className="notification-content">
                  <span className="notification-message">
                    {notification.message}
                  </span>
                  <span className="notification-time">
                    {notification.timestamp}
                  </span>
                </div>
                {!notification.read && (
                  <div className="unread-indicator" />
                )}
              </div>
            ))
          )}
        </div>
      </div>

      {/* 네트워크 활동 */}
      {networkActivity.length > 0 && (
        <div className="network-activity">
          <h3>네트워크 활동</h3>
          <div className="activity-graph">
            {networkActivity.map((activity, index) => (
              <div
                key={activity.timestamp}
                className="activity-bar"
                style={{
                  height: `${(activity.value / 1000) * 100}%`,
                  backgroundColor: '#722ed1'
                }}
                title={`${activity.value} MB/s`}
              />
            ))}
          </div>
        </div>
      )}

      {/* 타이머 패턴 설명 */}
      <div className="timer-patterns">
        <h3>💡 타이머와 클린업 패턴</h3>
        <div className="pattern-grid">
          <div className="pattern-card">
            <h4>1. setInterval 사용</h4>
            <code>const id = setInterval(callback, delay)</code>
            <p>주기적으로 함수 실행</p>
          </div>

          <div className="pattern-card">
            <h4>2. useRef로 ID 저장</h4>
            <code>const timerRef = useRef(null)</code>
            <p>타이머 ID를 저장해서 나중에 정리</p>
          </div>

          <div className="pattern-card">
            <h4>3. 클린업 함수</h4>
            <code>return () => clearInterval(id)</code>
            <p>컴포넌트 언마운트 시 타이머 정리</p>
          </div>

          <div className="pattern-card">
            <h4>4. 조건부 타이머</h4>
            <code>if (condition) setInterval(...)</code>
            <p>상태에 따라 타이머 시작/중지</p>
          </div>
        </div>
      </div>

      {/* 메모리 누수 방지 팁 */}
      <div className="memory-tips">
        <h3>⚠️ 메모리 누수 방지 팁</h3>
        <ul>
          <li><strong>항상 클린업:</strong> setInterval/setTimeout은 반드시 clear</li>
          <li><strong>useRef 활용:</strong> 타이머 ID를 useRef로 저장</li>
          <li><strong>조건부 정리:</strong> 타이머가 존재할 때만 clear</li>
          <li><strong>데이터 제한:</strong> 무한히 쌓이는 데이터 방지</li>
          <li><strong>이벤트 리스너:</strong> addEventListener도 removeEventListener 필요</li>
        </ul>
      </div>

      {/* 실시간 디버깅 */}
      <div className="debug-section">
        <h3>🔍 실시간 타이머 상태</h3>
        <div className="debug-info">
          <p><strong>활성 타이머:</strong></p>
          <ul>
            <li>시계: {clockTimerRef.current ? '실행 중' : '중지됨'}</li>
            <li>업타임: {uptimeTimerRef.current ? '실행 중' : '중지됨'}</li>
            <li>모니터링: {monitoringTimerRef.current ? '실행 중' : '중지됨'}</li>
            <li>하트비트: {heartbeatTimerRef.current ? '실행 중' : '중지됨'}</li>
            <li>데이터 정리: {cleanupTimerRef.current ? '실행 중' : '중지됨'}</li>
          </ul>
          
          <p><strong>데이터 상태:</strong></p>
          <ul>
            <li>CPU 히스토리: {cpuHistory.length}개</li>
            <li>메모리 히스토리: {memoryHistory.length}개</li>
            <li>네트워크 활동: {networkActivity.length}개</li>
            <li>알림: {notifications.length}개</li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default TimerExample