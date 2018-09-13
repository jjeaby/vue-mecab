#FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 18080 --host 0.0.0.0
cd frontend
npm run build
cd ..
FLASK_APP=run.py flask run --port 18080 --host 0.0.0.0
