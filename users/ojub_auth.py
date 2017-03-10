import requests

OPENJUB_BASE = "https://api.jacobs.university/"

def get_all(username, password):
	r = requests.post(OPENJUB_BASE + "auth/signin",
		data = {'username':username, 'password': password})

	if r.status_code != requests.codes.ok:
		return None

	resp = r.json()

	uname = resp['user']
	token = resp['token']

	users = []

	TIMEOUT = 60

	request = requests.get(OPENJUB_BASE + "query",
		params = {'token':token, 'limit': 20000}, timeout = TIMEOUT)

	while True:
		if request.status_code != requests.codes.ok:
			return None
		else:
			# read json
			resjson = request.json()

			# load all the users
			users += resjson["data"]

			# if there was no data or no next field, continue
			if len(resjson["data"]) == 0 or not resjson["next"]:
				return users
			else:
				request = requests.get(resjson["next"], timeout = TIMEOUT)
