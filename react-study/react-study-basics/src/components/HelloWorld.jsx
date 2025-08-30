// JSX 기본 문법 학습을 위한 컴포넌트

function HelloWorld() {
    // JSX는 JavaScript XML의 줄임말로, HTML과 비슷한 문법을 사용합니다
    // 하지만 실제로는 JavaScript 객체로 변환됩니다

    const name = "React 스터디";
    const isLearning = true;
    const topics = ["JSX", "Props", "State", "Hooks"];

    return (
        <div className="hello-world">
            {/* JSX 주석은 이렇게 작성합니다 */}

            {/* 1. JSX에서 JavaScript 표현식 사용하기 - 중괄호 {} 사용 */}
            <h2>안녕하세요, {name}!</h2>

            {/* 2. 조건부 렌더링 - 삼항 연산자 사용 */}
            <p>
                현재 상태: {isLearning ? "학습 중 📚" : "휴식 중 😴"}
            </p>

            {/* 3. 조건부 렌더링 - && 연산자 사용 */}
            {isLearning && (
                <div className="learning-status">
                    <p>열심히 공부하고 있어요! 💪</p>
                </div>
            )}

            {/* 4. 리스트 렌더링 - map 함수 사용 */}
            <div className="topics">
                <h3>학습 주제들:</h3>
                <ul>
                    {topics.map((topic, index) => (
                        // key prop은 React가 리스트 아이템을 효율적으로 업데이트하기 위해 필요합니다
                        <li key={index} className="topic-item">
                            {index + 1}. {topic}
                        </li>
                    ))}
                </ul>
            </div>

            {/* 5. JSX에서 스타일 적용하기 */}
            <div
                style={{
                    backgroundColor: "#f0f8ff",
                    padding: "1rem",
                    borderRadius: "8px",
                    marginTop: "1rem"
                }}
            >
                <p>이 박스는 인라인 스타일로 꾸며졌어요!</p>
                <p>JSX에서는 style 속성에 객체를 전달합니다.</p>
            </div>

            {/* 6. HTML 속성명의 차이점 */}
            <div className="note">
                <p><strong>주의사항:</strong></p>
                <ul>
                    <li>HTML의 'class' → JSX의 'className'</li>
                    <li>HTML의 'for' → JSX의 'htmlFor'</li>
                    <li>카멜케이스 사용: onClick, onChange 등</li>
                </ul>
            </div>
        </div>
    );
}

export default HelloWorld;