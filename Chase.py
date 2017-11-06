from OAuth import OAuth
from Search import Search

if __name__ == "__main__":
    certification = OAuth("Config.py")
    twitter=certification.oauth()
    search = Search(twitter)

    print("Which want search?\nuserID:0,ID:1")
    while True:
        searchType = input('>> ')
        if searchType.isdigit():
            if int(searchType) <= 1:
                break
        print("Input 0 or 1.")

    print("Input target.")
    target = input('>> ')
    print(search.findUser(target,int(searchType)))
