import requests

WEBHOOK_URL = "https://helpbr24.bitrix24.com.br/rest/12/s2ijlflqcsxil4ao/crm.deal.recurring.list.json"

payload = {
    "filter": {
        "CATEGORY_ID": 350
    },
    "select": ["ID", "TITLE", "ACTIVE", "NEXT_EXECUTION"]
}

response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 200:
    data = response.json()
    if data.get("result"):
        for item in data["result"]:
            print(f"ID: {item['ID']} | Título: {item['TITLE']} | Ativo: {item['ACTIVE']} | Próxima execução: {item.get('NEXT_EXECUTION')}")
    else:
        print("Nenhum negócio recorrente encontrado nessa pipeline.")
else:
    print("Erro na requisição:", response.text)