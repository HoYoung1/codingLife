// 폼 상태 관리를 위한 useState 활용 예제

import { useState } from 'react'

function FormExample() {
  // 1. 개별 입력 필드 상태 관리
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const [age, setAge] = useState('')
  const [gender, setGender] = useState('')
  const [hobbies, setHobbies] = useState([])
  const [bio, setBio] = useState('')
  
  // 2. 폼 상태 관리
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [errors, setErrors] = useState({})
  const [submitMessage, setSubmitMessage] = useState('')

  // 3. 객체로 폼 데이터 관리하는 방법
  const [formData, setFormData] = useState({
    company: '',
    position: '',
    experience: '',
    skills: []
  })

  // 취미 목록
  const availableHobbies = ['독서', '영화감상', '운동', '게임', '요리', '여행', '음악감상', '그림그리기']
  const availableSkills = ['JavaScript', 'React', 'Node.js', 'Python', 'Java', 'Spring', 'MySQL', 'MongoDB']

  // 유효성 검사 함수
  const validateForm = () => {
    const newErrors = {}

    // 이름 검증
    if (!name.trim()) {
      newErrors.name = '이름을 입력해주세요'
    } else if (name.length < 2) {
      newErrors.name = '이름은 2글자 이상이어야 합니다'
    }

    // 이메일 검증
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!email) {
      newErrors.email = '이메일을 입력해주세요'
    } else if (!emailRegex.test(email)) {
      newErrors.email = '올바른 이메일 형식이 아닙니다'
    }

    // 비밀번호 검증
    if (!password) {
      newErrors.password = '비밀번호를 입력해주세요'
    } else if (password.length < 6) {
      newErrors.password = '비밀번호는 6글자 이상이어야 합니다'
    }

    // 비밀번호 확인
    if (password !== confirmPassword) {
      newErrors.confirmPassword = '비밀번호가 일치하지 않습니다'
    }

    // 나이 검증
    if (!age) {
      newErrors.age = '나이를 입력해주세요'
    } else if (isNaN(age) || age < 1 || age > 120) {
      newErrors.age = '올바른 나이를 입력해주세요 (1-120)'
    }

    return newErrors
  }

  // 취미 선택/해제 처리
  const handleHobbyChange = (hobby) => {
    setHobbies(prevHobbies => {
      if (prevHobbies.includes(hobby)) {
        // 이미 선택된 취미면 제거
        return prevHobbies.filter(h => h !== hobby)
      } else {
        // 새로운 취미 추가
        return [...prevHobbies, hobby]
      }
    })
  }

  // 객체 상태 업데이트 (회사 정보)
  const handleFormDataChange = (field, value) => {
    setFormData(prevData => ({
      ...prevData,  // 기존 데이터 유지 (불변성)
      [field]: value  // 특정 필드만 업데이트
    }))
  }

  // 스킬 선택/해제 처리 (객체 내 배열 상태)
  const handleSkillChange = (skill) => {
    setFormData(prevData => ({
      ...prevData,
      skills: prevData.skills.includes(skill)
        ? prevData.skills.filter(s => s !== skill)
        : [...prevData.skills, skill]
    }))
  }

  // 폼 제출 처리
  const handleSubmit = async (e) => {
    e.preventDefault()  // 기본 폼 제출 동작 방지
    
    // 유효성 검사
    const formErrors = validateForm()
    setErrors(formErrors)

    // 에러가 있으면 제출 중단
    if (Object.keys(formErrors).length > 0) {
      setSubmitMessage('입력 정보를 확인해주세요')
      return
    }

    // 제출 시작
    setIsSubmitting(true)
    setSubmitMessage('제출 중...')

    try {
      // 가짜 API 호출 시뮬레이션
      await new Promise(resolve => setTimeout(resolve, 2000))
      
      // 성공 처리
      setSubmitMessage('회원가입이 완료되었습니다! 🎉')
      
      // 폼 초기화 (선택사항)
      // resetForm()
      
    } catch (error) {
      setSubmitMessage('오류가 발생했습니다. 다시 시도해주세요.')
    } finally {
      setIsSubmitting(false)
    }
  }

  // 폼 초기화
  const resetForm = () => {
    setName('')
    setEmail('')
    setPassword('')
    setConfirmPassword('')
    setAge('')
    setGender('')
    setHobbies([])
    setBio('')
    setFormData({
      company: '',
      position: '',
      experience: '',
      skills: []
    })
    setErrors({})
    setSubmitMessage('')
  }

  return (
    <div className="form-example">
      <h2>폼 상태 관리 학습</h2>

      <form onSubmit={handleSubmit} className="study-form">
        
        {/* 기본 정보 섹션 */}
        <div className="form-section">
          <h3>기본 정보</h3>
          
          {/* 텍스트 입력 */}
          <div className="form-group">
            <label>이름 *</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="이름을 입력하세요"
              className={errors.name ? 'error' : ''}
            />
            {errors.name && <span className="error-message">{errors.name}</span>}
          </div>

          {/* 이메일 입력 */}
          <div className="form-group">
            <label>이메일 *</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="example@email.com"
              className={errors.email ? 'error' : ''}
            />
            {errors.email && <span className="error-message">{errors.email}</span>}
          </div>

          {/* 비밀번호 입력 */}
          <div className="form-group">
            <label>비밀번호 *</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="6글자 이상 입력"
              className={errors.password ? 'error' : ''}
            />
            {errors.password && <span className="error-message">{errors.password}</span>}
          </div>

          {/* 비밀번호 확인 */}
          <div className="form-group">
            <label>비밀번호 확인 *</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              placeholder="비밀번호를 다시 입력"
              className={errors.confirmPassword ? 'error' : ''}
            />
            {errors.confirmPassword && <span className="error-message">{errors.confirmPassword}</span>}
          </div>

          {/* 숫자 입력 */}
          <div className="form-group">
            <label>나이 *</label>
            <input
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              placeholder="나이를 입력하세요"
              min="1"
              max="120"
              className={errors.age ? 'error' : ''}
            />
            {errors.age && <span className="error-message">{errors.age}</span>}
          </div>

          {/* 라디오 버튼 (단일 선택) */}
          <div className="form-group">
            <label>성별</label>
            <div className="radio-group">
              <label className="radio-label">
                <input
                  type="radio"
                  value="male"
                  checked={gender === 'male'}
                  onChange={(e) => setGender(e.target.value)}
                />
                남성
              </label>
              <label className="radio-label">
                <input
                  type="radio"
                  value="female"
                  checked={gender === 'female'}
                  onChange={(e) => setGender(e.target.value)}
                />
                여성
              </label>
              <label className="radio-label">
                <input
                  type="radio"
                  value="other"
                  checked={gender === 'other'}
                  onChange={(e) => setGender(e.target.value)}
                />
                기타
              </label>
            </div>
          </div>

          {/* 체크박스 (다중 선택) */}
          <div className="form-group">
            <label>취미 (복수 선택 가능)</label>
            <div className="checkbox-group">
              {availableHobbies.map(hobby => (
                <label key={hobby} className="checkbox-label">
                  <input
                    type="checkbox"
                    checked={hobbies.includes(hobby)}
                    onChange={() => handleHobbyChange(hobby)}
                  />
                  {hobby}
                </label>
              ))}
            </div>
            <div className="selected-info">
              선택된 취미: {hobbies.length > 0 ? hobbies.join(', ') : '없음'}
            </div>
          </div>

          {/* 텍스트 영역 */}
          <div className="form-group">
            <label>자기소개</label>
            <textarea
              value={bio}
              onChange={(e) => setBio(e.target.value)}
              placeholder="자신을 소개해주세요"
              rows="4"
            />
            <div className="char-count">
              {bio.length}/500 글자
            </div>
          </div>
        </div>

        {/* 회사 정보 섹션 (객체 상태 관리 예제) */}
        <div className="form-section">
          <h3>회사 정보 (객체 상태 관리)</h3>
          
          <div className="form-group">
            <label>회사명</label>
            <input
              type="text"
              value={formData.company}
              onChange={(e) => handleFormDataChange('company', e.target.value)}
              placeholder="회사명을 입력하세요"
            />
          </div>

          <div className="form-group">
            <label>직책</label>
            <select
              value={formData.position}
              onChange={(e) => handleFormDataChange('position', e.target.value)}
            >
              <option value="">선택하세요</option>
              <option value="frontend">프론트엔드 개발자</option>
              <option value="backend">백엔드 개발자</option>
              <option value="fullstack">풀스택 개발자</option>
              <option value="designer">디자이너</option>
              <option value="pm">프로젝트 매니저</option>
            </select>
          </div>

          <div className="form-group">
            <label>경력</label>
            <select
              value={formData.experience}
              onChange={(e) => handleFormDataChange('experience', e.target.value)}
            >
              <option value="">선택하세요</option>
              <option value="junior">신입 (0-2년)</option>
              <option value="mid">중급 (3-5년)</option>
              <option value="senior">시니어 (6년 이상)</option>
            </select>
          </div>

          <div className="form-group">
            <label>보유 기술</label>
            <div className="checkbox-group">
              {availableSkills.map(skill => (
                <label key={skill} className="checkbox-label">
                  <input
                    type="checkbox"
                    checked={formData.skills.includes(skill)}
                    onChange={() => handleSkillChange(skill)}
                  />
                  {skill}
                </label>
              ))}
            </div>
            <div className="selected-info">
              선택된 기술: {formData.skills.length > 0 ? formData.skills.join(', ') : '없음'}
            </div>
          </div>
        </div>

        {/* 제출 버튼 */}
        <div className="form-actions">
          <button 
            type="submit" 
            disabled={isSubmitting}
            className="submit-btn"
          >
            {isSubmitting ? '제출 중...' : '회원가입'}
          </button>
          <button 
            type="button" 
            onClick={resetForm}
            className="reset-btn"
          >
            초기화
          </button>
        </div>

        {/* 제출 메시지 */}
        {submitMessage && (
          <div className={`submit-message ${submitMessage.includes('완료') ? 'success' : 'info'}`}>
            {submitMessage}
          </div>
        )}
      </form>

      {/* 실시간 상태 표시 */}
      <div className="form-debug">
        <h3>🔍 실시간 폼 상태</h3>
        <pre>
{`개별 상태:
- name: "${name}"
- email: "${email}"
- age: "${age}"
- gender: "${gender}"
- hobbies: [${hobbies.map(h => `"${h}"`).join(', ')}]
- bio: "${bio.substring(0, 50)}${bio.length > 50 ? '...' : ''}"

객체 상태 (formData):
${JSON.stringify(formData, null, 2)}

폼 상태:
- isSubmitting: ${isSubmitting}
- errors: ${JSON.stringify(errors, null, 2)}
- submitMessage: "${submitMessage}"`}
        </pre>
      </div>

      {/* 폼 상태 관리 팁 */}
      <div className="tips-section">
        <h3>💡 폼 상태 관리 팁</h3>
        <div className="tips-grid">
          <div className="tip">
            <h4>1. 개별 상태 vs 객체 상태</h4>
            <p>간단한 폼: 개별 useState</p>
            <p>복잡한 폼: 객체로 관리</p>
          </div>
          <div className="tip">
            <h4>2. 불변성 유지</h4>
            <code>setState({`{...prev, field: value}`})</code>
          </div>
          <div className="tip">
            <h4>3. 유효성 검사</h4>
            <p>실시간 또는 제출 시 검증</p>
          </div>
          <div className="tip">
            <h4>4. 제어 컴포넌트</h4>
            <p>value와 onChange로 완전 제어</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default FormExample