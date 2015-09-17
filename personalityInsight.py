import requests
import json
import config


textFile = open('table.txt')
text = textFile.read()

pi_content_items = { 'contentItems' : [text] }

r = requests.post(config.pi_url + '/v2/profile', 
			auth=(config.pi_username, config.pi_password),
			headers = {
                'content-type': 'application/json',
                'accept': 'application/json'
            },
			data=json.dumps(pi_content_items)
		)
print(("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type'])))
print(json.loads(r.text))
