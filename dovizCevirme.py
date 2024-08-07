#https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD
import json
import requests

api_key ="c563d054c366cc45f87a094c"
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulan_doviz=input("bozulan döviz (TRY/USD/EUR):")
cevirilen_doviz=input("çevirilen döviz (TRY/USD/EUR):")

miktar=float(input(f"ne kadar {bozulan_doviz} bozduracaksınız:"))
response =requests.get(f"{api_url}{bozulan_doviz}")

response_json=json.loads(response.text)
#print(response_json["conversion_rates"][cevirilen_doviz])
#print("1 {0} = {1} {2}".format(bozulan_doviz,response_json["conversion_rates"][cevirilen_doviz],cevirilen_doviz))
print("{0} {1} = {2:.3f} {3}".format(miktar,bozulan_doviz,(miktar * response_json["conversion_rates"][cevirilen_doviz]),cevirilen_doviz))
