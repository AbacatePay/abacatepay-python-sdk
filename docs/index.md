# Abacatepay SDK python

1. [Inicio rápido](#inicio-rapido)
    - [Instalação](#instalacao)
    - [Criando a sua primeira cobrança](#criando-sua-primeira-cobranca)
    - [Cadastrando o seu primeiro cliente](#criando-um-cliente)

## Inicio rápido
/// admonition | Pré-requisitos.
- Ter sua conta da abacatepay disponível para aceitar pagamentos, caso ainda não tenha você pode cria-la [aqui](https://www.abacatepay.com/login)
- Uma vez que sua contra estiver disponível você pode encontrar a sua chave de API [aqui](https://www.abacatepay.com/integrar)
{% include "templates/pre_requirements.md" %}
///

### Instalação
{% include "templates/installation.md" %}



### Criando sua primeira cobrança
```py
import abacatepay

client = abacatepay.AbacatePay("<sua chave de API>")

billing = client.billing.create(
    products=[
        {
            "external_id": "123",
            "name": "PC gamer",
            "quantity": 1,
            "price": 1600_00, # (1)
            "description": "PC gamer completo de ultima geração"
        }
    ],
    return_url="https://mysite.com/return",  # (2)
    completion_url="https://mysite.com/completed",  # (3)
    customer={  # (4)
        "name": "John Doe",
        "email" "john@email.com",
        "cellphone": "(21) 5032-2583",
        "tax_id": "123.456.789-10"  # (5)
    },
    frequency='ONE_TIME',  # (6)
)
print(billing.url)
# > https://abacatepay.com/pay/aaaaaaa
``` 

1. O preço do produto deve ser passado em centavos.
2. URL para redirecionar o cliente caso o mesmo clique na opção "Voltar".
3. URL para redirecionar o cliente quando o pagamento for concluído.
4. Dados do seu cliente. Caso o cliente não exista ele será criado.
5. CPF ou CNPJ do cliente.
6. Para cobranças únicas, use `ONE_TIME`. Para cobranças que podem ser pagas mais de uma vez, use `MULTIPLE_PAYMENTS`.


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

### Listando todos os clientes
```py
customers = client.customers.list()
for customer in customers:
    print(customer.id, customer.email)  # > cust_123 customer@email.com
```