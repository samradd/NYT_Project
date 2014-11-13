import requests, json, re

## create a function to use later to name the json files
def JsonFileName(x,y,z):
	separator = '_'
	result = x + separator + y + separator + z
	return result

## create a list to append later
json_list = []

for year in range(1900,1902):

	begin_date = str(year) + '0101'
	end_date = str(year) + '0101'

	payload = {'begin_date': begin_date, 'end_date': end_date, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
	r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

	data = json.loads(r.text)

	# print (json.dumps(data, indent=4))

	print ("year:", year)
	## get count
	count = data['response']['meta']['hits']
	print ("count:",count)

	## divide by 10 to find total number of pages for year
	pages = int(count / 10)
	print ("pages:",pages)

	## loop through pages with dates
	for a_page in range(0,pages+1):

		payload = {'begin_date': begin_date, 'end_date': end_date, 'page': a_page, 'api-key': '7814e2003e284eebd3d2c5248733ece8:17:65376813'}
		r = requests.get('http://api.nytimes.com/svc/search/v2/articlesearch.json', params=payload)

		data = json.loads(r.text)

		## pull headlines and date of publication

		if data['response']['docs']:

			for article in data['response']['docs']:
				headline = article['headline']['main']
				pub_date = article['pub_date']

				## combine the gathered data
				headline_list = (headline + '-' + pub_date)

				# print (headline_list)

				## add the new data to the empty list
				json_list.append(headline_list)

				## use a regular expression to pull just the year out of the date
				# p = re.compile('\d\d\d\d')
				# m = p.search(headline_list)

				## name the file "headline", the number of results, and the year (regular expression)
				## replace str(year) below with (m.group(0)) for the regular expression to work
				file_name = JsonFileName("headlines","count" + str(count),str(year))

				## write the json files for each year
	with open(file_name, 'w') as f:
		f.write(json.dumps(json_list,indent=4))

	json_list = []

