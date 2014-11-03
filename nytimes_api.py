import requests, json


for year in range(1900, 2000):

	begin_date = str(year) + '0101'

	end_date = str(year) + '0101'

	# print (begin_date)

	payload = {'begin_date': begin_date, 'end_date': end_date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	data = json.loads(r.text)

	# print (data)


# pages loop up here (217)...

# year_pagenum.json (save requests to json file for each day)



# payload = {'begin_date':'19000101', 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# print (r.status_code)

# # print (r.text)

# data = json.loads(r.text)

# for first_layer in data:
# 	# print (first_layer)

# 	if first_layer == 'response':
		
# 		for second_layer in data[first_layer]:
# 			# print (second_layer)

# 			count = data['response']['meta']['hits']
# 			# print (count)

# 			pages = int(count / 10)
# 			# print (pages)

# 			for a_page in range(0,pages):


# 				payload = {'begin_date': begin_date, 'end_date': end_date, 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# 				r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# 				data = json.loads(r.text)

				# print (data)



				# def date_range(start_date, end_date):
				# 	if start_date = end_date:
				# 		for n in range ((end_date - start_date).days + 1):
				# 			yield start_date + datetime.whatever(n)

				# date_result = date_range(19000101, 19010101)

				# print (date_result)

					
						# we need to pull one date for every year
						# we need to loop through the data and add one to that year


				# for first_layer in data:
				# # print (first_layer)

				# 	if first_layer == 'response':

				# 		for second_layer in data[first_layer]:
				# 			# print (second_layer)

				# 			if second_layer == 'docs':

				# 				for third_layer in data[first_layer][second_layer]:
				# 					print (third_layer['headline']['main'])


 				
 				# loop through the dates & then through the pages



				


				