import requests
import os
import json

token = 'NEc6kALgl4Wid0LvtypQuGUuIiguytpAfctYabLQ5F8'
auth = requests.auth.HTTPBasicAuth(username=token, password='')

ROOT = os.path.join(os.path.dirname(__file__), '..')

def request(param):
    if param is None:
        param = 'artifacts/?where={"lang":"Java", "reproduce_successes":{"$gt":0, "$lt":50}, "classification.code":"Yes"}'
    url = 'http://www.api.bugswarm.org/v1/%s' % (param)
    return requests.get(url, auth=auth, json=True).json()

param = None

results = []
while True:
    data = request(param)
    results += data['_items']
    print(data['_links'])
    if 'next' in data['_links']:
        param = data['_links']['next']['href']
    else:
        break
print("# Pairs of builds: ", len(results))
with open(os.path.join(ROOT, 'test.json'), 'w') as fd:
    json.dump(results, fd)