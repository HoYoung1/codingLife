// Props를 통한 데이터 전달 학습을 위한 컴포넌트

// 1. 기본적인 Props 사용법
function UserCard({ name, age, email, isOnline }) {
  return (
    <div className="user-card">
      <div className="user-info">
        <h3>{name}</h3>
        <p>나이: {age}세</p>
        <p>이메일: {email}</p>
        
        {/* Props를 사용한 조건부 렌더링 */}
        <div className={`status ${isOnline ? 'online' : 'offline'}`}>
          {isOnline ? '🟢 온라인' : '🔴 오프라인'}
        </div>
      </div>
    </div>
  );
}

// 2. 기본값(Default Props) 설정
function Greeting({ name = "익명", message = "안녕하세요!" }) {
  return (
    <div className="greeting">
      <h4>{message}</h4>
      <p>{name}님, 환영합니다!</p>
    </div>
  );
}

// 3. 객체 Props 사용법
function ProductCard({ product }) {
  return (
    <div className="product-card">
      <h4>{product.name}</h4>
      <p>가격: {product.price.toLocaleString()}원</p>
      <p>카테고리: {product.category}</p>
      <p>재고: {product.stock > 0 ? `${product.stock}개` : '품절'}</p>
    </div>
  );
}

// 4. 함수 Props (이벤트 핸들러)
function Button({ text, onClick, disabled = false, variant = "primary" }) {
  return (
    <button 
      onClick={onClick}
      disabled={disabled}
      className={`btn btn-${variant}`}
      style={{
        padding: "0.5rem 1rem",
        border: "none",
        borderRadius: "4px",
        cursor: disabled ? "not-allowed" : "pointer",
        backgroundColor: variant === "primary" ? "#007bff" : "#6c757d",
        color: "white",
        opacity: disabled ? 0.6 : 1
      }}
    >
      {text}
    </button>
  );
}

// 5. children Props 사용법
function Card({ title, children }) {
  return (
    <div className="card" style={{
      border: "1px solid #ddd",
      borderRadius: "8px",
      padding: "1rem",
      margin: "1rem 0"
    }}>
      {title && <h3 className="card-title">{title}</h3>}
      <div className="card-content">
        {children}
      </div>
    </div>
  );
}

// 메인 컴포넌트 - 모든 예제를 보여줍니다
function PropsExample() {
  // 예제 데이터
  const users = [
    { id: 1, name: "김철수", age: 25, email: "kim@example.com", isOnline: true },
    { id: 2, name: "이영희", age: 30, email: "lee@example.com", isOnline: false },
    { id: 3, name: "박민수", age: 28, email: "park@example.com", isOnline: true }
  ];

  const products = [
    { id: 1, name: "노트북", price: 1200000, category: "전자제품", stock: 5 },
    { id: 2, name: "마우스", price: 25000, category: "전자제품", stock: 0 },
    { id: 3, name: "키보드", price: 80000, category: "전자제품", stock: 3 }
  ];

  // 이벤트 핸들러 함수들
  const handleClick = (message) => {
    alert(message);
  };

  const handleUserClick = (userName) => {
    console.log(`${userName}님을 클릭했습니다!`);
  };

  return (
    <div className="props-example">
      <h2>Props 사용법 학습</h2>
      
      {/* 1. 기본 Props 사용 */}
      <Card title="1. 기본 Props 사용법">
        <div className="user-list">
          {users.map(user => (
            <div key={user.id} onClick={() => handleUserClick(user.name)}>
              <UserCard 
                name={user.name}
                age={user.age}
                email={user.email}
                isOnline={user.isOnline}
              />
            </div>
          ))}
        </div>
      </Card>

      {/* 2. 기본값 Props */}
      <Card title="2. 기본값(Default Props)">
        <Greeting />
        <Greeting name="홍길동" />
        <Greeting name="김개발" message="코딩 화이팅!" />
      </Card>

      {/* 3. 객체 Props */}
      <Card title="3. 객체 Props">
        <div className="product-list">
          {products.map(product => (
            <ProductCard key={product.id} product={product} />
          ))}
        </div>
      </Card>

      {/* 4. 함수 Props */}
      <Card title="4. 함수 Props (이벤트 핸들러)">
        <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
          <Button 
            text="기본 버튼" 
            onClick={() => handleClick("기본 버튼이 클릭되었습니다!")} 
          />
          <Button 
            text="보조 버튼" 
            variant="secondary"
            onClick={() => handleClick("보조 버튼이 클릭되었습니다!")} 
          />
          <Button 
            text="비활성 버튼" 
            disabled={true}
            onClick={() => handleClick("이 버튼은 클릭되지 않습니다!")} 
          />
        </div>
      </Card>

      {/* 5. children Props */}
      <Card title="5. children Props">
        <Card>
          <p>이 내용은 children으로 전달되었습니다.</p>
          <p>Card 컴포넌트 안에 어떤 내용이든 넣을 수 있어요!</p>
          <Button 
            text="children 안의 버튼" 
            onClick={() => handleClick("children 안의 버튼입니다!")} 
          />
        </Card>
      </Card>

      {/* Props 사용 팁 */}
      <Card title="💡 Props 사용 팁">
        <ul>
          <li><strong>구조 분해 할당</strong>: function Component({`{name, age}`}) 형태로 사용</li>
          <li><strong>기본값 설정</strong>: 매개변수에 기본값을 지정하거나 defaultProps 사용</li>
          <li><strong>Props 검증</strong>: PropTypes를 사용해 타입 검증 (선택사항)</li>
          <li><strong>불변성</strong>: Props는 읽기 전용이므로 직접 수정하면 안됨</li>
          <li><strong>함수 전달</strong>: 이벤트 핸들러를 Props로 전달해 자식에서 부모 상태 변경</li>
        </ul>
      </Card>
    </div>
  );
}

export default PropsExample; // 여기까지공부했음