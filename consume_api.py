import requests
import json
from pprint import pprint

response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for question in response.json()['items']:
  if question['answer_count'] == 0:
    pprint(question['title'])
    pprint(question['link'])
  else:
    print('skipped')
  print()