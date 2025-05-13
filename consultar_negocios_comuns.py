import requests

WEBHOOK_URL = "--"

payload = {
    "filter": {
        "CATEGORY_ID": 350
    },
    "select": ["ID", "TITLE", "STAGE_ID", "STAGE_SEMANTIC_ID"]
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    data = response.json()
    if data.get("result"):
        for item in data["result"]:
            print(f"ID: {item['ID']} | Título: {item['TITLE']} | Etapa: {item['STAGE_ID']} | Semântica: {item['STAGE_SEMANTIC_ID']}")
    else:
        print("Nenhum negócio comum encontrado nessa pipeline.")
else:
    print("Erro na requisição:", response.text)
