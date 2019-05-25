import requests, string, random

#
# class FadeData
#   Creates fake data
#
class FakeData():

    def __init__(self):
        self.user = ''
        self.payload = {}

    def getFakeUser(self):
        r = requests.get('https://randomuser.me/api/')
        jsonResponse = r.json()
        jsonUser = jsonResponse['results'][0]
        self.payload = self.generatePayload(jsonUser)

        return self.user

    def generatePayload(self, json):
        return {
            'firstname': json['name']['first'].capitalize(),
            'lastname': json['name']['last'].capitalize(),
            'message': json['login']['sha256']
        }

    def randomString(self, strLength):
        pool = string.ascii_lowercase.join(string.digits).join(string.digits)
        return ''.join(random.choice(pool) for i in range(strLength))
        