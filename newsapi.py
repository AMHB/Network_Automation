import requests

apikey = 'fb0f4948b6a24d19b8ffcb5ef0f340e3'

response = requests.get('https://newsapi.org/v2/top-headlines',
                        params={
                            # 'q': 'bitcoin',
                            'category': 'health',
                            'country': 'tr',
                        },
                        headers={'X-Api-Key': apikey})

if response.status_code == 200:
    data = response.json()
    if data['status'] == 'ok':
        for title in [x['title'] for x in data['articles']]:
            print(title)
    else:
        print(response.text)
else:
    print(response.text)
