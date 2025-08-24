"""
파일 시스템 관련 MCP 도구들

실제 시스템 API (파일 시스템)와 상호작용하는 도구들을 구현합니다.
LLM → MCP Server → File System API
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


def list_files(directory: str = ".", show_hidden: bool = False) -> Dict[str, Any]:
    """
    디렉토리의 파일 목록을 반환
    
    Args:
        directory: 조회할 디렉토리 경로
        show_hidden: 숨김 파일 표시 여부
    
    Returns:
        파일 목록과 정보
    """
    try:
        path = Path(directory)
        if not path.exists():
            return {
                "success": False,
                "error": f"디렉토리가 존재하지 않습니다: {directory}"
            }
        
        if not path.is_dir():
            return {
                "success": False,
                "error": f"파일입니다, 디렉토리가 아닙니다: {directory}"
            }
        
        files = []
        directories = []
        
        for item in path.iterdir():
            # 숨김 파일 처리
            if not show_hidden and item.name.startswith('.'):
                continue
            
            item_info = {
                "name": item.name,
                "path": str(item),
                "size": item.stat().st_size if item.is_file() else None,
                "modified": item.stat().st_mtime
            }
            
            if item.is_file():
                files.append(item_info)
            elif item.is_dir():
                directories.append(item_info)
        
        return {
            "success": True,
            "directory": str(path.absolute()),
            "files": files,
            "directories": directories,
            "total_files": len(files),
            "total_directories": len(directories)
        }
        
    except Exception as e:
        logger.error(f"파일 목록 조회 실패: {str(e)}")
        return {
            "success": False,
            "error": f"파일 목록 조회 중 오류 발생: {str(e)}"
        }


def read_file(file_path: str, encoding: str = "utf-8") -> Dict[str, Any]:
    """
    파일 내용을 읽어서 반환
    
    Args:
        file_path: 읽을 파일 경로
        encoding: 파일 인코딩
    
    Returns:
        파일 내용
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return {
                "success": False,
                "error": f"파일이 존재하지 않습니다: {file_path}"
            }
        
        if not path.is_file():
            return {
                "success": False,
                "error": f"디렉토리입니다, 파일이 아닙니다: {file_path}"
            }
        
        # 파일 크기 체크 (너무 큰 파일은 읽지 않음)
        file_size = path.stat().st_size
        if file_size > 1024 * 1024:  # 1MB 제한
            return {
                "success": False,
                "error": f"파일이 너무 큽니다 (1MB 초과): {file_size} bytes"
            }
        
        with open(path, 'r', encoding=encoding) as f:
            content = f.read()
        
        return {
            "success": True,
            "file_path": str(path.absolute()),
            "content": content,
            "size": file_size,
            "encoding": encoding
        }
        
    except UnicodeDecodeError:
        return {
            "success": False,
            "error": f"파일 인코딩 오류: {encoding}로 읽을 수 없습니다"
        }
    except Exception as e:
        logger.error(f"파일 읽기 실패: {str(e)}")
        return {
            "success": False,
            "error": f"파일 읽기 중 오류 발생: {str(e)}"
        }


def write_file(file_path: str, content: str, encoding: str = "utf-8", overwrite: bool = False) -> Dict[str, Any]:
    """
    파일에 내용을 작성
    
    Args:
        file_path: 작성할 파일 경로
        content: 파일 내용
        encoding: 파일 인코딩
        overwrite: 기존 파일 덮어쓰기 허용 여부
    
    Returns:
        작성 결과
    """
    try:
        path = Path(file_path)
        
        # 기존 파일 존재 확인
        if path.exists() and not overwrite:
            return {
                "success": False,
                "error": f"파일이 이미 존재합니다. overwrite=True로 설정하세요: {file_path}"
            }
        
        # 디렉토리 생성
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, 'w', encoding=encoding) as f:
            f.write(content)
        
        return {
            "success": True,
            "file_path": str(path.absolute()),
            "content_length": len(content),
            "encoding": encoding,
            "overwritten": path.exists()
        }
        
    except Exception as e:
        logger.error(f"파일 쓰기 실패: {str(e)}")
        return {
            "success": False,
            "error": f"파일 쓰기 중 오류 발생: {str(e)}"
        }


def create_directory(directory_path: str, parents: bool = True) -> Dict[str, Any]:
    """
    디렉토리 생성
    
    Args:
        directory_path: 생성할 디렉토리 경로
        parents: 상위 디렉토리도 함께 생성할지 여부
    
    Returns:
        생성 결과
    """
    try:
        path = Path(directory_path)
        
        if path.exists():
            if path.is_dir():
                return {
                    "success": True,
                    "message": f"디렉토리가 이미 존재합니다: {directory_path}",
                    "directory_path": str(path.absolute())
                }
            else:
                return {
                    "success": False,
                    "error": f"같은 이름의 파일이 존재합니다: {directory_path}"
                }
        
        path.mkdir(parents=parents, exist_ok=True)
        
        return {
            "success": True,
            "directory_path": str(path.absolute()),
            "created": True
        }
        
    except Exception as e:
        logger.error(f"디렉토리 생성 실패: {str(e)}")
        return {
            "success": False,
            "error": f"디렉토리 생성 중 오류 발생: {str(e)}"
        }


def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    파일/디렉토리 정보 조회
    
    Args:
        file_path: 조회할 파일/디렉토리 경로
    
    Returns:
        파일/디렉토리 정보
    """
    try:
        path = Path(file_path)
        
        if not path.exists():
            return {
                "success": False,
                "error": f"파일 또는 디렉토리가 존재하지 않습니다: {file_path}"
            }
        
        stat = path.stat()
        
        info = {
            "success": True,
            "path": str(path.absolute()),
            "name": path.name,
            "type": "file" if path.is_file() else "directory",
            "size": stat.st_size,
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
            "accessed": stat.st_atime,
            "permissions": oct(stat.st_mode)[-3:]
        }
        
        if path.is_file():
            info["extension"] = path.suffix
        
        return info
        
    except Exception as e:
        logger.error(f"파일 정보 조회 실패: {str(e)}")
        return {
            "success": False,
            "error": f"파일 정보 조회 중 오류 발생: {str(e)}"
        }


# MCP 도구 정의들
FILE_SYSTEM_TOOLS = [
    {
        "name": "list_files",
        "description": "디렉토리의 파일과 폴더 목록을 조회합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "조회할 디렉토리 경로 (기본값: 현재 디렉토리)",
                    "default": "."
                },
                "show_hidden": {
                    "type": "boolean",
                    "description": "숨김 파일 표시 여부",
                    "default": False
                }
            },
            "required": []
        },
        "function": list_files
    },
    {
        "name": "read_file",
        "description": "파일의 내용을 읽어서 반환합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "읽을 파일의 경로"
                },
                "encoding": {
                    "type": "string",
                    "description": "파일 인코딩 (기본값: utf-8)",
                    "default": "utf-8"
                }
            },
            "required": ["file_path"]
        },
        "function": read_file
    },
    {
        "name": "write_file",
        "description": "파일에 내용을 작성합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "작성할 파일의 경로"
                },
                "content": {
                    "type": "string",
                    "description": "파일에 작성할 내용"
                },
                "encoding": {
                    "type": "string",
                    "description": "파일 인코딩 (기본값: utf-8)",
                    "default": "utf-8"
                },
                "overwrite": {
                    "type": "boolean",
                    "description": "기존 파일 덮어쓰기 허용 여부",
                    "default": False
                }
            },
            "required": ["file_path", "content"]
        },
        "function": write_file
    },
    {
        "name": "create_directory",
        "description": "새 디렉토리를 생성합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "directory_path": {
                    "type": "string",
                    "description": "생성할 디렉토리 경로"
                },
                "parents": {
                    "type": "boolean",
                    "description": "상위 디렉토리도 함께 생성할지 여부",
                    "default": True
                }
            },
            "required": ["directory_path"]
        },
        "function": create_directory
    },
    {
        "name": "get_file_info",
        "description": "파일 또는 디렉토리의 상세 정보를 조회합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "조회할 파일 또는 디렉토리 경로"
                }
            },
            "required": ["file_path"]
        },
        "function": get_file_info
    }
]


if __name__ == "__main__":
    # 파일 시스템 도구 테스트
    print("=== 파일 시스템 도구 테스트 ===")
    
    # 1. 현재 디렉토리 파일 목록
    print("\n1. 현재 디렉토리 파일 목록:")
    result = list_files(".")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 2. 테스트 파일 생성
    print("\n2. 테스트 파일 생성:")
    result = write_file("test_mcp.txt", "안녕하세요! MCP 테스트 파일입니다.", overwrite=True)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 3. 파일 읽기
    print("\n3. 파일 읽기:")
    result = read_file("test_mcp.txt")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 4. 파일 정보 조회
    print("\n4. 파일 정보 조회:")
    result = get_file_info("test_mcp.txt")
    print(json.dumps(result, ensure_ascii=False, indent=2))