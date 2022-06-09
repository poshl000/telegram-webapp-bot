# telegram-webapp-bot
Telegram Web App bot example. 

Bot consists of two parts:
- webapp-backend
- webapp-frontend

## Installation

### webapp-backend

Built with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) and [peewee orm](http://docs.peewee-orm.com/en/latest/)

1. Execute in `database` directory to create sqlite file to work with peewee:

```
python3 create_database.py
```

1. Set telegram bot key in `config/config.ini`
2. Edit products price in `config/products.yml`

