import json, os

{
    "timeline":
    {
        "headline":"Birth Control Timeline",
        "type":"default",
        "text":"<p>Intro body text goes here, blah blah blah</p>",
        "asset": {
            "media":"http://yourdomain_or_socialmedialink_goes_here.jpg",
            "credit":"Rachel, Sam & Hannah",
            "caption":"LIS-697 Fall 2014"
        },
        "date": [],

        "era": [
            {
                "startDate":"1915,01,01",
                "endDate":"2014,12,31",
                "headline":"Headline Goes Here",
                "text":"<p>Body text goes here, some HTML is OK</p>",
                "tag":"This is Optional"
            }

        ]
    }
}




data = []

for root, dirs, files in os.walk('.'):
	for file in files:
		if file.endswith('.json'):

			with open(file) as f:
				day = json.loads(f.read())
				# print (day)

				for articles in day:
					# print (articles["pub_date"])

					# split here! new variable called timeline dates, split it out, 
					# use that for the startdate & enddate

					# make a new dictionary for each headline 
					nytimes = {}

					nytimes["startDate"] = articles["pub_date"]
					nytimes["endDate"] = articles["pub_date"]
					nytimes["headline"] = articles["headline"]
					nytimes["text"] = articles["snippet"],articles["web_url"]
					nytimes["tag"] = None
					nytimes["classname"] = None
					nytimes["asset"] = None

					# print (nytimes)

					data.append(nytimes)
					# print (data)
				
				with open("timeline_file.json", 'w') as f:
					f.write(json.dumps(data,indent=4))
