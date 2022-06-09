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
3. Run bot using
   
```
python3 bot.py
```

Note that bot use infinity_polling so need to started i background. Use tools like [Monit](https://mmonit.com/monit/) for control bot script.

### webapp-frontend

Simpe interface built with react and react-bootstrap

1. Set products data in `src/catalog/state.js`
2. Run `npm start` for test
3. `npm run build` for build

