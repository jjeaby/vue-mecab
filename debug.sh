cd frontend
npm run serve &
cd ..
FLASK_APP=run.py FLASK_DEBUG=1 flask run --port 18080 --host 0.0.0.0
