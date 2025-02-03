from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Twitter giriş bilgileri
username = 'muller_eck99397'
password = 'Beko05353807479'

# Hedef kullanıcı adı
target_user = 'muller_eck99397'

# Selenium'u başlatma
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Tarayıcıyı arka planda çalıştırmak istemiyorsanız bu satırı yorum satırı yapabilirsiniz.
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Twitter giriş sayfasına gitme
driver.get('https://twitter.com/login')

# Sayfanın yüklenmesini bekleme
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'text')))

# Giriş bilgilerini doldurma (doğru XPATH veya CSS seçicilerini kullanarak)
try:
    username_input = driver.find_element(By.NAME, 'text')  # Güncellenmiş giriş alanı seçicisi
    username_input.send_keys(username)
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

    password_input = driver.find_element(By.NAME, 'password')  # Güncellenmiş giriş alanı seçicisi
    password_input.send_keys(password)
    driver.find_element(By.XPATH, '//div[@data-testid="LoginForm_Login_Button"]').click()

    # Girişin tamamlanmasını bekleme
    WebDriverWait(driver, 10).until(EC.url_contains('home'))

    # Hedef kullanıcının profil sayfasına gitme
    driver.get(f'https://twitter.com/{target_user}')

    # Sayfanın yüklenmesini bekleme
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/followers")]/span/span')))

    # Takipçi ve takip edilenler sayısını alma
    followers_count = driver.find_element(By.XPATH, '//a[contains(@href, "/followers")]/span/span').text
    following_count = driver.find_element(By.XPATH, '//a[contains(@href, "/following")]/span/span').text
    print(f"Takipçi sayısı: {followers_count}")
    print(f"Takip edilenler sayısı: {following_count}")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

# Tarayıcıyı kapatma
driver.quit()
