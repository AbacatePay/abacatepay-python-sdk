# AbacatePay SDK

![PyPI Version](https://img.shields.io/pypi/v/abacatepay?label=pypi%20package)
![PyPI Downloads](https://img.shields.io/pypi/dm/abacatepay)

> Um SDK Python para simplificar a interação com a API do AbacatePay. <br />
> Esse SDK fornece ferramentas para gerenciamento de faturamento, gerenciamento de clientes e muito mais.

[Inglês](README.md) | [Português](README-pt.md)

---

## Índice

- [Instalação](#instalação)
- [Iniciando](#iniciando)
- [Exemplos de Uso](#exemplos-de-uso)
  - [Criar uma fatura](#criar-uma-fatura)
  - [Listar todas as faturas](#listar-todas-as-faturas)
  - [Gerenciamento de clientes](#gerenciamento-de-clientes)
- [Contribuindo](#contribuindo)

---

## Instalação

### Usando pip

```bash
pip install abacatepay
```

### Usando Poetry

```bash
poetry add abacatepay
```

---

## Iniciando

Para usar o SDK, importe-o e inicialize o cliente com sua chave de API:

```python
import abacatepay

client = abacatepay.AbacatePay("<your-api-key>")
```

---

## Exemplos de Uso

### Criar uma fatura

```python
from abacatepay.products import Product

products = [
    Product(
        external_id="123",
        name="Test Product",
        quantity=1,
        price=5000,
        description="Example product"
    ),
    # ou como um dicionário
    {
        'external_id': "321",
        'name': "Product as dict",
        'quantity': 1,
        'price': 10_00,
        'description': "Example using dict"
    }
]

billing = client.billing.create(
    products=products,
    return_url="https://yourwebsite.com/return",
    completion_url="https://yourwebsite.com/complete"
)

print(billing.data.url)
```

### Listar todas as faturas

```python
billings = client.billing.list()
for billing in billings:
    print(billing.id, billing.status)

print(len(billings))
```

### Gerenciamento de clientes

```python
from abacatepay.customers import CustomerMetadata

customer = CustomerMetadata(  # Também pode ser apenas um dicionário
    email="customer@example.com",
    name="Customer Name",
    cellphone="(12) 3456-7890",
    tax_id="123-456-789-10"
)

created_customer = client.customers.create(customer)
print(created_customer.id)
```

---

## Contribuindo

Contribuições para o **SDK do AbacatePay** são muito bem-vindas!
Para colaborar, siga as instruções do nosso [guia de contribuição](./CONTRIBUTING-pt.md).
