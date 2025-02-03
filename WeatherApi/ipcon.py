import requests

def get_ip_location(ip_address=None):
    # IP adresi belirtilmezse, kendi IP adresinizi alır
    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()

    return data

# IP adresinizi veya varsayılan olarak kendi IP adresinizi kullanın
location_data = get_ip_location()
print(location_data['city'])