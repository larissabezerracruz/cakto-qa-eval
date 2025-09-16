Feature: Criar usuário
  Como QA tester
  Quero criar usuários via POST /users
  Para validar que o endpoint funciona corretamente

  Scenario: Criar usuário válido
    Given que a API está disponível
    When eu envio uma requisição POST para "/users" com body:
      """
      {
        "name": "Larissa Bezerra da Cruz",
        "email": "larissasbezerra@outlook.com",
        "age": 30,
        "status": "active"
      }
      """
    Then a resposta deve ter status 201
    And os dados do usuário retornado devem estar corretos

    Scenario: Criar usuário com email duplicado
  Given que a API está disponível
  When eu envio uma requisição POST para "/users" com body:
    """
    {
      "name": "Helena Cruz",
      "email": "larissasbezerra@outlook.com",
      "age": 9,
      "status": "inactive"
    }
    """
  Then a resposta deve ter status 400
  And a mensagem de erro deve indicar email duplicado