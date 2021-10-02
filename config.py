import os
class vars(object):
    api_id = os.getenv('API_ID', '38815')
    api_hash = os.getenv('API_HASH' ,'1ebf12e67222683abe1cf0209b79df')
    bot_token = os.getenv('BOT_TOKEN', '2029085800:AAEljSm1Y3psbe3Ksk_xuOAIVg_HHJImA')
    max = int(os.getenv('MAX', '20'))
