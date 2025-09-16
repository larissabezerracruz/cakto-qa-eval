import json
import requests
from behave import given, when, then

BASE_URL = "https://cakto-qa-eval.launchify.com.br"

# ---------------------------
# Given
# ---------------------------
@given("que a API está disponível")
def step_impl(context):
    context.base_url = BASE_URL

# ---------------------------
# When
# ---------------------------
@when('eu faço uma requisição GET para "{endpoint}"')
def step_impl(context, endpoint):
    context.response = requests.get(f"{context.base_url}{endpoint}")

@when('eu envio uma requisição POST para "{endpoint}" com body:')
def step_impl(context, endpoint):
    payload = json.loads(context.text)
    context.response = requests.post(f"{context.base_url}{endpoint}", json=payload)
    context.payload = payload

# ---------------------------
# Then
# ---------------------------
@then("a resposta deve ter status 200")
def step_impl(context):
    assert context.response.status_code == 200, f"Esperado 200, obtido {context.response.status_code}"

@then("a resposta deve ter status 201")
def step_impl(context):
    assert context.response.status_code == 201, f"Esperado 201, obtido {context.response.status_code}"

@then("a lista de usuários deve estar presente no JSON")
def step_impl(context):
    body = context.response.json()
    assert "data" in body
    assert isinstance(body["data"], list)

@then("todos os usuários devem ter age como número")
def step_impl(context):
    body = context.response.json()
    for user in body["data"]:
        assert isinstance(user["age"], int), f"Campo 'age' incorreto: {user['age']}"

@then("os dados do usuário retornado devem estar corretos")
def step_impl(context):
    data = context.response.json()["data"]
    assert data["name"] == context.payload["name"]
    assert data["email"] == context.payload["email"]
    assert data["age"] == context.payload["age"]
    assert data["status"] == context.payload["status"]

@then("a resposta deve ter status 400")
def step_impl(context):
    assert context.response.status_code == 400, f"Esperado 400, obtido {context.response.status_code}"

@then("a mensagem de erro deve indicar email duplicado")
def step_impl(context):
    data = context.response.json()
    assert "error" in data, f"Esperado erro de email duplicado, obtido: {data}"
    assert "duplicate" in data["error"].lower(), f"Esperado mensagem de email duplicado, obtido: {data['error']}"