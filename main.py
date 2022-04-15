from instabot import Bot
import time, os

directories = ["arduinonano" , "esp8266", "esp32", "iot", "iotprojects", "homeautomation", "digitalelectronics"]
i=1
bot = Bot()

bot.login(username = os.environ.get("USERNAME"), password = os.environ.get("PASSWORD"))

try:
    for directory in directories:
        for i in range(5):
            
            filename = f"../images/{directory}/{i}.jpg"
            file = os.path.exists(filename)
            if file: 
                bot.upload_photo(filename,caption =f"Follow : @mr_iot.bot & @school_of_iot \n.\nSource : Unknown\nTag scrape: #{directory}\n.\nTags ⏬\n____________\n#arduino #arduinoproject #arduinouno #arduinofun #embedded #digitalelectronics #arduinonano #arduinoprogramming #arduinoprojects  #arduinoproject #arduinomega #arduinolove #electronics #diyelectronics #raspberrypi4 #raspberrypi3 #raspberrypi", upload_id=None, from_video=False)
                #bot.upload_photo(filename, caption = "This is a caption", upload_id=None, from_video=False)
                
                print(f"Posted photo - {i} from {directory}")
                print("")
                time.sleep(3600) # 60 mins
            i = i + 1
            
            
except Exception as e:
    print("Error:")
    print(e)

