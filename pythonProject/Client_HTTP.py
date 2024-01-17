import requests
def client_http_get():
    # saisir un serveur a interroger
    url=str(input("saisir l'url à interroger : "))
    # requête get
    reponse=requests.get(url)
    # verifiez que le statut de la réponse est correct
    if reponse.status_code != 200 :
        print("url est pas valide")
        client_http_get()
    else:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.text)

def client_http_post(data):
    # saisir un serveur a interroger
    url = str(input("saisir l'url à interroger : "))

    # requête POST
    reponse = requests.post(url, data=data, json=None)

    # Vérifiez le statut de la réponse
    if reponse.status_code != 200:
        print("url est pas valide")
        client_http_post()
    else:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.text)

def client_http_put(data):
    # saisir un serveur a interroger
    url = str(input("saisir l'url à interroger : "))

    # requête PUT
    reponse = requests.put(url, data=data, json=None)

    # Vérifiez le statut de la réponse
    if reponse.status_code != 200:
        print("url est pas valide")
        client_http_put()
    else:
        # Affichez les données de la réponse
        print("Reponse :")
        print(reponse.text)
