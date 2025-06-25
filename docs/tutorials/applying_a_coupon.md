Com o SDK da {{ org_name }}, você pode criar cupons de desconto e listá-los com facilidade.

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>")

cupom = client.coupons.create(
    code="DEV10",  # (1)
    discount_kind="PERCENTAGE",  # (2)
    discount=10,  # (3)
    notes="Desconto exclusivo para devs",  # (4)
    max_redeems=100  # (5)
    metadata={"campanha": "abril"}  # (6)
)

print(cupom.code)
# > DEV10
```

1. Código único do cupom (ex: `"BLACKFRIDAY"`).
2. Pode ser `"PERCENTAGE"` (percentual) ou `"FIXED"` (valor fixo em centavos).
3. Valor do desconto (em `%` ou centavos, dependendo do tipo).
4. Descrição interna (opcional).
5. Limite de usos (opcional, `-1` = ilimitado).
6. Dados extras (opcionais).

/// details | O objeto `Coupon`
::: abacatepay.coupons.models.Coupon
///
---

Você pode buscar todos os cupons criados com:

```py
cupons = client.coupons.list()

for cupom in cupons:
    print(cupom.code, cupom.discount_kind, cupom.discount)
```

Se não houver nenhum cupom, o SDK retorna uma lista vazia.

---

Agora você já pode distribuir cupons promocionais no seu sistema usando a {{ org_name }} 🎟️🚀
