import requests
import os
import urllib.request

for filename in os.listdir('static/samples'):

    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open('static/samples/'+filename, 'rb'),
        },
        headers={'api-key': '222eb8ee-27ae-4b5d-aaf6-6ad00569500b'}
    )
    print(r.json())

    urllib.request.urlretrieve(r.json()['output_url'], filename[:-4]+'_big.png')
