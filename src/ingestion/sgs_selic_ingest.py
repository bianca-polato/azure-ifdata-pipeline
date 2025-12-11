import os
import json
from datetime import datetime

import requests


URL = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados"
    "?formato=json&dataInicial=01/01/2020&dataFinal=31/12/2025"
)

#Função para pegar dados do site, via request
def fetch_sgs_raw():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    return response.json()

#Função para 'guardar' os dados 
def save_raw_to_landing(data: list) -> str:
    os.makedirs("data/landing", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join("data", "landing", f"sgs_selic_{timestamp}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return file_path

#função que executa as funções acima 
def main():
    raw_data = fetch_sgs_raw()
    output_path = save_raw_to_landing(raw_data)
    print(f"Arquivo salvo em: {output_path}")


if __name__ == "__main__":
    main()
