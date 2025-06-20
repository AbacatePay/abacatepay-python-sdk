# AbacatePay SDK

![PyPI Version](https://img.shields.io/pypi/v/abacatepay?label=pypi%20package)
![PyPI Downloads](https://img.shields.io/pypi/dm/abacatepay)

> A Python SDK to simplify interactions with the AbacatePay API. <br />
> This SDK provides tools for billing management, customer handling, and more.


[English](README.md) | [Português](README-pt.md)

---

## Table of Contents

- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage Examples](#usage-examples)
  - [Create a Billing](#create-a-billing)
  - [List All Billings](#list-all-billings)
  - [Customer Management](#customer-management)
- [Contributing](#contributing)

---

## Installation

### Using pip

```bash
pip install abacatepay
```

### Using Poetry

```bash
poetry add abacatepay
```

---

## Getting Started

To use the SDK, import it and initialize the client with your API key:

```python
import abacatepay

client = abacatepay.AbacatePay("<your-api-key>")
```

---

## Usage Examples

### Create a Billing

```python
from abacatepay.products import Product


products = [
    Product(
        external_id="123",
        name="Test Product",
        quantity=1,
        price=50_00,
        description="Example product"
    ),
    # or as dict
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

### List All Billings

```python
billings = client.billing.list()
for billing in billings:
    print(billing.id, billing.status)

print(len(billings))
```

### Customer Management

```python
from abacatepay.customers import CustomerMetadata

customer = CustomerMetadata(  # Its can also be only a dict
    email="customer@example.com",
    name="Customer Name",
    cellphone="(12) 3456-7890",
    tax_id="123-456-789-10"
)

created_customer = client.customers.create(customer)
print(created_customer.id)
```

---

## Contributing

We welcome contributions to the **AbacatePay SDK**!
To get started, please follow the steps in our [Contributing Guide](./CONTRIBUTING.md).
