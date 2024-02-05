import requests
import json
import pandas as pd

def extract_epss(cve_id):
    
    url = requests.get('https://api.first.org/data/v1/epss?cve='+cve_id)
    text=url.text

    
    infos = json.loads(text)
    datas = infos['data'] # On obtient une liste

    # On prends le premier objet de cette liste qui est un dictionnaire
    data = datas[0]

    # on récupère la valeur pour la clé 'epss'
    epss = float(data['epss'])

    return epss

def extract_percentile(cve_id):

    url = requests.get('https://api.first.org/data/v1/epss?cve='+cve_id)
    text=url.text

    
    infos = json.loads(text)
    datas = infos['data'] # On obtient une liste

    # On prends le premier objet de cette liste qui est un dictionnaire
    data = datas[0]

    # on récupère la valeur pour la clé 'percentile'
    percentile = float(data['percentile'])

    return percentile