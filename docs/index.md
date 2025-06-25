# {{author}} SDK python

1. [Inicio rápido](#inicio-rapido)
    - [Instalação](#instalacao)
    - [Criando a sua primeira cobrança](#criando-sua-primeira-cobranca)
    - [Cadastrando o seu primeiro cliente](#criando-seu-primeiro-cliente)

2. [Sobre a {{ org_name }}](#sobre)
    - [Site oficial da AbacatePay](https://abacatepay.com)
    - [Documentação oficial da AbacatePay](https://docs.abacatepay.com/pages/introduction)
    - [Suporte](#sobre)
    

## Inicio rápido
/// admonition | Pré-requisitos.
- Ter sua conta da {{ org_name }} disponível para aceitar pagamentos, caso ainda não tenha você pode cria-la [aqui](https://www.abacatepay.com/login)
- Uma vez que sua contra estiver disponível você pode encontrar a sua chave de API [aqui](https://www.abacatepay.com/integrar)
{% include "templates/pre_requirements.md" %}
///

### Instalação
{% include "templates/installation.md" %}



### Criando sua primeira cobrança
```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>")  # (1)

billing = client.billing.create(
    products=[
        {
            "external_id": "123",
            "name": "PC gamer",
            "quantity": 1,
            "price": 1600_00, # (2)
            "description": "PC gamer completo de ultima geração"
        }
    ],
    return_url="https://mysite.com/return",  # (3)
    completion_url="https://mysite.com/completed",  # (4)
    customer={  # (5)
        "name": "John Doe",
        "email" "john@email.com",
        "cellphone": "(21) 5032-2583",
        "tax_id": "123.456.789-10"  # (6)
    },
    frequency='ONE_TIME',  # (7)
)
print(billing.url)
# > https://abacatepay.com/pay/aaaaaaa
```

1. Mantenha sua chave segura! Tenha certeza de usa-la como variável de ambiente ou outro local apropriado.
2. O preço do produto deve ser passado em centavos.
3. URL para redirecionar o cliente caso o mesmo clique na opção "Voltar".
4. URL para redirecionar o cliente quando o pagamento for concluído.
5. Dados do seu cliente. Caso o cliente não exista ele será criado.
6. CPF ou CNPJ do cliente.
7. Para cobranças únicas, use `ONE_TIME`. Para cobranças que podem ser pagas mais de uma vez, use `MULTIPLE_PAYMENTS`.


### Criando seu primeiro cliente
```py
customer = client.customers.create({
    "email": "customer@example.com",
    "name": "Customer Name",
    "cellphone": "(12) 3456-7890",
    "tax_id": "123-456-789-10"
})
print(customer.email)
#> customer@example.com
```

## **Sobre**
A {{ org_name }} é um gateway de pagamento que surgiu da nossa própria necessidade de simplificar cobranças em nossos produtos.

Em caso de duvidas ou suporte contate nos pelo email [ajuda@abacatepay.com](mailto:{{help_email}})
