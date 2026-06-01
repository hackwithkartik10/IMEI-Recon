import pyfiglet
emei=pyfiglet.figlet_format("EMEI NUMBER")
print(emei)
import requests
from colorama import Fore

imei = input("Enter IMEI: ")

url = f"https://api.imeicheck.net/v1/checks?imei={imei}"

headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

response = requests.get(url, headers=headers)

data = response.json()

print(Fore.GREEN + "Brand:", data.get("brand"))
print(Fore.CYAN + "Model:", data.get("model"))
print(Fore.YELLOW + "Blacklisted:", data.get("blacklisted"))