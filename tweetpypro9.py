import os
import time
import

consumer_key=ZExy6TxP5VPhnCxMx5tGjl63I
consume_secret=Sl3GQ6qGRmyvkA09sxOUPVc8wgpjrSHRYcFm2dKVlnmfnKREWz

def get_api(cfg):
  auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
  auth.set_accessZExy6TxP5VPhnCxMx5tGjl63I  api= tweepy.API(auth)
  a=0
  b=1
while(a<2):
    img="/home?user/rip/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 1200*800 "+img
    os.system(cmd)
    print("selfie taken")
    file =open(img,'rb')
    data =file.read()
    api.update_wit_media(img,status="pic of the day")
    print("wait for 5 seconds selfie")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
