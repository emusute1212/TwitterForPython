from OAuth import OAuth
from Search import Search

if __name__ == "__main__":
    certification = OAuth("Config.py")
    twitter=certification.oauth()
    search = Search(twitter)

    print("Input target id.\nTarget id is \"https://twitter.com/(User_ID)/status/(Target_ID)\"")
    target = input('>> ')
    print(search.findTweet(target))
