Feature: Listar usuários
  Como QA tester
  Quero buscar todos os usuários
  Para validar que o endpoint GET /users funciona corretamente

  Scenario: Buscar lista de usuários
    Given que a API está disponível
    When eu faço uma requisição GET para "/users"
    Then a resposta deve ter status 200
    And a lista de usuários deve estar presente no JSON