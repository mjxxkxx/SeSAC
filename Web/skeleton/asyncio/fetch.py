import requests

def fetch(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response

def main():
    urls = [...] # virtual urls

    for url in urls:
        response = fetch(url)
        # do sth with response 

if __main__ == '__main__':
    main()