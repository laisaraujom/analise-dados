# analise-dados
Projeto desenvolvido no módulo de POO - Programação Orientada a Objetos

Enunciado:

### 📊 Projeto 8: Análise de Dados

Crie um sistema que analise os dados contidos no arquivo [lista_clientes.csv](/aula12/lista_clientes.csv) e, usando POO, implemente as seguintes _features_:

1. Normalização dos dados

    | Campo | Regras e validações|
    | ----- | ------------------ |
    | **Nome**        | • Extraia o **nome completo**, **primeiro nome** e **segundo nome**.<br>• Os nomes devem estar registrado em “Camel Case”, com preposições (“da”, “de”, “do”, “das”, “dos”, “e”), que devem estar em minúsculo. |
    | **Gênero**      | • Inferir pelo **primeiro nome**.<br>• Disponibilize **3 estratégias** de API: `genderize.io`, `genderapi.io`, `gender-api.com`.<br>• O usuário escolhe qual API usar em tempo de execução.<br>• Caso a API exija token, leia‐o de variável de ambiente (_pesquise sobre isso_). |
    | **Celular**     | • Formato final: `"DD 9XXXXXXXX"`.<br>• Se faltar **DDD**, infira‐o pelo **CEP** (dica: utilize o serviço ViaCEP).<br>• Se o dígito **9** estiver ausente, adicione-o.<br>• Campo vazio → adicionar nota em `observacoes`.<br>• Número inválido → adicionar nota em `observacoes`. |
    | **CPF**         | • Formato final: apenas dígitos (`XXXXXXXXXXX`).<br>• Valide dígitos verificadores; CPF inválido → nota em `observacoes`.  |
    | **CEP**         | • Formato final: apenas dígitos (`XXXXXXXX`).<br>• Use ViaCEP (ou equivalente) para obter **Bairro, Cidade, Estado**. |
    | **Observações** | • Liste problemas detectados (ex.: “CPF inválido”, “telefone ausente”). |

2. Arquivo de saída (`.json`)

    O arquivo de saída será em formato '.json' e deve conter uma lista de usuários, organizados por **ordem alfabética**, seguindo o modelo a seguir:

    ```json
    {
      "users":
        [
          {
            "nome_completo": "André de Bifur Gomes Ribeiro",
            "primeiro_nome": "André",
            "segundo_nome": "de Bifur",
            "genero": "male",
            "email": "andrebifur@testmail.org",
            "celular": "51 952127281",
            "interesse": "Desenvolvimento de Jogos Digitais",
            "cpf": "94097729828",
            "bairro": "Petrópolis",
            "cidade": "Porto Alegre",
            "estado": "RS",
            "observacoes": "CPF Inválido"
          },
          ...
        ]
    }
    ```

3. Relatório de saída

    Além do arquivo de saída, exiba no console uma análise dos dados processados, informando:

    - Distribuição de gênero: % de homens e mulheres
    - Distribuição geográfica: % por região
    - Qualidades dos dados: CPFs inválidos, números de telefones ausentes...
    - Percentual das áreas de interesse (geral)
    - Quais áreas de intersse são mais desejadas por homens e mulheres (percentual)

4. Estrutura

    ```text
    analise_dados/
    │
    ├── src/                        # Código-fonte da aplicação
    │   ├── models/                 # Classes que representam entidades de negócio
    │   │   ├── pessoa.py
    │   │   ├── endereco.py
    │   │   └── cpf.py
    │   ├── services/               # Regras de negócio que dependem de recursos externos
    │   │   ├── gender_service.py
    │   │   └── cpf_service.py
    │   ├── repo/                   # Funções responsáveis por ler/gravar dados
    │   │   ├── csv_repo.py
    │   │   └── json_repo.py
    │   └── main.py
    │
    ├── tests/                      # Testes unitários
    │   ├── test_cpf_service.py
    │   ├── test_phone_service.py
    │   ├── test_gender_service.py
    │   └── ...
    └── README.md
    ```

