from fastapi_app import app
import pytest
from fastapi.testclient import TestClient

test_cases = [
    ("SELECT experience_level, avg(salary_in_usd) AS avg_salary_usd FROM salaries GROUP BY experience_level", {"result":[["EX",199392.03846153847],["MI",87996.05633802817],["EN",61643.318181818184],["SE",138617.29285714286]]})
]

client = TestClient(app)

def test_fastapi_app():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Databricks"}

def test_sql():
    response = client.get("/query")
    assert response.status_code == 200
    assert response.json() == {"result":[["EX",199392.03846153847],["MI",87996.05633802817],["EN",61643.318181818184],["SE",138617.29285714286]]}