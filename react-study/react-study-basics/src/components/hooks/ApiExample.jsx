// useEffect에서 API 호출 패턴 학습 - 모니터링 대시보드 API 예제

import { useState, useEffect } from 'react'

function ApiExample() {
  // API 상태 관리
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [retryCount, setRetryCount] = useState(0)
  
  // 대시보드 데이터 상태들
  const [serverMetrics, setServerMetrics] = useState(null)
  const [apiEndpoints, setApiEndpoints] = useState([])
  const [systemAlerts, setSystemAlerts] = useState([])
  const [userActivity, setUserActivity] = useState([])
  
  // 설정 상태
  const [selectedServer, setSelectedServer] = useState('server-1')
  const [refreshInterval, setRefreshInterval] = useState(5000) // 5초
  const [autoRefreshEnabled, setAutoRefreshEnabled] = useState(true)

  // 가짜 API 함수들 (실제로는 axios나 fetch 사용)
  const mockApiCall = (endpoint, delay = 1000, failureRate = 0.1) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (Math.random() < failureRate) {
          reject(new Error(`API 호출 실패: ${endpoint}`))
        } else {
          resolve(generateMockData(endpoint))
        }
      }, delay)
    })
  }

  const generateMockData = (endpoint) => {
    switch (endpoint) {
      case 'server-metrics':
        return {
          serverId: selectedServer,
          timestamp: new Date().toISOString(),
          cpu: Math.floor(Math.random() * 100),
          memory: Math.floor(Math.random() * 100),
          disk: Math.floor(Math.random() * 100),
          network: {
            inbound: Math.floor(Math.random() * 1000),
            outbound: Math.floor(Math.random() * 1000)
          },
          uptime: Math.floor(Math.random() * 86400), // 초 단위
          status: Math.random() > 0.2 ? 'healthy' : 'warning'
        }
      
      case 'api-endpoints':
        return [
          {
            id: 1,
            endpoint: '/api/users',
            method: 'GET',
            responseTime: Math.floor(Math.random() * 500) + 50,
            status: Math.random() > 0.1 ? 200 : 500,
            requestCount: Math.floor(Math.random() * 1000)
          },
          {
            id: 2,
            endpoint: '/api/orders',
            method: 'POST',
            responseTime: Math.floor(Math.random() * 300) + 100,
            status: Math.random() > 0.05 ? 200 : 400,
            requestCount: Math.floor(Math.random() * 500)
          },
          {
            id: 3,
            endpoint: '/api/products',
            method: 'GET',
            responseTime: Math.floor(Math.random() * 200) + 30,
            status: 200,
            requestCount: Math.floor(Math.random() * 2000)
          }
        ]
      
      case 'system-alerts':
        const alertTypes = ['info', 'warning', 'error']
        const messages = [
          'CPU 사용률이 80%를 초과했습니다',
          '새로운 사용자가 로그인했습니다',
          '디스크 공간이 부족합니다',
          'API 응답 시간이 증가했습니다',
          '시스템 백업이 완료되었습니다'
        ]
        
        return Array.from({ length: Math.floor(Math.random() * 5) + 1 }, (_, i) => ({
          id: Date.now() + i,
          type: alertTypes[Math.floor(Math.random() * alertTypes.length)],
          message: messages[Math.floor(Math.random() * messages.length)],
          timestamp: new Date(Date.now() - Math.random() * 3600000).toISOString(),
          serverId: selectedServer
        }))
      
      case 'user-activity':
        const activities = ['login', 'logout', 'page_view', 'api_call', 'error']
        return Array.from({ length: Math.floor(Math.random() * 10) + 5 }, (_, i) => ({
          id: Date.now() + i,
          userId: `user_${Math.floor(Math.random() * 100)}`,
          activity: activities[Math.floor(Math.random() * activities.length)],
          timestamp: new Date(Date.now() - Math.random() * 1800000).toISOString(),
          ip: `192.168.1.${Math.floor(Math.random() * 255)}`,
          userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }))
      
      default:
        return null
    }
  }

  // 1. 컴포넌트 마운트 시 초기 데이터 로드
  useEffect(() => {
    console.log('🚀 API 대시보드 컴포넌트 마운트됨')
    loadInitialData()
    
    return () => {
      console.log('🔄 API 대시보드 컴포넌트 언마운트됨')
    }
  }, []) // 빈 dependency array

  // 2. 서버 선택이 변경될 때 데이터 다시 로드
  useEffect(() => {
    console.log(`🔄 선택된 서버 변경: ${selectedServer}`)
    loadServerData()
  }, [selectedServer]) // selectedServer가 변경될 때마다 실행

  // 3. 자동 새로고침 설정
  useEffect(() => {
    let intervalId

    if (autoRefreshEnabled && refreshInterval > 0) {
      console.log(`⏰ 자동 새로고침 시작 (${refreshInterval}ms 간격)`)
      
      intervalId = setInterval(() => {
        console.log('🔄 자동 새로고침 실행')
        loadServerData()
      }, refreshInterval)
    }

    // 클린업 함수 - 인터벌 정리
    return () => {
      if (intervalId) {
        console.log('🧹 자동 새로고침 인터벌 정리')
        clearInterval(intervalId)
      }
    }
  }, [autoRefreshEnabled, refreshInterval]) // 두 상태 중 하나라도 변경되면 재설정

  // 초기 데이터 로드 함수
  const loadInitialData = async () => {
    setLoading(true)
    setError(null)
    
    try {
      console.log('📡 초기 데이터 로드 시작')
      
      // 병렬로 여러 API 호출
      const [metricsData, endpointsData, alertsData, activityData] = await Promise.all([
        mockApiCall('server-metrics', 800),
        mockApiCall('api-endpoints', 600),
        mockApiCall('system-alerts', 400),
        mockApiCall('user-activity', 500)
      ])
      
      setServerMetrics(metricsData)
      setApiEndpoints(endpointsData)
      setSystemAlerts(alertsData)
      setUserActivity(activityData)
      
      console.log('✅ 초기 데이터 로드 완료')
      setRetryCount(0) // 성공 시 재시도 카운트 리셋
      
    } catch (err) {
      console.error('❌ 초기 데이터 로드 실패:', err)
      setError(err.message)
      setRetryCount(prev => prev + 1)
    } finally {
      setLoading(false)
    }
  }

  // 서버별 데이터 로드 함수
  const loadServerData = async () => {
    // 이미 로딩 중이면 중복 요청 방지
    if (loading) return
    
    setLoading(true)
    setError(null)
    
    try {
      console.log(`📡 서버 데이터 로드: ${selectedServer}`)
      
      const [metricsData, alertsData] = await Promise.all([
        mockApiCall('server-metrics', 500),
        mockApiCall('system-alerts', 300)
      ])
      
      setServerMetrics(metricsData)
      setSystemAlerts(alertsData)
      
      console.log('✅ 서버 데이터 로드 완료')
      setRetryCount(0)
      
    } catch (err) {
      console.error('❌ 서버 데이터 로드 실패:', err)
      setError(err.message)
      setRetryCount(prev => prev + 1)
    } finally {
      setLoading(false)
    }
  }

  // 수동 새로고침
  const handleManualRefresh = () => {
    console.log('🔄 수동 새로고침 실행')
    loadServerData()
  }

  // 재시도 함수
  const handleRetry = () => {
    console.log('🔄 재시도 실행')
    loadInitialData()
  }

  // 시간 포맷팅 함수
  const formatUptime = (seconds) => {
    const hours = Math.floor(seconds / 3600)
    const minutes = Math.floor((seconds % 3600) / 60)
    return `${hours}시간 ${minutes}분`
  }

  const formatTimestamp = (timestamp) => {
    return new Date(timestamp).toLocaleString()
  }

  // 상태별 색상
  const getStatusColor = (status) => {
    switch (status) {
      case 'healthy': return '#52c41a'
      case 'warning': return '#faad14'
      case 'error': return '#ff4d4f'
      default: return '#d9d9d9'
    }
  }

  const getResponseTimeColor = (time) => {
    if (time > 300) return '#ff4d4f'
    if (time > 150) return '#faad14'
    return '#52c41a'
  }

  return (
    <div className="api-example">
      <h2>useEffect API 호출 패턴 - 모니터링 대시보드</h2>

      {/* 컨트롤 패널 */}
      <div className="control-panel">
        <div className="server-selector">
          <label>모니터링 서버:</label>
          <select 
            value={selectedServer} 
            onChange={(e) => setSelectedServer(e.target.value)}
          >
            <option value="server-1">Server-1 (Production)</option>
            <option value="server-2">Server-2 (Staging)</option>
            <option value="server-3">Server-3 (Development)</option>
          </select>
        </div>

        <div className="refresh-controls">
          <label>
            <input
              type="checkbox"
              checked={autoRefreshEnabled}
              onChange={(e) => setAutoRefreshEnabled(e.target.checked)}
            />
            자동 새로고침
          </label>
          
          <select 
            value={refreshInterval} 
            onChange={(e) => setRefreshInterval(Number(e.target.value))}
            disabled={!autoRefreshEnabled}
          >
            <option value={3000}>3초</option>
            <option value={5000}>5초</option>
            <option value={10000}>10초</option>
            <option value={30000}>30초</option>
          </select>

          <button onClick={handleManualRefresh} disabled={loading}>
            {loading ? '🔄 로딩 중...' : '🔄 새로고침'}
          </button>
        </div>
      </div>

      {/* 에러 표시 */}
      {error && (
        <div className="error-banner">
          <div className="error-content">
            <span>❌ {error}</span>
            <div className="error-actions">
              <span>재시도 횟수: {retryCount}</span>
              <button onClick={handleRetry}>다시 시도</button>
            </div>
          </div>
        </div>
      )}

      {/* 로딩 상태 */}
      {loading && (
        <div className="loading-banner">
          <div className="loading-spinner"></div>
          <span>데이터를 불러오는 중...</span>
        </div>
      )}

      {/* 서버 메트릭 */}
      {serverMetrics && (
        <div className="metrics-section">
          <h3>서버 메트릭 - {serverMetrics.serverId}</h3>
          <div className="metrics-grid">
            <div className="metric-card">
              <h4>CPU 사용률</h4>
              <div className="metric-value">{serverMetrics.cpu}%</div>
              <div className="metric-bar">
                <div 
                  className="metric-fill"
                  style={{ 
                    width: `${serverMetrics.cpu}%`,
                    backgroundColor: serverMetrics.cpu > 80 ? '#ff4d4f' : '#52c41a'
                  }}
                />
              </div>
            </div>

            <div className="metric-card">
              <h4>메모리 사용률</h4>
              <div className="metric-value">{serverMetrics.memory}%</div>
              <div className="metric-bar">
                <div 
                  className="metric-fill"
                  style={{ 
                    width: `${serverMetrics.memory}%`,
                    backgroundColor: serverMetrics.memory > 80 ? '#ff4d4f' : '#52c41a'
                  }}
                />
              </div>
            </div>

            <div className="metric-card">
              <h4>디스크 사용률</h4>
              <div className="metric-value">{serverMetrics.disk}%</div>
              <div className="metric-bar">
                <div 
                  className="metric-fill"
                  style={{ 
                    width: `${serverMetrics.disk}%`,
                    backgroundColor: serverMetrics.disk > 90 ? '#ff4d4f' : '#52c41a'
                  }}
                />
              </div>
            </div>

            <div className="metric-card">
              <h4>서버 상태</h4>
              <div 
                className="status-badge"
                style={{ backgroundColor: getStatusColor(serverMetrics.status) }}
              >
                {serverMetrics.status.toUpperCase()}
              </div>
              <div className="uptime">
                가동시간: {formatUptime(serverMetrics.uptime)}
              </div>
            </div>
          </div>

          <div className="network-info">
            <h4>네트워크 트래픽</h4>
            <div className="network-stats">
              <span>⬇️ 인바운드: {serverMetrics.network.inbound} MB/s</span>
              <span>⬆️ 아웃바운드: {serverMetrics.network.outbound} MB/s</span>
            </div>
          </div>
        </div>
      )}

      {/* API 엔드포인트 상태 */}
      {apiEndpoints.length > 0 && (
        <div className="endpoints-section">
          <h3>API 엔드포인트 상태</h3>
          <div className="endpoints-table">
            <div className="table-header">
              <span>엔드포인트</span>
              <span>메소드</span>
              <span>응답시간</span>
              <span>상태</span>
              <span>요청수</span>
            </div>
            {apiEndpoints.map(endpoint => (
              <div key={endpoint.id} className="table-row">
                <span className="endpoint-path">{endpoint.endpoint}</span>
                <span className={`method method-${endpoint.method.toLowerCase()}`}>
                  {endpoint.method}
                </span>
                <span 
                  className="response-time"
                  style={{ color: getResponseTimeColor(endpoint.responseTime) }}
                >
                  {endpoint.responseTime}ms
                </span>
                <span 
                  className="status-code"
                  style={{ color: endpoint.status === 200 ? '#52c41a' : '#ff4d4f' }}
                >
                  {endpoint.status}
                </span>
                <span className="request-count">{endpoint.requestCount}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 시스템 알림 */}
      {systemAlerts.length > 0 && (
        <div className="alerts-section">
          <h3>시스템 알림</h3>
          <div className="alerts-list">
            {systemAlerts.map(alert => (
              <div key={alert.id} className={`alert-item alert-${alert.type}`}>
                <div className="alert-content">
                  <span className="alert-message">{alert.message}</span>
                  <span className="alert-time">{formatTimestamp(alert.timestamp)}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* 사용자 활동 */}
      {userActivity.length > 0 && (
        <div className="activity-section">
          <h3>최근 사용자 활동</h3>
          <div className="activity-list">
            {userActivity.slice(0, 5).map(activity => (
              <div key={activity.id} className="activity-item">
                <span className="activity-user">{activity.userId}</span>
                <span className="activity-type">{activity.activity}</span>
                <span className="activity-time">{formatTimestamp(activity.timestamp)}</span>
                <span className="activity-ip">{activity.ip}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* API 호출 패턴 설명 */}
      <div className="api-patterns">
        <h3>💡 useEffect API 호출 패턴</h3>
        <div className="pattern-grid">
          <div className="pattern-card">
            <h4>1. 초기 데이터 로드</h4>
            <code>useEffect(() => {`{ loadData() }`}, [])</code>
            <p>컴포넌트 마운트 시 한 번만 실행</p>
          </div>

          <div className="pattern-card">
            <h4>2. 의존성 기반 재로드</h4>
            <code>useEffect(() => {`{ loadData() }`}, [serverId])</code>
            <p>특정 상태 변경 시 데이터 재로드</p>
          </div>

          <div className="pattern-card">
            <h4>3. 자동 새로고침</h4>
            <code>setInterval(() => {`{ loadData() }`}, 5000)</code>
            <p>주기적으로 데이터 업데이트</p>
          </div>

          <div className="pattern-card">
            <h4>4. 에러 처리</h4>
            <code>try/catch + 재시도 로직</code>
            <p>API 실패 시 에러 표시 및 재시도</p>
          </div>
        </div>
      </div>

      {/* 주의사항 */}
      <div className="api-tips">
        <h3>⚠️ API 호출 시 주의사항</h3>
        <ul>
          <li><strong>중복 요청 방지:</strong> 로딩 상태 체크</li>
          <li><strong>메모리 누수 방지:</strong> 클린업 함수로 인터벌 정리</li>
          <li><strong>에러 처리:</strong> try/catch와 사용자 친화적 에러 메시지</li>
          <li><strong>로딩 상태:</strong> 사용자에게 진행 상황 표시</li>
          <li><strong>AbortController:</strong> 컴포넌트 언마운트 시 진행 중인 요청 취소</li>
        </ul>
      </div>
    </div>
  )
}

export default ApiExample