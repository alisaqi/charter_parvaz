# Charter Parvaz Bot

A Telegram bot for searching and booking charter flight tickets in Iran.

## Features

- 🇮🇷 Search domestic flights
- 🌍 Search international flights
- 💺 Real-time seat availability
- 💵 Price information with commission
- 📅 Date selection in Jalali calendar
- 👤 User profile management
- 🔔 Channel membership verification

## Requirements

- Python 3.7+
- Telegram Bot Token
- Telegram API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alisaqi/charter_parvaz.git
cd charter_parvaz
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your Telegram credentials
```

4. Run the bot:
```bash
python main.py
```

## Configuration

Create a `.env` file with the following variables:

- `TELEGRAM_API_ID`: Your Telegram API ID from https://my.telegram.org
- `TELEGRAM_API_HASH`: Your Telegram API Hash
- `TELEGRAM_BOT_TOKEN`: Your bot token from @BotFather

## Project Structure

```
charter_parvaz/
├── main.py              # Main bot logic and handlers
├── config.py            # Configuration and constants
├── charterTicket.py     # Flight data scraper
├── test.py              # Test data structures
├── requirements.txt     # Python dependencies
├── Procfile            # Heroku deployment config
└── .env.example        # Example environment variables
```

## Usage

1. Start the bot with `/start`
2. Join the required channel
3. Select flight type (domestic/international)
4. Choose departure and destination cities
5. Select travel date
6. Browse available flights
7. Contact support to complete booking

## Development

The bot uses:
- **Pyrogram**: Telegram MTProto API framework
- **BeautifulSoup4**: Web scraping for flight data
- **persiantools**: Jalali date handling

## Security

⚠️ **Important**: Never commit sensitive credentials to version control. Always use environment variables or a `.env` file (which is gitignored).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For support, contact: [@ASoDme](https://t.me/ASoDme)

## Acknowledgments

Flight data is sourced from ticket-charter.com
