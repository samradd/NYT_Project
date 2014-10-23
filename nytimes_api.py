import requests, json

payload = {'begin_date': '19000101', 'end_date': '19000101', 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

print (r.status_code)

# print (r.text)

data = json.loads(r.text)

# print (json.dumps(data, indent=4))


for first_layer in data:
	# print (first_layer)

	if first_layer == 'response':

		for second_layer in data[first_layer]:
			# print (second_layer)

			if second_layer == 'docs':

				for third_layer in data[first_layer][second_layer]:
					print (third_layer['headline']['main'])

				


				