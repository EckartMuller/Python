import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.background import BackgroundScheduler

product_link = input("Please enter product link (amazon.com.tr, trendyol.com, or hepsiburada.com): ")
product_price_limit = float(input("Enter the limit at which you want to be notified when the price drops: "))
receiver_email = input("Enter your email address to receive notifications: ")

def send_mail(receiver_email, product_price, product_link):
    sender_mail = "*****@gmail.com"
    sender_password = "google application password"

    subject = "🔥 Product Spy - Price Drop Alert!"
    message = f"🎉 The price of the product has decreased! 🎉\n\nNew price: {product_price} TL\n\nProduct Link: {product_link}"

    msg = MIMEMultipart()
    msg['From'] = sender_mail
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail, receiver_email, msg.as_string())
        server.quit()
        print("✅ E-posta sended!")
    except Exception as e:
        print(f"❌ An error occurred while sending the email: {e}")

def get_product_price(driver, product_link):
    if "amazon" in product_link:
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))
            )
            price_element = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
            price_text = price_element.text.strip()
            product_price = float(price_text.replace(".", "").replace(",", "").strip())
            return product_price
        except Exception as e:
            print(f"Error while getting price from Amazon: {e}")
            return None

    elif "trendyol" in product_link:
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[6]/main/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/span[2]"))
            )
            price_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/main/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/span[2]")
            price_text = price_element.text.strip().replace("₺", "").replace(",", "").strip()
            product_price = float(price_text)
            return product_price
        except Exception as e:
            print(f"Error while getting price from Trendyol: {e}")
            return None

    elif "hepsiburada" in product_link:
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "/html/body/div[2]/div/main/div/div/div[2]/section[1]/div[2]/div[3]/div/div[1]/div[1]/span"))
            )
            price_element = driver.find_element(By.CSS_SELECTOR, "/html/body/div[2]/div/main/div/div/div[2]/section[1]/div[2]/div[3]/div/div[1]/div[1]/span")
            price_text = price_element.text.strip().replace("TL", "").replace(",", "").strip()
            product_price = float(price_text)
            return product_price
        except Exception as e:
            print(f"Error while getting price from Hepsiburada: {e}")
            return None
    else:
        print("There is no supported site in this link.!")
        return None

def price_control(product_link, product_price_limit, receiver_email):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(product_link)

    product_price = get_product_price(driver, product_link)

    if product_price is not None:
        print(f"📢 Current Price: {product_price} TL")

        if product_price <= product_price_limit:
            print(f"🔥 Price Dropped! New Price: {product_price} TL")
            send_mail(receiver_email, product_price, product_link)
        else:
            print("🔔 Price is still high!")
    else:
        print("Could not get price!")

    driver.quit()

def job():
    print("🔄 Starting price check...")
    price_control(product_link, product_price_limit, receiver_email)

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', hours=6)

print("⏳ The program runs in the background. It will check prices every 6 hours...")

scheduler.start()

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
