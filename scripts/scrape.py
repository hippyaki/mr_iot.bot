from instascrape import Hashtag, scrape_posts
import time, os, conf

SESSIONID = ${{ secrets.SESSIONID }}
headers = {"tag-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
            "cookie": f"sessionid={SESSIONID};"}

parent_dir = "../IG_Scrape/images"
directories = ["digitalelectronics", "arduinonano", "esp8266", "esp32", "iot", "iotprojects", "homeautomation"]

mode = 0o666

try:
    for directory in directories:
        try:
            path = os.path.join(parent_dir, directory)

            os.mkdir(path, mode)

            tag = Hashtag(directory)
            tag.scrape(headers=headers)

            recents = tag.get_recent_posts()

            tag_photos = [post for post in recents if not post.is_video]

            i = 1
            for post in tag_photos:
                try:
                    post.download(f"../images/{directory}/{i}.jpg")
                    i = i+1
                    time.sleep(60)
                    if i==5:
                        break
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
except Exception as e:
    print("Error:")
    print(e)

