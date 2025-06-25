# {{ org_name }} SDK Python

1. [Início rápido](#inicio-rapido)
    - [Instalação](#instalacao)
    - [Criando sua primeira cobrança](#criando-sua-primeira-cobranca)
    - [Cadastrando seu primeiro cliente](#criando-seu-primeiro-cliente)

2. [Sobre a {{ org_name }}](#sobre)
    - [Site oficial da AbacatePay]({{ oficial_website }})
    - [Documentação oficial da AbacatePay]({{ oficial_documentation }})
    - [Suporte](#suporte)

## Início rápido
/// admonition | Pré-requisitos
- Ter uma conta na {{ org_name }} habilitada para aceitar pagamentos e uma chave de API. Caso ainda não tenha, veja o tutorial [**Como pegar minha chave de acesso**](/tutorials/getting_api_key/).
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
            "price": 1600_00,  # (2)
            "description": "PC gamer completo de última geração"
        }
    ],
    return_url="https://mysite.com/return",         # (3)
    completion_url="https://mysite.com/completed",  # (4)
    customer={                                       # (5)
        "name": "John Doe",
        "email": "john@email.com",
        "cellphone": "(21) 5032-2583",
        "tax_id": "123.456.789-10"                   # (6)
    },
    frequency='ONE_TIME',                            # (7)
)
print(billing.url)
# > https://abacatepay.com/pay/aaaaaaa
```

1. Mantenha sua chave segura! Prefira usá-la como variável de ambiente ou em outro local apropriado.
2. O preço do produto deve ser informado em centavos.
3. URL para redirecionar o cliente caso ele clique na opção "Voltar".
4. URL para redirecionar o cliente após a conclusão do pagamento.
5. Dados do cliente. Caso ele ainda não exista, será criado automaticamente.
6. CPF ou CNPJ do cliente.
7. Para cobranças únicas, use `ONE_TIME`. Para cobranças que podem ser pagas mais de uma vez, use `MULTIPLE_PAYMENTS`.

### Criando seu primeiro cliente

```py
customer = client.customers.create({
    "email": "customer@example.com",
    "name": "Customer Name",
    "cellphone": "(12) 3456-7890",
    "tax_id": "123.456.789-10"
})
print(customer.email)
# > customer@example.com
```

## **Sobre**

A {{ org_name }} é um gateway de pagamentos criado por desenvolvedores, com foco em simplicidade, rapidez e integração fácil via API. Ideal para quem busca uma alternativa moderna e sem burocracia.

### Suporte
Em caso de dúvidas, fale com a gente: [ajuda@abacatepay.com](mailto:{{help_email}})
