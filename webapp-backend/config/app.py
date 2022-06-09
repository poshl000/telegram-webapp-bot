from configparser import ConfigParser

def telegram_key():
    parser = ConfigParser()
    parser.read('./config/config.ini')
    api_key = parser.get('telegram', 'key')
    return api_key
    
