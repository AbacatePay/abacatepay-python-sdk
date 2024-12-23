# AbacatePay
SDK Python para interagir com a API da AbacatePay (https://abacatepay.com)

![PyPI](https://img.shields.io/pypi/v/abacatepay?label=pypi%20package)
![PyPI - Downloads](https://img.shields.io/pypi/dm/abacatepay)
## Instalação

### Instalação via PyPI
```bash
pip install abacatepay
```

### Instalação via desenvolvimento

Para o desenvolvimento, você deve clonar o repositório e instalar o pacote com o instalador de pacotes `uv` (https://docs.astral.sh/uv/). Este instalador é recomendado para projetos Python e já possui a criação de ambientes virtuais e outras dependências necessárias para o desenvolvimento:

```bash
uv sync
uv run pip install -e .
uv venv
```

#### Rodando os testes

```bash
uv run pytest
```


## Usage/Examples

```python
import abacatepay
from abacatepay.models import Product

token = "<your enviroment api token>"
client = AbacatePay(token)

billing = client.billing.create(products=[Product(externalId="123", name="Teste", quantity=1, price=101, description="Teste")], returnURL="https://abacatepay.com", completionUrl="https://abacatepay.com")
print(billing.data.url)
# > https://abacatepay.com/pay/aaaaaaa
```