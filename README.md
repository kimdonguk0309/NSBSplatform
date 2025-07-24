# NSBS: 탈중앙 네트워크 공유 플랫폼

## 실행 방법

```bash
# 1. 인증서 준비 (certbot 등으로 생성 후 backend/certs/ 에 복사)
# 2. 백엔드 실행
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000 --ssl-keyfile backend/certs/privkey.pem --ssl-certfile backend/certs/fullchain.pem

# 3. 프론트엔드 실행
streamlit run frontend/app.py \
    --server.port 8501 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --server.address 0.0.0.0 \
    --server.sslCertFile backend/certs/fullchain.pem \
    --server.sslKeyFile backend/certs/privkey.pem****


cd C:\Users\rlaxo\NSBSplatform
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000 ^
 --ssl-keyfile backend/certs/privkey.pem ^
 --ssl-certfile backend/certs/fullchain.pem
cd C:\Users\rlaxo\NSBSplatform\frontend

python -m streamlit run app.py ^
 --server.port 8501 ^
 --server.address 0.0.0.0 ^
 --server.enableCORS false ^
 --server.enableXsrfProtection false ^
 --server.enableWebsocketCompression false ^
 --server.sslCertFile ../backend/certs/fullchain.pem ^
 --server.sslKeyFile ../backend/certs/privkey.pem
