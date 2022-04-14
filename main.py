from instabot import Bot
import time, os.path
import conf
 
directories = ["esp8266", "arduinonano" , "esp32", "iot", "iotprojects", "homeautomation", "digitalelectronics"]
i=1
bot = Bot()

bot.login(username = conf.username, password = conf.password)
            
try:
    for directory in directories:
        for i in range(5):
            
            filename = f"images/{directory}/{i}.jpg"
            file = os.path.exists(filename)
            if file: 
                bot.upload_photo(filename,caption =f"Follow : @mr_iot.bot & @school_of_iot \n.\nSource : @{directory}\n.\nTags ⏬\n____________\n#arduino #arduinoproject #arduinouno #arduinofun #embedded #digitalelectronics #arduinonano #arduinoprogramming #arduinoprojects  #arduinoproject #arduinomega #arduinolove #electronics #diyelectronics #raspberrypi4 #raspberrypi3 #raspberrypi")
                print(f"Posted photo - {i} from {directory}")
                time.sleep(43200)
            i = i + 1
            
except Exception as e:
    print("Error:")
    print(e)

