import fakedata, exception, bcolors
import requests, time

class Request:
    def __init__(self):
        self.fakeData = fakedata.FakeData()
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.session = requests.Session()
        self.url = ""

    def call(self, url, times):
        loop = 1

        try:
            loop = int(times)
        except ValueError:
            raise exception.CallError('Invalid value for spam loop.') 

        for i in range(loop):

            self.fakeData.getFakeUser()

            r = self.session.post(url,headers=self.headers,data=self.fakeData.payload)

            if (r.status_code != 200):
                raise exception.CallError('Error processing post request.') 
            else:
                print(bcolors.colors.OKGREEN + 'Form posted for fake user ' + self.fakeData.payload['lastname'] + ' - Status code ' + str(r.status_code) + bcolors.colors.ENDC)

            time.sleep(1)

        return r.status_code

