import requests, json

# Parameter for just Foreign news
# 'fq': 'news_desk:("Foreign")'

# Beginning date
date = 20141030

# Loop through every year of that MM/DD going back to beginning of archive
while date > 18510101:

	page = 10

	while page > 0:


		# API call
		payload = {'begin_date': date, 'end_date': date, 'page' : page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
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

		page = page - 1

	# Increments the "beginning date" by subtracting 10,000 (reduces it by one year)
	date = date - 10000







				


				