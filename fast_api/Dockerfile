# 베이스 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일들을 컨테이너에 복사
COPY main.py /app/main.py
COPY requirements.txt /app/requirements.txt

# 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# uvicorn을 사용하여 FastAPI 애플리케이션 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]