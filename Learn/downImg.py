import random
import urllib.request

def save_img(url):
    num = random.randrange(1,1000)
    name = str(num) + ".jpg"
    urllib.request.urlretrieve(url,name)

save_img("https://kellyjackson2102.files.wordpress.com/2016/05/food-clipart-07.jpg")
