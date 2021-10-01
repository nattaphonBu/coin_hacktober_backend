set -m
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES &
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
fg %3
