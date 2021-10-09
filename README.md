# coin_hacktober_backend

How to use it
- Install [poetry](https://python-poetry.org/docs/)
- Active poetry
  `poetry shell`
- Install dependency
  `poetry install`
- Copy env_example to .env
  `COPY env_example app/.env`
- Change `API_KEY` , `API_SECRET` to key from binance api

- Run Project 
 `uvicorn app.main:app --reload`
  You will see on browser `http://localhost:8000/docs`
  
  
 - How to run test
  `pytest`
  
