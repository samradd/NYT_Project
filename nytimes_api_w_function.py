import requests, json

# Parameter for just Foreign news
# 'fq': 'news_desk:("Foreign")'

# def JsonFileName(headline,pub_date):
# 	separator = '_'
# 	result = headline + separator + pub_date + '.json'
# 	return result

data_list = []

# Ending? date
date = 19000101

# Loop through every year of that MM/DD going back to beginning of archive
while date < 20000101:

	payload = {'begin_date': date, 'end_date': date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	data = json.loads(r.text)

	count = data['response']['meta']['hits']
	# print (count)

	pages = int(count / 10)

	print (pages)

	#for page in pages -- another request, etc.

# 	page = 10

# 	while page > 0:

# 		# API call
# 		payload = {'begin_date': date, 'end_date': date, 'fq': 'news_desk:("National Desk")', 'page': page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
# 		r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

# 		# Parses JSON from NYT API into a data structure 
# 		data = json.loads(r.text)

# 		# print (json.dumps(data, indent=4))

# 		# If statement to check whether API response is "good"		
# 		if data['response']['docs']:
		
# 			# Creates variables for 1st article from each day
# 			headline = data['response']['docs'][0]['headline']['main']
# 			pub_date = data['response']['docs'][0]['pub_date']
# 			# snippet = data['response']['docs'][0]['snippet']
# 			# multimedia = data['response']['docs'][0]['multimedia']



# 			# Prints those variables
# 			# print (headline + ' - ' + pub_date)

# 			headline_list = (headline + ' - ' + pub_date)

# 			data_list.append(headline_list)

# 			# file_name = JsonFileName(headline[0], pub_date)

# 		page = page - 1

# 		with open('file_name.txt', 'w') as f:
# 			f.write(json.dumps(data_list, indent=4))


# # 	# Increments the "beginning date" by subtracting 10,000 (reduces it by one year)
	date = date + 10000



#url w all data
	# http://api.nytimes.com/svc/search/v2/articlesearch.json?begin_date=19000101&end_date=19000101&api-key=7814e2003e284eebd3d2c5248733ece8:17:65376813

# write out all data to json files -- one json file for each day
# gather data and then write it out and reset the variable for each day
# clear out list before going to the next day






# # # 				