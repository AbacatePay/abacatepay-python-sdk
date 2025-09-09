Use o modo assíncrono para ganhar desempenho em cenários I/O‑bound (múltiplas chamadas de rede concorrentes), evitando bloquear threads da sua aplicação. 
Ele é ideal para integrações com APIs, processamento em lote e outras operações que aguardam respostas externas. O SDK fornece clientes assíncronos com a mesma interface dos clientes síncronos.

---

## 1. Iniciando um cliente assíncrono

Você pode ativar o modo assíncrono usando o parâmetro `async_mode=True` na função geradora `AbacatePay`:

```py
from abacatepay import AbacatePay

client = AbacatePay("<sua chave de API>", async_mode=True)  # retorna AbacatePayAsyncClient
```

Ou, se preferir uma declaração explícita, importe a classe diretamente:

```py
from abacatepay import AbacatePayAsyncClient

client = AbacatePayAsyncClient("<sua chave de API>")
```

/// admonition | Atenção
- O uso é semelhante ao modo síncrono, porém as chamadas aos métodos são `await` e devem ocorrer dentro de uma função `async`.
- Para executar uma função `async` em scripts, use `asyncio.run(...)`.
///

---

## 2. Exemplo: criando um Pix QR Code (async)

```py
import asyncio
from abacatepay import AbacatePay

async def main() -> None:
    client = AbacatePay("<sua chave de API>", async_mode=True)

    pix_qr = await client.pixQrCode.create(
        amount=500_00,  # (1)
        description="Assinatura mensal",
        expires_in=600,  # (2)
        customer={  # (3)
            "name": "Maria Silva",
            "email": "maria@email.com",
            "cellphone": "(11) 90000-0000",
            "tax_id": "123.456.789-00"
        }
    )

    print(pix_qr.status)

if __name__ == "__main__":
    asyncio.run(main())
```

1. O valor é em centavos (`500_00` = R$ 500,00).
2. `expires_in` é opcional (em segundos). Ex.: `600` = 10 minutos.
3. O cliente pode ser um `dict` ou [`CustomerMetadata`][abacatepay.customers.CustomerMetadata].

/// details | Referência (Async)
:::: abacatepay.pixQrCode.client.PixQrCodeAsyncClient.create
///

---

## 3. Executando várias chamadas em paralelo

Com `asyncio.gather`, você pode paralelizar múltiplas chamadas I/O-bound para reduzir o tempo total:

```py
import asyncio
from abacatepay import AbacatePay

async def criar_pix(client, valor: int):
    return await client.pixQrCode.create(amount=valor, description="Lote")

async def main() -> None:
    client = AbacatePay("<sua chave de API>", async_mode=True)

    resultados = await asyncio.gather(
        criar_pix(client, 100_00),
        criar_pix(client, 200_00),
        criar_pix(client, 300_00),
    )

    for r in resultados:
        print(r.id, r.status)

if __name__ == "__main__":
    asyncio.run(main())
```
Isso pode ser útil para criar lotes de cobranças e enviá-las mais rápido, ou para executar tarefas repetitivas em paralelo. Use conforme a sua necessidade.
---

## 4. Exemplo com FastAPI

```py
from fastapi import FastAPI
from abacatepay import AbacatePay
from app.schemas import PixCreateRequest

app = FastAPI()

client = AbacatePay("<sua chave de API>", async_mode=True)  # ou use AbacatePayAsyncClient para ser mais explícito

@app.post("/api/pix")
async def criar_pix(payload: PixCreateRequest):
    pix = await client.pixQrCode.create(
        amount=payload.amount,
        description=payload.description,
    )
    return {"id": pix.id, "status": pix.status}
```

/// admonition | Por que não bloqueia?
- Enquanto a função aguarda `await client.pixQrCode.create(...)`, o loop de eventos pode atender outras requisições.
- No modo síncrono, a thread ficaria ocupada até a resposta da API, reduzindo a concorrência.
///


Pronto! Agora você sabe iniciar e utilizar o cliente assíncrono. Se ainda não criou sua chave de API, veja: [Como pegar minha chave de acesso](getting_api_key.md). Para operações específicas, consulte os tutoriais:

- [Criando um Pix QR Code](creating_a_pix_payment.md)
- [Gerenciando clientes](managing_customers.md)
