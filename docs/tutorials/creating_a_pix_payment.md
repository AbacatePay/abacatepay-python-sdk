Você pode criar, consultar e simular pagamentos via Pix diretamente pelo SDK da {{ org_name }}.

---

## 1. Criando um Pix QR Code

Você pode criar um Pix QR Code informando o valor, dados do cliente e uma descrição opcional.

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>")
ONE_MINUTE = 60

pix_qr = client.pixQrCode.create(
    amount=500_00,  # (1)
    description="Assinatura mensal",
    expires_in=ONE_MINUTE,  # (2)
    customer={  # (3)
        "name": "Maria Silva",
        "email": "maria@email.com",
        "cellphone": "(11) 90000-0000",
        "tax_id": "123.456.789-00"
    }
)

print(pix_qr.status)
```

1. O valor é em **centavos** (ex: `500_00` = R$ 500,00).
2. O campo `expires_in` é opcional (em segundos). Ex: `600` = 10 minutos.
3. Você pode passar o cliente como `dict` ou [`CustomerMetadata`][abacatepay.customers.CustomerMetadata].

---

/// details | Referência para o método `create`
::: abacatepay.pixQrCode.client.PixQrCodeClient.create
///

/// details | O objeto `PixQrCode`
::: abacatepay.pixQrCode.models.PixQrCode
///

---

## 2. Consultando o status do Pix

Após criar um Pix QR Code, você pode acompanhar seu status (se foi pago, expirado, etc).

```py
status = client.pixQrCode.check(pix_qr.id)
print(status.status)
# > "PAID" ou "PENDING" ou "EXPIRED"
```

---

## 3. Simulando um pagamento (ambiente de testes)

Se estiver usando o ambiente sandbox, você pode simular um pagamento:

```py
simulado = client.pixQrCode.simulate(pix_qr.id)
print(simulado.status)
# > "PAID"
```

Você também pode enviar metadados para simular o pagamento:

```py
pix_status = client.pixQrCode.simulate(
    id=pix_qr.id,
    metadata={"origin": "test-script"}
)
print(pix_status.status)
```
/// details | O objeto `PixStatus`
::: abacatepay.pixQrCode.models.PixStatus
///

---

Pronto! Agora você já pode gerar e gerenciar pagamentos via Pix de forma prática com a {{ org_name }} 🚀

