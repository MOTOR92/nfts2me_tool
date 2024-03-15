import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def process_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.select_one("head > meta:nth-child(13)")

        if meta_tag:
            content_value = meta_tag.get("content")
        else:
            content_value = "Мета-тег не найден."
    else:
        content_value = f"Ошибка при получении страницы. Статус код: {response.status_code}"

    return content_value

def main():
    with open("urls.txt", "r") as file:
        urls = file.read().splitlines()

    with open("contract.txt", "w") as output_file, open("list.txt", "w") as list_file:
        contract_addresses = []  # Список для хранения всех контрактов

        for url in tqdm(urls, desc="Собираю контракты", unit="URL", bar_format="{l_bar}{bar}{r_bar}", colour="green"):
            result = process_url(url)
            output_file.write(f"{url}: {result}\n")
            contract_addresses.extend(result.split(", "))

        list_file.write(",\n".join(['"' + address + '"' for address in contract_addresses]) + "\n")

if __name__ == "__main__":
    main()
