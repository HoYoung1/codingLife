// 리스트 렌더링과 key props 학습을 위한 컴포넌트

import { useState } from 'react'

function ListRender() {
  // 다양한 리스트 데이터
  const [todos, setTodos] = useState([
    { id: 1, text: "React 기초 학습하기", completed: false, priority: "high" },
    { id: 2, text: "JSX 문법 익히기", completed: true, priority: "medium" },
    { id: 3, text: "Props 사용법 배우기", completed: true, priority: "high" },
    { id: 4, text: "State 관리 학습하기", completed: false, priority: "low" }
  ])

  const [newTodo, setNewTodo] = useState("")
  const [filter, setFilter] = useState("all") // "all", "completed", "active"
  const [sortBy, setSortBy] = useState("id") // "id", "text", "priority"

  // 사용자 데이터
  const users = [
    { id: 1, name: "김철수", age: 25, city: "서울", skills: ["JavaScript", "React"] },
    { id: 2, name: "이영희", age: 30, city: "부산", skills: ["Python", "Django", "PostgreSQL"] },
    { id: 3, name: "박민수", age: 28, city: "대구", skills: ["Java", "Spring", "MySQL"] },
    { id: 4, name: "정수진", age: 26, city: "인천", skills: ["JavaScript", "Vue.js", "Node.js"] }
  ]

  // 카테고리별 제품 데이터
  const products = {
    electronics: [
      { id: 1, name: "노트북", price: 1200000 },
      { id: 2, name: "스마트폰", price: 800000 },
      { id: 3, name: "태블릿", price: 600000 }
    ],
    books: [
      { id: 4, name: "React 완벽 가이드", price: 35000 },
      { id: 5, name: "JavaScript 딥다이브", price: 45000 },
      { id: 6, name: "클린 코드", price: 30000 }
    ],
    clothing: [
      { id: 7, name: "티셔츠", price: 25000 },
      { id: 8, name: "청바지", price: 80000 },
      { id: 9, name: "운동화", price: 120000 }
    ]
  }

  // Todo 추가
  const addTodo = () => {
    if (newTodo.trim()) {
      const newId = Math.max(...todos.map(t => t.id)) + 1
      setTodos([...todos, {
        id: newId,
        text: newTodo,
        completed: false,
        priority: "medium"
      }])
      setNewTodo("")
    }
  }

  // Todo 완료 상태 토글
  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ))
  }

  // Todo 삭제
  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id))
  }

  // Todo 필터링
  const getFilteredTodos = () => {
    let filtered = todos
    
    // 필터 적용
    if (filter === "completed") {
      filtered = filtered.filter(todo => todo.completed)
    } else if (filter === "active") {
      filtered = filtered.filter(todo => !todo.completed)
    }
    
    // 정렬 적용
    filtered.sort((a, b) => {
      if (sortBy === "text") {
        return a.text.localeCompare(b.text)
      } else if (sortBy === "priority") {
        const priorityOrder = { high: 3, medium: 2, low: 1 }
        return priorityOrder[b.priority] - priorityOrder[a.priority]
      }
      return a.id - b.id
    })
    
    return filtered
  }

  return (
    <div className="list-render">
      <h2>리스트 렌더링과 key props 학습</h2>

      {/* 1. 기본 리스트 렌더링 */}
      <div className="section">
        <h3>1. 기본 리스트 렌더링</h3>
        <p>간단한 배열을 map 함수로 렌더링:</p>
        
        <div className="simple-list">
          {["사과", "바나나", "오렌지", "포도"].map((fruit, index) => (
            <div key={index} className="fruit-item">
              {index + 1}. {fruit}
            </div>
          ))}
        </div>
        
        <div className="warning">
          ⚠️ 위 예제는 index를 key로 사용했지만, 실제로는 고유한 id를 사용하는 것이 좋습니다!
        </div>
      </div>

      {/* 2. 객체 배열 렌더링 */}
      <div className="section">
        <h3>2. 객체 배열 렌더링</h3>
        <div className="user-grid">
          {users.map(user => (
            <div key={user.id} className="user-card">
              <h4>{user.name}</h4>
              <p>나이: {user.age}세</p>
              <p>지역: {user.city}</p>
              <div className="skills">
                <strong>기술:</strong>
                {user.skills.map((skill, index) => (
                  <span key={skill} className="skill-tag">
                    {skill}
                    {index < user.skills.length - 1 && ", "}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 3. 중첩된 리스트 렌더링 */}
      <div className="section">
        <h3>3. 중첩된 리스트 렌더링 (카테고리별 제품)</h3>
        {Object.entries(products).map(([category, items]) => (
          <div key={category} className="category">
            <h4>{category === 'electronics' ? '전자제품' : 
                 category === 'books' ? '도서' : '의류'}</h4>
            <div className="product-list">
              {items.map(product => (
                <div key={product.id} className="product-item">
                  <span className="product-name">{product.name}</span>
                  <span className="product-price">
                    {product.price.toLocaleString()}원
                  </span>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* 4. 동적 리스트 (Todo 앱) */}
      <div className="section">
        <h3>4. 동적 리스트 관리 (Todo 앱)</h3>
        
        {/* Todo 추가 */}
        <div className="todo-input">
          <input
            type="text"
            value={newTodo}
            onChange={(e) => setNewTodo(e.target.value)}
            placeholder="새로운 할일을 입력하세요"
            onKeyPress={(e) => e.key === 'Enter' && addTodo()}
          />
          <button onClick={addTodo}>추가</button>
        </div>

        {/* 필터와 정렬 */}
        <div className="todo-controls">
          <div className="filter-controls">
            <label>필터: </label>
            <select value={filter} onChange={(e) => setFilter(e.target.value)}>
              <option value="all">전체</option>
              <option value="active">미완료</option>
              <option value="completed">완료</option>
            </select>
          </div>
          
          <div className="sort-controls">
            <label>정렬: </label>
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
              <option value="id">추가순</option>
              <option value="text">이름순</option>
              <option value="priority">우선순위</option>
            </select>
          </div>
        </div>

        {/* Todo 리스트 */}
        <div className="todo-list">
          {getFilteredTodos().length === 0 ? (
            <p className="empty-message">표시할 할일이 없습니다.</p>
          ) : (
            getFilteredTodos().map(todo => (
              <div 
                key={todo.id} 
                className={`todo-item ${todo.completed ? 'completed' : ''}`}
              >
                <input
                  type="checkbox"
                  checked={todo.completed}
                  onChange={() => toggleTodo(todo.id)}
                />
                <span className="todo-text">{todo.text}</span>
                <span className={`priority priority-${todo.priority}`}>
                  {todo.priority}
                </span>
                <button 
                  onClick={() => deleteTodo(todo.id)}
                  className="delete-btn"
                >
                  삭제
                </button>
              </div>
            ))
          )}
        </div>

        <div className="todo-stats">
          <p>전체: {todos.length}개</p>
          <p>완료: {todos.filter(t => t.completed).length}개</p>
          <p>미완료: {todos.filter(t => !t.completed).length}개</p>
        </div>
      </div>

      {/* 5. 조건부 리스트 렌더링 */}
      <div className="section">
        <h3>5. 조건부 리스트 렌더링</h3>
        <div className="conditional-lists">
          {/* 완료된 할일만 표시 */}
          <div className="completed-todos">
            <h4>✅ 완료된 할일</h4>
            {todos.filter(todo => todo.completed).length > 0 ? (
              <ul>
                {todos
                  .filter(todo => todo.completed)
                  .map(todo => (
                    <li key={`completed-${todo.id}`}>{todo.text}</li>
                  ))
                }
              </ul>
            ) : (
              <p>완료된 할일이 없습니다.</p>
            )}
          </div>

          {/* 높은 우선순위 할일만 표시 */}
          <div className="high-priority-todos">
            <h4>🔥 높은 우선순위 할일</h4>
            {todos.filter(todo => todo.priority === 'high').length > 0 ? (
              <ul>
                {todos
                  .filter(todo => todo.priority === 'high')
                  .map(todo => (
                    <li key={`high-${todo.id}`} className={todo.completed ? 'completed' : ''}>
                      {todo.text}
                    </li>
                  ))
                }
              </ul>
            ) : (
              <p>높은 우선순위 할일이 없습니다.</p>
            )}
          </div>
        </div>
      </div>

      {/* 리스트 렌더링 팁 */}
      <div className="section tips">
        <h3>💡 리스트 렌더링 팁</h3>
        <ul>
          <li><strong>key props</strong>: 각 리스트 아이템에 고유한 key 제공 (가능하면 id 사용)</li>
          <li><strong>map 함수</strong>: 배열을 JSX 요소로 변환</li>
          <li><strong>filter + map</strong>: 조건에 맞는 아이템만 렌더링</li>
          <li><strong>sort</strong>: 렌더링 전에 배열 정렬</li>
          <li><strong>빈 리스트 처리</strong>: 리스트가 비어있을 때의 UI 고려</li>
          <li><strong>성능 최적화</strong>: 큰 리스트의 경우 가상화 고려</li>
        </ul>
      </div>
    </div>
  )
}

export default ListRender