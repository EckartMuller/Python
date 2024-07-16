import pyqrcode

try:
    url = input("Enter URL to generate QR Code: ")
    qrCode = pyqrcode.create(url)
    qrCode.svg("deneme.svg", scale=5)
    print("QR Code successfully generated and saved as qrcode.svg and qrcode.png")
except Exception as e:
    print(f"An error occurred: {e}")
