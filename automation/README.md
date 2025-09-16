# Automation - Users CRUD Tests

Este diretório contém os testes automatizados para os endpoints do recurso **Users** da API `cakto-qa-eval`, usando **Python + Behave** (BDD).

## Estrutura

automation/
└── UsersCRUDTests/
├── features/ # Arquivos .feature (cenários BDD)
│ ├── create_user.feature
│ └── list_users.feature
├── steps/ # Implementação dos steps
│ └── users_steps.py
├── requirements.txt # Dependências do Python
└── pytest.ini # Configurações

## Pré-requisitos

- Python 3.11+ instalado
- Virtualenv (opcional, mas recomendado)
- Bibliotecas Python listadas em `requirements.txt`

## Instalação

1. Criar e ativar virtualenv:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux / Mac

pip install -r requirements.txt

behave automation/UsersCRUDTests/features