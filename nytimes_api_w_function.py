import requests, json

# Parameter for just Foreign news
# 'fq': 'news_desk:("Foreign")'

def JsonFileName(headline_dates,page_num):
	separator = '_'
	result = headline_dates + separator + page_num
	return result

json_file = []

# Ending? date
date = 20000101

# Loop through every year of that MM/DD going back to beginning of archive
while date > 19000101:

	page = 10

	while page > 0:

		# API call
		payload = {'begin_date': date, 'end_date': date, 'page': page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
		r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

		# Parses JSON from NYT API into a data structure 
		data = json.loads(r.text)

		# print (json.dumps(data, indent=4))

		# If statement to check whether API response is "good"		
		if data['response']['docs']:
		
			# Creates variables for 1st article from each day
			headline = data['response']['docs'][0]['headline']['main']
			pub_date = data['response']['docs'][0]['pub_date']

	# trying to iterate through the headlines to get more than one per day  --> something to do with the [0] above

		# 	print (headline)
			# if next_headline != 0:
			# 	headline = headline + 1

			# Prints those variables
			# print (headline + ' - ' + pub_date)

			headline_list = (headline + ' - ' + pub_date)

			json_file.append(headline_list)

			file_name = JsonFileName(headline[0], pub_date)

		page = page - 1

		with open(file_name, 'w') as f:
			f.write(json.dumps(json_file,indent=4))


# 	# Increments the "beginning date" by subtracting 10,000 (reduces it by one year)
	date = date - 10000







# # 				