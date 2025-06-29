
# 🛰️ satsfaucet_bot

Um bot simples e automatizado em Python que coleta satoshis (frações de bitcoin) automaticamente em sites como **SatsFaucet**, clicando no botão "Claim" sempre que disponível.

## 📁 Estrutura

```
📂 SCRIPTS/
├── chromedriver-win64/       # Pasta opcional com outros drivers
├── chromedriver.exe          # Driver do navegador Chrome
├── index.html                # Arquivo opcional (página de apresentação/local)
├── iniciar_coletor.bat       # Atalho para iniciar o bot com 2 cliques
└── satsfaucet_bot.py         # Script principal
```

## ⚙️ Requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- Biblioteca Selenium instalada

## 💻 Como instalar

1. Instale o Selenium:
   ```bash
   pip install selenium
   ```

2. Baixe o ChromeDriver no site oficial e coloque o executável na pasta do projeto (já incluído no seu caso).

## 🚀 Como usar

1. Execute o arquivo `iniciar_coletor.bat` com dois cliques, ou use o terminal:
   ```bash
   python satsfaucet_bot.py
   ```

2. O Chrome abrirá automaticamente. Faça o **login manualmente** na plataforma do faucet.

3. O bot vai:
   - Aguardar 60 segundos (você quem deternmina)
   - Clicar no botão "Claim" automaticamente, se estiver disponível
   - Esperar 1 hora e repetir o processo

## ❗ Avisos

- Evite uso excessivo ou múltiplas sessões no mesmo site para não ser banido.
- Este projeto tem finalidade educacional.
- Leia os termos de uso da plataforma que estiver utilizando.

## 💡 Dica

Use o `iniciar_coletor.bat` para facilitar o processo de execução automática, sem precisar abrir terminal toda vez.

---

Desenvolvido com 💰 por [Aparecida Marques](https://github.com/dinhapreta)
