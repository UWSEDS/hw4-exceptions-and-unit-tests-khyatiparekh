import urllib.request
import os
def get_data(url):
    try:
        testfile = urllib.request.URLopener()
        name = url.rsplit('/', 1)[-1]
        filename = os.path.join('/Users/jayeshparekh/Downloads', name)
        print('hello')
        if not os.path.isfile(filename):
            testfile.retrieve(url, filename)
            print("File downloaded successfully")
        else:
            print("File already exists")
    except urllib.error.URLError:
        print("URL does not point to an existing file")
        ##no action

def delete_data(url):
    name = url.rsplit('/', 1)[-1]
    filename = os.path.join('/Users/jayeshparekh/Downloads', name)
    if os.path.isfile(filename):
        os.remove(filename)
        print("File removed")
    else:
        print("No file to delete")


def main():
    get_data( https://data.seattle.gov/resource/4xy5-26gy.csv)

main()