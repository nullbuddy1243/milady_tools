import requests, time, json

# https://www.miladymaker.net/milady/json/6756

base_url = 'https://miladymaker.net/milady/' # tokenId
token_uri = 'https://www.miladymaker.net/milady/json/' # tokenId

for tokenId in range(2254,10000): 
    img_url = "{}{}.png".format(base_url, tokenId)
    token_url = "{}{}".format(token_uri, tokenId)

    print("Getting {}\n{}".format(token_url, img_url))

    mil_json = json.loads(requests.get(token_url).content)
    # print(json.dumps(mil_json))

    with open("./jsons/{}.json".format(tokenId), 'w+') as handler:
        handler.write(json.dumps(mil_json))

    mil_img = requests.get(img_url).content

    this_mil_png = './img/{}.png'.format(tokenId)
    with open(this_mil_png, 'wb+') as handler:
        handler.write(mil_img)

    time.sleep(0.150)