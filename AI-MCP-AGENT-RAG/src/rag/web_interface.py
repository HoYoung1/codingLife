"""
RAG 시스템 웹 인터페이스
"""

import os
import sys
from pathlib import Path
from typing import List, Optional
import logging

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.rag_system import RAGSystem

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI 앱 생성
app = FastAPI(
    title="RAG 시스템 웹 인터페이스",
    description="AI Agent, RAG, MCP 학습을 위한 웹 인터페이스 (로컬 모델 사용)",
    version="1.0.0"
)

# RAG 시스템 인스턴스
rag_system = None

# 데이터 모델
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    question: str
    answer: str
    relevant_documents: List[dict]

class DocumentInfo(BaseModel):
    total_documents: int
    collection_info: Optional[dict]

class UploadResponse(BaseModel):
    message: str
    uploaded_files: List[str]

# 정적 파일 서빙 (HTML, CSS, JS)
static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

# HTML 템플릿
html_template = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAG 시스템 - AI Agent 학습 (로컬 모델)</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        
        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }
        
        .system-info {
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: center;
            color: white;
        }
        
        .main-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
        }
        
        .card h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.5rem;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 10px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #555;
        }
        
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 12px;
            border: 2px solid #e1e5e9;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s ease;
        }
        
        .form-group input:focus,
        .form-group textarea:focus,
        .form-group select:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        
        .btn:hover {
            transform: translateY(-2px);
        }
        
        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            transform: none;
        }
        
        .results {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .results h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 1.5rem;
        }
        
        .question {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            border-left: 4px solid #667eea;
        }
        
        .answer {
            background: #e8f4fd;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #17a2b8;
        }
        
        .documents {
            background: #fff3cd;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #ffc107;
        }
        
        .document-item {
            background: white;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #dee2e6;
        }
        
        .loading {
            text-align: center;
            padding: 20px;
            color: #666;
        }
        
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #f5c6cb;
        }
        
        .success {
            background: #d4edda;
            color: #155724;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px solid #c3e6cb;
        }
        
        @media (max-width: 768px) {
            .main-content {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 RAG 시스템</h1>
            <p>AI Agent, RAG, MCP 학습을 위한 지능형 질의응답 시스템</p>
        </div>
        
        <div class="system-info">
            <strong>💡 시스템 정보:</strong> 
            Sentence Transformers (all-MiniLM-L6-v2) 임베딩 모델을 사용하여 
            로컬에서 무료로 실행됩니다. Ollama가 설치되어 있다면 고품질 LLM 답변도 가능합니다.
        </div>
        
        <div class="main-content">
            <!-- 문서 업로드 -->
            <div class="card">
                <h2>📚 문서 업로드</h2>
                <form id="uploadForm">
                    <div class="form-group">
                        <label for="files">문서 파일 선택 (PDF, DOCX, TXT, MD)</label>
                        <input type="file" id="files" name="files" multiple accept=".pdf,.docx,.txt,.md" required>
                    </div>
                    <button type="submit" class="btn">문서 업로드</button>
                </form>
                <div id="uploadStatus"></div>
            </div>
            
            <!-- 질의응답 -->
            <div class="card">
                <h2>🔍 질의응답</h2>
                <form id="queryForm">
                    <div class="form-group">
                        <label for="question">질문을 입력하세요</label>
                        <textarea id="question" name="question" rows="4" placeholder="예: AI 기술의 장점은 무엇인가요?" required></textarea>
                    </div>
                    <button type="submit" class="btn">질문하기</button>
                </form>
            </div>
        </div>
        
        <!-- 결과 표시 -->
        <div class="results" id="results" style="display: none;">
            <h2>📊 질의응답 결과</h2>
            <div id="queryResults"></div>
        </div>
        
        <!-- 시스템 정보 -->
        <div class="results">
            <h2>ℹ️ 시스템 정보</h2>
            <div id="systemInfo">
                <p>문서를 업로드하면 시스템 정보가 표시됩니다.</p>
            </div>
        </div>
    </div>

    <script>
        // 전역 변수
        let isProcessing = false;
        
        // DOM 요소
        const uploadForm = document.getElementById('uploadForm');
        const queryForm = document.getElementById('queryForm');
        const uploadStatus = document.getElementById('uploadStatus');
        const results = document.getElementById('results');
        const queryResults = document.getElementById('queryResults');
        const systemInfo = document.getElementById('systemInfo');
        
        // 문서 업로드
        uploadForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            if (isProcessing) return;
            isProcessing = true;
            
            const formData = new FormData();
            const files = document.getElementById('files').files;
            
            if (files.length === 0) {
                showMessage(uploadStatus, '파일을 선택해주세요.', 'error');
                isProcessing = false;
                return;
            }
            
            for (let file of files) {
                formData.append('files', file);
            }
            
            showMessage(uploadStatus, '문서를 업로드하고 처리 중입니다...', 'loading');
            
            try {
                const response = await fetch('/upload-documents', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    showMessage(uploadStatus, result.message, 'success');
                    updateSystemInfo();
                } else {
                    showMessage(uploadStatus, `오류: ${result.detail}`, 'error');
                }
            } catch (error) {
                showMessage(uploadStatus, `오류: ${error.message}`, 'error');
            } finally {
                isProcessing = false;
            }
        });
        
        // 질의응답
        queryForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            if (isProcessing) return;
            isProcessing = true;
            
            const question = document.getElementById('question').value.trim();
            
            if (!question) {
                isProcessing = false;
                return;
            }
            
            showMessage(queryResults, '질문을 처리하고 있습니다...', 'loading');
            results.style.display = 'block';
            
            try {
                const response = await fetch('/query', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ question: question })
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    displayQueryResult(result);
                } else {
                    showMessage(queryResults, `오류: ${result.detail}`, 'error');
                }
            } catch (error) {
                showMessage(queryResults, `오류: ${error.message}`, 'error');
            } finally {
                isProcessing = false;
            }
        });
        
        // 메시지 표시
        function showMessage(element, message, type) {
            element.innerHTML = `<div class="${type}">${message}</div>`;
        }
        
        // 질의응답 결과 표시
        function displayQueryResult(result) {
            let html = `
                <div class="question">
                    <strong>질문:</strong> ${result.question}
                </div>
                <div class="answer">
                    <strong>답변:</strong> ${result.answer}
                </div>
            `;
            
            if (result.relevant_documents && result.relevant_documents.length > 0) {
                html += `
                    <div class="documents">
                        <strong>관련 문서:</strong>
                        ${result.relevant_documents.map((doc, index) => `
                            <div class="document-item">
                                <strong>문서 ${index + 1}:</strong> ${doc.content}
                            </div>
                        `).join('')}
                    </div>
                `;
            }
            
            queryResults.innerHTML = html;
        }
        
        // 시스템 정보 업데이트
        async function updateSystemInfo() {
            try {
                const response = await fetch('/system-info');
                const result = await response.json();
                
                if (response.ok) {
                    systemInfo.innerHTML = `
                        <p><strong>총 문서 수:</strong> ${result.total_documents}개</p>
                        ${result.collection_info ? `<p><strong>컬렉션:</strong> ${result.collection_info.name}</p>` : ''}
                        <p><strong>모드:</strong> 로컬 임베딩 + 키워드 매칭 (또는 Ollama LLM)</p>
                    `;
                }
            } catch (error) {
                console.error('시스템 정보 업데이트 실패:', error);
            }
        }
        
        // 페이지 로드 시 시스템 정보 확인
        window.addEventListener('load', updateSystemInfo);
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def read_root():
    """메인 페이지"""
    return html_template

@app.post("/upload-documents", response_model=UploadResponse)
async def upload_documents(files: List[UploadFile] = File(...)):
    """문서 업로드 및 처리"""
    try:
        if not rag_system:
            raise HTTPException(status_code=500, detail="RAG 시스템이 초기화되지 않았습니다.")
        
        # 임시 파일 저장
        temp_dir = Path("temp_uploads")
        temp_dir.mkdir(exist_ok=True)
        
        uploaded_files = []
        
        for file in files:
            if file.filename:
                # 파일 확장자 검증
                allowed_extensions = {'.pdf', '.docx', '.txt', '.md'}
                file_ext = Path(file.filename).suffix.lower()
                
                if file_ext not in allowed_extensions:
                    continue
                
                # 파일 저장
                file_path = temp_dir / file.filename
                with open(file_path, "wb") as buffer:
                    content = await file.read()
                    buffer.write(content)
                
                uploaded_files.append(str(file_path))
        
        if not uploaded_files:
            raise HTTPException(status_code=400, detail="유효한 파일이 없습니다.")
        
        # RAG 시스템에 문서 추가
        success = rag_system.add_documents(uploaded_files)
        
        if not success:
            raise HTTPException(status_code=500, detail="문서 처리에 실패했습니다.")
        
        # 임시 파일 정리
        for file_path in uploaded_files:
            try:
                os.remove(file_path)
            except:
                pass
        
        return UploadResponse(
            message=f"{len(uploaded_files)}개 문서가 성공적으로 업로드되었습니다.",
            uploaded_files=[Path(f).name for f in uploaded_files]
        )
        
    except Exception as e:
        logger.error(f"문서 업로드 실패: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    """질의응답 수행"""
    try:
        if not rag_system:
            raise HTTPException(status_code=500, detail="RAG 시스템이 초기화되지 않았습니다.")
        
        result = rag_system.query(request.question)
        
        return QueryResponse(
            question=result["question"],
            answer=result["answer"],
            relevant_documents=result["relevant_documents"]
        )
        
    except Exception as e:
        logger.error(f"질의응답 실패: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system-info", response_model=DocumentInfo)
async def get_system_info():
    """시스템 정보 조회"""
    try:
        if not rag_system:
            return DocumentInfo(total_documents=0, collection_info=None)
        
        info = rag_system.get_document_info()
        return DocumentInfo(**info)
        
    except Exception as e:
        logger.error(f"시스템 정보 조회 실패: {str(e)}")
        return DocumentInfo(total_documents=0, collection_info=None)

@app.on_event("startup")
async def startup_event():
    """애플리케이션 시작 시 실행"""
    global rag_system
    
    try:
        # RAG 시스템 초기화 (Ollama 사용 시도)
        try:
            rag_system = RAGSystem(use_ollama=True, ollama_model="llama2")
            logger.info("RAG 시스템이 Ollama와 함께 성공적으로 초기화되었습니다.")
        except Exception as e:
            logger.warning(f"Ollama 연결 실패: {e}. 키워드 매칭 모드로 전환합니다.")
            rag_system = RAGSystem(use_ollama=False)
            logger.info("RAG 시스템이 키워드 매칭 모드로 초기화되었습니다.")
        
    except Exception as e:
        logger.error(f"RAG 시스템 초기화 실패: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
