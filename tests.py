import pytest
import requests

# CRUD
# Comando para rodar o pytest
# Terminal: pytest nome_do_arquivo.py - v

base_url = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{base_url}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.requests.post(f"{base_url}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "totoal_tasks" in response_json

def test_get_task():
    task_id = tasks[0]
    response = requests.get(f"{base_url}/tasks/{task_id}")
    assert response.status_code == 200
    response_json = response.json()
    assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Titulo atualizado"
        }
        response = requests.put(f"{base_url}/tasks/{task_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        # Nova requisição a tarefa específica
        response = requests.get(f"{base_url}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == payload['title']
        assert response_json['description'] == payload['description']
        assert response_json['completed'] == payload['completed']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{base_url}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f"{base_url}/tasks/{task_id}")
        assert response.status_code == 404
