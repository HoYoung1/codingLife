// useState Hook 기본 사용법 학습을 위한 카운터 컴포넌트

import { useState } from 'react'

function CounterExample() {
  // useState Hook 사용법
  // useState(초기값)은 [현재상태, 상태변경함수]를 배열로 반환합니다
  const [count, setCount] = useState(0)
  
  // 여러 개의 상태를 독립적으로 관리할 수 있습니다
  const [step, setStep] = useState(1)
  const [message, setMessage] = useState("카운터를 시작해보세요!")

  // 상태 업데이트 함수들
  // React는 상태가 변경되면 컴포넌트를 다시 렌더링합니다
  
  const increment = () => {
    // 기본적인 상태 업데이트
    setCount(count + step)
    setMessage(`${step}만큼 증가했습니다!`)
  }

  const decrement = () => {
    setCount(count - step)
    setMessage(`${step}만큼 감소했습니다!`)
  }

  const reset = () => {
    setCount(0)
    setMessage("카운터가 초기화되었습니다!")
  }

  // 함수형 업데이트 - 이전 상태를 기반으로 새 상태 계산
  const incrementByFunction = () => {
    // 이 방법이 더 안전합니다 (특히 비동기 상황에서)
    setCount(prevCount => prevCount + step)
    setMessage("함수형 업데이트로 증가!")
  }

  // 복잡한 상태 업데이트 예제
  const doubleCount = () => {
    setCount(prevCount => prevCount * 2)
    setMessage("카운터가 2배가 되었습니다!")
  }

  const randomCount = () => {
    const randomValue = Math.floor(Math.random() * 100)
    setCount(randomValue)
    setMessage(`랜덤 값 ${randomValue}으로 설정!`)
  }

  // 조건부 상태 업데이트
  const smartIncrement = () => {
    if (count < 100) {
      setCount(prevCount => prevCount + step)
      setMessage("정상적으로 증가!")
    } else {
      setMessage("100을 초과할 수 없습니다!")
    }
  }

  return (
    <div className="counter-example">
      <h2>useState Hook 기본 사용법</h2>
      
      {/* 현재 상태 표시 */}
      <div className="counter-display">
        <div className="count-value">
          현재 카운트: <span className="count-number">{count}</span>
        </div>
        <div className="message">
          {message}
        </div>
      </div>

      {/* 스텝 설정 */}
      <div className="step-control">
        <label>증감 단위: </label>
        <input 
          type="number" 
          value={step} 
          onChange={(e) => {
            const newStep = parseInt(e.target.value) || 1
            setStep(newStep)
            setMessage(`증감 단위가 ${newStep}로 변경되었습니다!`)
          }}
          min="1"
          max="10"
        />
      </div>

      {/* 기본 버튼들 */}
      <div className="button-group">
        <h3>기본 상태 업데이트</h3>
        <button onClick={increment} className="btn-primary">
          +{step} 증가
        </button>
        <button onClick={decrement} className="btn-secondary">
          -{step} 감소
        </button>
        <button onClick={reset} className="btn-warning">
          초기화
        </button>
      </div>

      {/* 함수형 업데이트 */}
      <div className="button-group">
        <h3>함수형 업데이트 (권장)</h3>
        <button onClick={incrementByFunction} className="btn-success">
          함수형 +{step}
        </button>
        <button onClick={smartIncrement} className="btn-info">
          스마트 증가 (100 제한)
        </button>
      </div>

      {/* 특별한 업데이트들 */}
      <div className="button-group">
        <h3>특별한 업데이트</h3>
        <button onClick={doubleCount} className="btn-purple">
          2배로 만들기
        </button>
        <button onClick={randomCount} className="btn-orange">
          랜덤 값 (0-99)
        </button>
      </div>

      {/* 상태에 따른 조건부 렌더링 */}
      <div className="status-display">
        {count === 0 && (
          <div className="status zero">🎯 시작점입니다!</div>
        )}
        {count > 0 && count <= 10 && (
          <div className="status low">📈 좋은 시작이에요!</div>
        )}
        {count > 10 && count <= 50 && (
          <div className="status medium">🚀 잘하고 있어요!</div>
        )}
        {count > 50 && count < 100 && (
          <div className="status high">🔥 대단해요!</div>
        )}
        {count >= 100 && (
          <div className="status max">🏆 최고점 달성!</div>
        )}
        {count < 0 && (
          <div className="status negative">⚠️ 음수 영역입니다!</div>
        )}
      </div>

      {/* useState 사용 팁 */}
      <div className="tips-section">
        <h3>💡 useState 사용 팁</h3>
        <div className="tips-grid">
          <div className="tip">
            <h4>1. 구조 분해 할당</h4>
            <code>const [state, setState] = useState(초기값)</code>
          </div>
          <div className="tip">
            <h4>2. 함수형 업데이트</h4>
            <code>setState(prevState => prevState + 1)</code>
            <p>이전 상태를 기반으로 안전하게 업데이트</p>
          </div>
          <div className="tip">
            <h4>3. 여러 상태 관리</h4>
            <code>useState를 여러 번 호출해서 독립적인 상태 관리</code>
          </div>
          <div className="tip">
            <h4>4. 상태 불변성</h4>
            <code>객체나 배열은 새로운 객체/배열로 교체</code>
          </div>
        </div>
      </div>

      {/* 실시간 상태 정보 */}
      <div className="debug-info">
        <h4>🔍 실시간 상태 정보</h4>
        <pre>
{`현재 상태:
- count: ${count}
- step: ${step}
- message: "${message}"

렌더링 정보:
- 이 컴포넌트는 상태가 변경될 때마다 다시 렌더링됩니다
- useState는 상태 변경을 감지하고 리렌더링을 트리거합니다
- 각 상태는 독립적으로 관리됩니다`}
        </pre>
      </div>
    </div>
  )
}

export default CounterExample