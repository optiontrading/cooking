import requests
import json

def search_ingredients(ingredient):
   headers = {'Content-Type': 'application/json'}
   uri = 'http://localhost:9200/cooking/_search'
   json_body = '{"query" : {"match" : { "Ingredients": "%s" }}}'%(ingredient)
   resp = requests.get(uri, headers=headers, data=json_body)
   resp_text = json.loads(resp.text)
   print ("resp_text:", resp_text)
   return resp_text


if __name__ == '__main__':
   search_ingredients('coconut')
