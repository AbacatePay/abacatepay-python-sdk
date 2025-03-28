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

We welcome contributions to the AbacatePay SDK! Follow the steps below to get started:

1. Fork the repository on GitHub.

2. Clone your fork locally:

   ```bash
   git clone https://github.com/your-username/abacatepay.git
   cd abacatepay
   ```

3. Set up the virtual environment using [poetry](https://python-poetry.org/):
> If you don't have poetry installed, you can install following the instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer).

   ```bash
   poetry install
   ```

4. Make your changes in a new branch:

   ```bash
   git checkout -b feature-name
   ```

5. Run tests to ensure your changes don’t break existing functionality:

   ```bash
   poetry run pytest
   ```

6. Commit your changes and push the branch:

   ```bash
   git add .
   git commit -m "Add feature or fix description"
   git push origin feature-name
   ```

7. Open a pull request on GitHub and describe your changes.
