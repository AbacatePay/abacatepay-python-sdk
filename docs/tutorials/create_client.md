Você pode instanciar o cliente do SDK da {{ org_name }} de forma simples usando a função `AbacatePay`. Por padrão, o cliente é síncrono para manter compatibilidade com versões anteriores.

---

## 1. Criando o cliente (modo padrão síncrono)

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>")
```

Com o `client` criado, você terá acesso aos serviços:

```py
client.billing      # Cobranças
client.customers    # Clientes
client.coupons      # Cupons
client.pixQrCode    # Pagamentos Pix (QR Code)
```

/// admonition | Boa prática
- Mantenha sua chave de API fora do código-fonte. Prefira variáveis de ambiente.

```py
import os
from abacatepay import AbacatePay

api_key = os.getenv("ABACATEPAY_API_KEY")
client = AbacatePay(api_key)
```

Se ainda não tem uma chave, veja o tutorial [Como pegar minha chave de acesso](getting_api_key.md).
///

---

## 2. Sobre o modo assíncrono (visão geral)

Se preferir trabalhar de forma assíncrona, você pode habilitar o modo async passando `async_mode=True` ao criar o cliente. Para detalhes, veja: [Uso assíncrono](asynchronous.md).

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>", async_mode=True)  # retorna AbacatePayAsyncClient
```

Também é possível importar as classes diretamente para uma declaração explícita:

=== "Síncrono (classe explícita)"

    ```py
    from abacatepay import AbacatePayClient

    client = AbacatePayClient("<sua chave de API>")
    ```

=== "Assíncrono (classe explícita)"

    ```py
    from abacatepay import AbacatePayAsyncClient

    client = AbacatePayAsyncClient("<sua chave de API>")
    ```

Para um guia completo sobre padrões de uso com `asyncio`, veja: [Uso assíncrono](asynchronous.md).

---

## 3. Próximos passos

- Quer criar sua primeira cobrança? Veja: [Criando um Pix QR Code](creating_a_pix_payment.md)
- Quer cadastrar clientes? Veja: [Gerenciando clientes](managing_customers.md)
- Quer desempenho com muitas chamadas? Veja: [Uso assíncrono](asynchronous.md)
