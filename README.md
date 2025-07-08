# analise-dados
Projeto desenvolvido no módulo de POO - Programação Orientada a Objetos

Enunciado:

Crie um sistema que analise os dados contidos no arquivo lista_clientes.csv e, usando POO, implemente as seguintes features:

Normalização dos dados

Campo	Regras e validações
Nome	
• Extraia o nome completo, primeiro nome e segundo nome.
• Os nomes devem estar registrado em “Camel Case”, com preposições (“da”, “de”, “do”, “das”, “dos”, “e”), que devem estar em minúsculo.
Gênero	
• Inferir pelo primeiro nome.
• Disponibilize 3 estratégias de API: genderize.io, genderapi.io, gender-api.com.
• O usuário escolhe qual API usar em tempo de execução.
• Caso a API exija token, leia‐o de variável de ambiente (pesquise sobre isso).
Celular	
• Formato final: "DD 9XXXXXXXX".
• Se faltar DDD, infira‐o pelo CEP (dica: utilize o serviço ViaCEP).
• Se o dígito 9 estiver ausente, adicione-o.
• Campo vazio → adicionar nota em observacoes.
• Número inválido → adicionar nota em observacoes.
CPF	
• Formato final: apenas dígitos (XXXXXXXXXXX).
• Valide dígitos verificadores; CPF inválido → nota em observacoes.
CEP	
• Formato final: apenas dígitos (XXXXXXXX).
• Use ViaCEP (ou equivalente) para obter Bairro, Cidade, Estado.
Observações	
• Liste problemas detectados (ex.: “CPF inválido”, “telefone ausente”).
