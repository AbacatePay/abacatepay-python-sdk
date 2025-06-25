# 🛠️ Guia de Contribuição

Agradecemos por querer contribuir com o **SDK do AbacatePay**!
Siga os passos abaixo para começar:

## ✅ Pré-requisitos

* [Python](https://www.python.org/downloads/) `>=3.10, <4.0`
* [Poetry](https://python-poetry.org/) `>=1.6.1`

## 🚀 Passo a passo

1. **Faça um fork do repositório**
   [Clique aqui para fazer o fork no GitHub](https://github.com/AbacatePay/abacatepay-python-sdk/fork)

2. **Clone o repositório do seu fork**
   Substitua `seu-usuario` pelo seu nome de usuário no GitHub:

   ```bash
   git clone https://github.com/seu-usuario/abacatepay.git
   cd abacatepay
   ```

3. **Configure o ambiente virtual com o [Poetry](https://python-poetry.org/)**

   > Caso ainda não tenha o Poetry instalado, siga as instruções [nesta página](https://python-poetry.org/docs/#installing-with-the-official-installer).

   ```bash
   poetry install
   ```

4. **Crie uma nova branch para suas alterações**
   Escolha um nome descritivo para a branch:

   ```bash
   git checkout -b nome-da-feature
   ```

5. **Execute os testes para garantir que tudo continua funcionando**

   ```bash
   poetry run task test
   ```

6. **Verifique a formatação e os padrões de código**
   O comando de testes já verifica o estilo do código com o [Ruff](https://docs.astral.sh/ruff/).
   Caso necessário, corrija manualmente com:

   ```bash
   poetry run task lint
   poetry run task fmt
   ```

7. **Não esqueça de documentar suas alterações**
    Para documentação nos utilizamos o [MKdocs](https://www.mkdocs.org/user-guide/).
    Também usamos [MKdocstrings](https://mkdocstrings.github.io/) para gerar a referência a partir de docstrings, portanto não esqueça de documentar suas funções e módulos devidamente.

8. **Faça commit e envie suas alterações**

    ```bash
    git add .
    git commit -m "Adiciona feature ou correção: descrição curta"
    git push origin nome-da-feature
    ```

9. **Abra um Pull Request no GitHub** e descreva suas alterações com clareza.

---

☕ Pronto! Agora é só tomar um café enquanto sua contribuição é revisada.
Obrigado por ajudar a melhorar o **SDK do AbacatePay**! 🙌
