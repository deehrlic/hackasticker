import requests
import os
import urllib.request

i=0
for filename in os.listdir('samples'):

    if i<500:
        print(i)
        i+=1
        continue

    r = requests.post(
        "https://api.deepai.org/api/torch-srgan",
        files={
            'image': open('samples/'+filename, 'rb'),
        },
        headers={'api-key': '222eb8ee-27ae-4b5d-aaf6-6ad00569500b'}
    )
    print(r.json())

    urllib.request.urlretrieve(r.json()['output_url'], 'static/big_samples/'+filename[:-4]+'_big.png')
