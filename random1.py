import requests
from requests.models import Response
from pprint import pprint

result: Response = requests.get("https://westus.api.cognitive.microsoft.com/luis/prediction/v3.0/apps/7d1eeea3-9c4d-4ac8-a162-34599b5e7dda/slots/production/predict?subscription-key=92480e29ca404ae6b2429e9730e9ebaf&verbose=true&show-all-intents=true&log=true&query=travel to kathmandu")

pprint(result.json())