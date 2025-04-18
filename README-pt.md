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

Bom-vindo a contribuições para o SDK do AbacatePay! Siga os passos abaixo para começar:

1. Fork o repositório no GitHub.

2. Clone seu fork localmente:

   ```bash
   git clone https://github.com/your-username/abacatepay.git
   cd abacatepay
   ```

3. Configure o ambiente virtual usando [poetry](https://python-poetry.org/):
> Se você não tiver poetry instalado, você pode instalar seguindo as instruções [aqui](https://python-poetry.org/docs/#installing-with-the-official-installer).

   ```bash
   poetry install
   ```

4. Faça suas alterações em uma nova branch:

   ```bash
   git checkout -b feature-name
   ```

5. Execute os testes para garantir que suas alterações não quebrem a funcionalidade existente:

   ```bash
   poetry run pytest
   ```

6. Commit suas alterações e envie a branch:

   ```bash
   git add .
   git commit -m "Add feature or fix description"
   git push origin feature-name
   ```

7. Abra um pull request no GitHub e descreva suas alterações.
