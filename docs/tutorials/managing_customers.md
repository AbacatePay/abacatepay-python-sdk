Você pode criar e listar clientes com facilidade usando o SDK da {{ org_name }}.

---

## 1. Criando um cliente

Para criar um novo cliente, utilize o método `create`. Ele pode receber um dicionário, uma instância de `CustomerMetadata` ou argumentos nomeados.
=== "Argumentos nomeados"
    ```py
    from abacatepay import AbacatePay

    client = AbacatePay("<sua chave de API>")

    customer = client.customers.create(
        name="João Silva",
        email="joao@email.com",
        cellphone="(11) 91234-5678",
        tax_id="123.456.789-00"
    )

    print(customer.id)
    # > cust_abc123
    ```

=== "Dicionário"
    ```py
    from abacatepay import AbacatePay

    client = AbacatePay("<sua chave de API>")

    customer = client.customers.create({
        "name": "João Silva",
        "email": "joao@email.com",
        "cellphone": "(11) 91234-5678",
        "tax_id": "123.456.789-00"
    })

    print(customer.id)
    # > cust_abc123
    ```

=== "Usando modelo"
    ```py
    from abacatepay import AbacatePay
    from abacatepay.customers import CustomerMetadata

    client = AbacatePay("<sua chave de API>")

    customer_data = CustomerMetadata(
        name="João Silva",
        email="joao@email.com",
        cellphone="(11) 91234-5678",
        tax_id="123.456.789-00"
    )

    customer = client.customers.create(customer=customer_data)
    print(customer.id)
    ```

/// details | Referência para o método `create`
::: abacatepay.customers.client.CustomerClient.create
///

---

## 2. Listando clientes existentes

Você pode listar todos os clientes cadastrados com um único comando:

```py
customers = client.customers.list()
print(len(customers))

for customer in customers:
    print(customer.id, customer.name)
```

---

Pronto! Agora você já pode cadastrar e gerenciar clientes com a {{ org_name }} diretamente do seu sistema 🚀
