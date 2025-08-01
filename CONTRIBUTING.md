# 🛠️ Contributing Guide

We welcome contributions to the **AbacatePay SDK**! Follow the steps below to get started.

## ✅ Prerequisites

* [Python](https://www.python.org/downloads/) `>=3.10, <4.0`
* [Poetry](https://python-poetry.org/) `>=1.6.1`

## 🚀 Getting Started

1. **Fork the repository**
   [Fork it on GitHub](https://github.com/AbacatePay/abacatepay-python-sdk/fork)

2. **Clone your fork locally**
   Replace `your-username` with your GitHub username:

   ```bash
   git clone https://github.com/your-username/abacatepay.git
   cd abacatepay
   ```

3. **Set up the virtual environment using [Poetry](https://python-poetry.org/)**

   > If you don’t have Poetry installed, follow the instructions [here](https://python-poetry.org/docs/#installing-with-the-official-installer).

   ```bash
   poetry install
   ```

4. **Create a new branch for your changes**
   Use a descriptive name for the feature or fix:

   ```bash
   git checkout -b feature-name
   ```

5. **Run the tests** to ensure nothing is broken:

   ```bash
   poetry run task test
   ```

6. **Check code style and formatting**
   The test command will also check code style using [Ruff](https://docs.astral.sh/ruff/).
   If formatting issues remain, you can fix them manually:

   ```bash
   poetry run task lint
   poetry run task fmt
   ```

7. **Don't forget to document your changes**
   We use [MKDocs](https://www.mkdocs.org/user-guide/) for documentation.
   We also use [MKDocStrings](https://mkdocstrings.github.io/) to generate reference documentation from docstrings, so make sure to properly document your functions and modules.

8. **Commit and push your changes**

   ```bash
   git add .
   git commit -m "Add feature or fix: short description"
   git push origin feature-name
   ```

9. **Open a pull request** on GitHub and describe your changes clearly.

---

☕ That’s it! Grab a coffee while we review your contribution.
Thanks for helping improve **AbacatePay SDK**! 🙌
