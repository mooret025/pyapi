#!/usr/bin/python3

import requests


def main():
    roverresp = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=sNsap4DVAsc1KtYf73eQUqd5dKl1d2qGOnv1Grzn").json()
    with open('/home/student/static/rover.txt', 'w') as file_obj:
        for item in roverresp['photos']:
            print(item['img_src'], file=file_obj)

if __name__ == "__main__":
    main()
