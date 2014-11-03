import requests, json

<<<<<<< HEAD

for year in range(1900, 2000):

	begin_date = str(year) + '0101'

	end_date = str(year) + '0101'

	# print (begin_date)

	payload = {'begin_date': begin_date, 'end_date': end_date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	data = json.loads(r.text)
=======
# Parameter for just Foreign news
# 'fq': 'news_desk:("Foreign")'

# Beginning date
date = 20141030

# Loop through every year of that MM/DD going back to beginning of archive
while date > 18510101:

	# API call
	payload = {'begin_date': date, 'end_date': date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	# Parses JSON from NYT API into a data structure 
	data = json.loads(r.text)

	# If statement to check whether API response is "good"		
	if data['response']['docs']:
	
		# Creates variables for 1st article from each day
		headline = data['response']['docs'][0]['headline']['main']
		pub_date = data['response']['docs'][0]['pub_date']

		# Prints those variables
		print (headline + ' - ' + pub_date)

	# Increments the "beginning date" by subtracting 10,000 (reduces it by one year)
	date = date - 10000



# article_count = data['response']

# print (article_count)

# for first_layer in data:
# 	# print (first_layer)

# 	if first_layer == 'response':
		
# 		for second_layer in data[first_layer]:
# 			# print (second_layer)

# 			count = data['response']['meta']['hits']
# 			# print (count)

# 			pages = int(count / 10)

# 			# print (pages)
>>>>>>> FETCH_HEAD

	# print (data)

<<<<<<< HEAD

# pages loop up here (217)...

# year_pagenum.json (save requests to json file for each day)



# payload = {'begin_date':'19000101', 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# print (r.status_code)
=======
# 			for a_page in range(0,pages):

# 				payload = {'begin_date':'19000101', 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# 				r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# 				data = json.loads(r.text)

# 				print (data)
 				
#  				loop through the dates & then through the pages

# 				articles = page_num[data]

# 				for articles in data:

# 					for article in articles['response']['docs']:
# 					print (article['headline']['main'])
# 			ERROR WE KEEP GETTING!!! TypeError: 'int' object is not subscriptable	 (also that it's not iterable)	
# 			iterate the page number			
# 						count += 1
		
>>>>>>> FETCH_HEAD

# # print (r.text)

<<<<<<< HEAD
# data = json.loads(r.text)
=======
# 				for first_layer in data:
# 					print (first_layer)
>>>>>>> FETCH_HEAD

# for first_layer in data:
# 	# print (first_layer)

# 	if first_layer == 'response':
		
# 		for second_layer in data[first_layer]:
# 			# print (second_layer)

<<<<<<< HEAD
# 			count = data['response']['meta']['hits']
# 			# print (count)

# 			pages = int(count / 10)
# 			# print (pages)
=======
# 					if first_layer == 'response':

# 						for second_layer in data[first_layer]:
# 							# print (second_layer)

# 							if second_layer == 'docs':

# 								for third_layer in data[first_layer][second_layer]:
# 									print (third_layer['headline']['main'])
>>>>>>> FETCH_HEAD

# 			for a_page in range(0,pages):


# 				payload = {'begin_date': begin_date, 'end_date': end_date, 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# 				r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# 				data = json.loads(r.text)

				# print (data)


<<<<<<< HEAD
=======
			
# get to offset & divide 13million number by 10, then loop through for that num of pages
# for page in xnum_of_pages
>>>>>>> FETCH_HEAD

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

<<<<<<< HEAD
				# 	if first_layer == 'response':
=======

# for first_layer in data:
# 	# print (first_layer)
>>>>>>> FETCH_HEAD

				# 		for second_layer in data[first_layer]:
				# 			# print (second_layer)

				# 			if second_layer == 'docs':

				# 				for third_layer in data[first_layer][second_layer]:
				# 					print (third_layer['headline']['main'])


 				
 				# loop through the dates & then through the pages



				


				