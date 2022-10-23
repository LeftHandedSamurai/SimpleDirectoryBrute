import requests


def makeReq():

    def fuzzer():
        dirlist = open("domains.txt", "r+")
        for dir in dirlist:
            x = requests.get("https://"+site+"/"+dir)
            if x.status_code:
                print(str(x.url)+"==>" + str(x.status_code))

    try:
        site = input("Enter domain:")
        r = requests.get("https://"+site)

        if r.status_code == 200:
            print("Starting to fuzzzzz")
            fuzzer()

    except requests.exceptions.ConnectionError:
        print("Site does not respond to the request")


makeReq()
