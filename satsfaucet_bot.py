from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

# Caminho do chromedriver
chrome_path = "C:\\Users\\seucaminho\\depasta\\aqui\\chromedriver.exe"

# Opções do navegador
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Iniciar driver
service = Service(chrome_path)
driver = webdriver.Chrome(service=service, options=options)

# Abrir o site
driver.get("https://satsfaucet.com/app/bounty")
print("[✔] Faça login manualmente. O bot iniciará em 30 segundos...")
time.sleep(30)  # Tempo para login manual

# Loop para verificar e clicar no botão 'Claim'
while True:
    try:
        driver.refresh()
        time.sleep(5)

        claim_button = driver.find_element(By.XPATH, "//button[contains(., 'Claim')]")

        if claim_button.is_displayed() and claim_button.is_enabled():
            claim_button.click()
            print("[✔] Botão 'Claim' clicado com sucesso!")
        else:
            print("[…] Botão encontrado, mas não clicável.")

    except NoSuchElementException:
        print("[…] Botão 'Claim' ainda não disponível.")
    except Exception as e:
        print(f"[X] Erro inesperado: {e}")

    print("[⏳] Aguardando 1 hora para próxima verificação...")
    time.sleep(3600)
