import urllib.parse
import urllib.request


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class URLFetcher(metaclass=Singleton):

    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)

        with urllib.request.urlopen(req) as response:

            if response.code == 200:
                print(response.read())

                self.urls.append(url)


def main():

    MY_URLS = ['http://www.voidspace.org.uk', 
               'http://google.com', 
               'http://python.org',
               'https://www.python.org/error',
               ]

    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)

if __name__=='__main__':
    main()