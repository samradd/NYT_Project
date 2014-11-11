import requests, json

# Parameter for just Foreign news
# , 'fq': 'news_desk:("National Desk")'

date = 19000101

# Loop through every year of that MM/DD going back to beginning of archive
# while begin_date == str(year) + '0101':
while date < 20010101:

	# API call
	payload = {'begin_date': date, 'end_date': date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	# Parses JSON from NYT API into a data structure 
	data = json.loads(r.text)

	# print (data)
	# print (json.dumps(data, indent=4))

	count = data['response']['meta']['hits']
	# print (count)

	pages = int(count / 10)
	print (pages)

	date = date + 10000


	# for year in range(1900,2001):

	# 	begin_date = str(year) + '0101'
	# 	end_date = str(year) + '0101'


	# for a_page in range(0,pages):

	# 	payload = {'begin_date': begin_date, 'end_date': end_date, 'page': pages, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	# 	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	# 	data = json.loads(r.text)

	# 	print (json.dumps(data, indent=4))

	# if data['response']['docs']:

	# 	for article in data['response']['docs']:
	# 		headline = article['headline']['main']
	# 		pub_date = article['pub_date']

	# 		print (headline + ' - ' + pub_date)


print ('___________________')

	# pages = 10

	# for a_page in pages:

	# 	payload = {'begin_date': begin_date, 'end_date': end_date, 'page':pages, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	# 	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	# 	# Takes number of hits and finds # of pages
	# 	count = data['response']['meta']['hits']
	# 	print (count)
		# pages = int(count / 10)
		# print (pages)

# Now that we've found "pages," loop through each page of 10 articles
# for a_page in range(0,pages):
	
# 	# Prints the page number
# 	print (a_page)

# 	# Resets 'payload' and 'r' to the new API request for that specific page
# 	payload = {'begin_date': begin_date, 'end_date': end_date, 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813', 'fq': 'word_count:([2000 TO 7000]) AND Poopie'}
# 	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# 	# Resets 'data' to the payload of the new API request
# 	data = json.loads(r.text)

# 	# If statement to check whether API response is "good"		
# 	if data['response']['docs']:

# 		for article in data['response']['docs']:
# 			headline = article['headline']['main']
# 			pub_date = article['pub_date']
# 			print (headline + ' - ' + pub_date)

# 	# Increments the "beginning date" by subtracting 10,000 (reduces it by one year)
# 	# date = date - 10000
# 	begin_date = begin_date - 10000
# 	end_date = end_date - 10000


print ('_____________________')

# Creates variables for 1st article from each day
# headline = data['response']['docs'][0]['headline']['main']
# pub_date = data['response']['docs'][0]['pub_date']

# Prints those variables
# print (headline + ' - ' + pub_date)



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
		


# 				for first_layer in data:
# 					print (first_layer)



# 					if first_layer == 'response':

# 						for second_layer in data[first_layer]:
# 							# print (second_layer)

# 							if second_layer == 'docs':

# 								for third_layer in data[first_layer][second_layer]:
# 									print (third_layer['headline']['main'])



				




			
# get to offset & divide 13million number by 10, then loop through for that num of pages
# for page in xnum_of_pages

# count = data['response']['meta']['hits']

# pages = hits/10

# for a_page in pages:
# 	payload = {'pages': a_page, 'api-key'}
# 	r = requests...


# print (json.dumps(data, indent=4))



# for first_layer in data:
# 	# print (first_layer)

# 	if first_layer == 'response':

# 		for second_layer in data[first_layer]:
# 			# print (second_layer)

# 			if second_layer == 'docs':

# 				for third_layer in data[first_layer][second_layer]:
# 					print (third_layer['headline']['main'])




				


				