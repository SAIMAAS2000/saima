import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        :"ZExy6TxP5VPhnCxMx5tGjl63I" ,
    "consumer_secret"     :"Sl3GQ6qGRmyvkA09sxOUPVc8wgpjrSHRYcFm2dKVlnmfnKREWz",
    "access_token"        :"971949240065781760-h7QFkWKUSz8hyisDTD77TgSUnPt4jjt",
    "access_token_secret" :"Z3sLwOnQHKL27cVzyEEsMVlN1RWpUuWZimJHbxZQeAs1C"

    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()