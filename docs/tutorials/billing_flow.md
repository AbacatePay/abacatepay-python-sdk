## 1. Importe o SDK da {{ org_name }}
/// warning | Aviso
Caso ainda não tenha a sua chave de API siga o tutorial [**Como pegar minha chave de acesso**](tutorials/getting_api_key.md)
///

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>")  # (1)
```

1. **Mantenha sua chave segura!** Prefira armazená-la como uma variável de ambiente ou em outro local apropriado.

---

## 2. Adicione os produtos que deseja incluir na cobrança

```py
products = [
    {
        "external_id": "123",
        "name": "PC gamer",
        "quantity": 1,
        "price": 1600_00,  # (1)
        "description": "PC gamer completo de última geração"
    }
]
```

1. O preço deve ser informado em **centavos** (ex: R\$ 1600,00 → `160000`).

---

/// details | 💡 Usando modelos (opcional)
Se preferir, você também pode usar o modelo de produto fornecido pelo SDK:

```py
from abacatepay.products import Product

products = [
    Product(
        external_id="123",
        name="PC gamer",
        quantity=1,
        price=1600_00,
        description="PC gamer completo de última geração"
    )
]
```
///

---

## 3. Crie a cobrança
=== "✅ Para um cliente **já existente** na {{ org_name }}"
    ```py
    billing = client.billing.create(
        products=products,
        return_url="https://mysite.com/return",       # (1)
        completion_url="https://mysite.com/completed",# (2)
        customer_id='cust_1234',                      # (3)
        frequency='ONE_TIME',                         # (4)
    )

    print(billing.url)
    # > https://abacatepay.com/pay/aaaaaaa
    ```

    1. URL para onde o cliente será redirecionado ao clicar em "Voltar".
    2. URL de redirecionamento após o pagamento ser concluído.
    3. ID do cliente já cadastrado na {{ org_name }}.
    4. Use `ONE_TIME` para cobranças únicas ou `MULTIPLE_PAYMENTS` para recorrências manuais.

=== "✨ Para um **novo cliente**"
    ```py
    billing = client.billing.create(
        products=products,
        return_url="https://mysite.com/return",       # (1)
        completion_url="https://mysite.com/completed",# (2)
        customer={                                    # (3)
            "name": "John Doe",
            "email": "john@email.com",
            "cellphone": "(21) 5032-2583",
            "tax_id": "123.456.789-10"                # (4)
        },
        frequency='ONE_TIME',                         # (5)
    )

    print(billing.url)
    # > https://abacatepay.com/pay/aaaaaaa
    ```

    1. URL para onde o cliente será redirecionado ao clicar em "Voltar".
    2. URL de redirecionamento após o pagamento ser concluído.
    3. Se o cliente já existir (mesmo email ou CPF/CNPJ), ele não será recriado.
    4. CPF ou CNPJ do cliente.
    5. Use `ONE_TIME` para cobranças únicas ou `MULTIPLE_PAYMENTS` para recorrências manuais.

---

## 4. Listando cobranças existentes

Depois de criar suas cobranças, você pode acessar o histórico facilmente:

```py
billings = client.billing.list()
print(len(billings))

for billing in billings:
    print(billing.id, billing.status)
```

---

Pronto! Agora é só integrar com seu sistema e começar a cobrar seus clientes com praticidade 🚀😊
