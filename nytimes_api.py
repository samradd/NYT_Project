import requests, json

payload = {'begin_date':'19000101', 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

print (r.status_code)

# print (r.text)

data = json.loads(r.text)

for first_layer in data:
	# print (first_layer)

	if first_layer == 'response':
		
		for second_layer in data[first_layer]:
			# print (second_layer)

			count = data['response']['meta']['hits']
			# print (count)

			pages = count / 10

			# print (pages)


			for pages in data:
				payload = {'begin_date':'19000101', 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
				data = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

			
			# 	for first_layer in data:
					# print (first_layer)

					# if first_layer == 'response':

					# 	for second_layer in data[first_layer]:
					# 		# print (second_layer)

					# 		if second_layer == 'docs':

					# 			for third_layer in data[first_layer][second_layer]:
					# 				print (third_layer['headline']['main'])



				




			
#get to offset & divide 13million number by 10, then loop through for that num of pages
# for page in xnum_of_pages

# count = data['response']['meta']['hits']

# pages = hits/10

# for a_page in pages:
# 	payload = {'pages': a_page, 'api-key'}
# 	r = requests...


# print (json.dumps(data, indent=4))


# 
# for first_layer in data:
# 	# print (first_layer)

# 	if first_layer == 'response':

# 		for second_layer in data[first_layer]:
# 			# print (second_layer)

# 			if second_layer == 'docs':

# 				for third_layer in data[first_layer][second_layer]:
# 					print (third_layer['headline']['main'])




				


				