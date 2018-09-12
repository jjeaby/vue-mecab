# vue-mecab project 
1. 실행 명령어
    * 8080 port 로 vuejs 가 구동된다.
```
./start.sh 
```
2. 상세 실행 방법 
```
# install front-end
cd frontend
npm install

# build for production/Flask with minification
npm run serve

# install back-end
pip install flask flask-cors

# serve back-end at localhost:8080
FLASK_APP=run.py flask run --port 8080 --host 0.0.0.0
```

### refer : https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532
