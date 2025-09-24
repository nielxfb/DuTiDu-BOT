# DuTiDu Bot 🤖

A LINE Bot for managing and querying student schedules and shift information. This bot is designed to help students and staff easily access schedule information through simple commands.

## Features

- **Schedule Lookup**: Check individual schedule details by student initial and day
- **Shift Information**: View shift assignments (Morning/Night) for specific days
- **Multi-language Support**: Commands available in Indonesian (/jadwal) and English (/schedule)
- **RESTful Webhook**: Integrates with LINE Messaging API
- **Dockerized**: Ready for deployment with Docker and Docker Compose

## Commands

| Command | Aliases | Description | Usage |
|---------|---------|-------------|-------|
| `/schedule` | `/jadwal` | Get schedule for a specific student on a specific day | `/schedule XX 1` |
| `/shift` | `/sh` | Get shift information for a specific day | `/shift 1` |
| `/help` | - | Show available commands | `/help` |

### Day Numbers
- `1` = Monday
- `2` = Tuesday  
- `3` = Wednesday
- `4` = Thursday
- `5` = Friday
- `6` = Saturday

### Examples
```
/schedule AB 1          # Get AB's Monday schedule
/jadwal CD 3           # Get CD's Wednesday schedule (Indonesian)
/shift 2               # Get Tuesday shift assignments
/sh 5                  # Get Friday shift assignments
```

## Setup

### Prerequisites
- Python 3.13+
- LINE Developer Account
- LINE Bot Channel

### Environment Variables
Create a `.env` file in the root directory:

```env
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token_here
LINE_CHANNEL_SECRET=your_line_channel_secret_here
```

### Schedule Data
1. Copy the example schedule file:
   ```bash
   cp datas/schedule.json.example datas/schedule.json
   ```

2. Update `datas/schedule.json` with your actual schedule data. The structure should follow:
   ```json
   {
     "monday": {
       "XX23-2": {
         "shift": "P",
         "scheduleDetails": [
           {
             "shiftSchedule": {
               "name": "Class Name",
               "startTime": "08:00",
               "endTime": "10:00"
             },
             "description": "Course Description"
           }
         ]
       }
     }
   }
   ```

### Installation Options

#### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/nielxfb/DuTiDu-BOT.git
cd DuTiDu-BOT

# Create and configure your .env file
cp .env.example .env
# Edit .env with your LINE credentials

# Run with Docker Compose
docker-compose up -d
```

#### Option 2: Local Development
```bash
# Clone the repository
git clone https://github.com/nielxfb/DuTiDu-BOT.git
cd DuTiDu-BOT

# Install dependencies
pip install -r requirements.txt

# Create and configure your .env file
cp .env.example .env
# Edit .env with your LINE credentials

# Run the application
python app.py
```

## Project Structure

```
dutidu-bot/
├── app.py                    # Main Flask application and webhook handler
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose configuration
├── controllers/             # Command handlers
│   ├── help.py             # Help command handler
│   ├── schedule.py         # Schedule lookup handler
│   └── shift.py            # Shift information handler
├── datas/                  # Data management
│   ├── load.py            # Data loader utility
│   ├── schedule.json      # Schedule data (not in repo)
│   └── schedule.json.example # Example schedule structure
└── util/                  # Utilities
    └── commands.py        # Command routing configuration
```

## API Endpoints

- `POST /webhook` - LINE Bot webhook endpoint for receiving messages

## LINE Bot Setup

1. Create a LINE Bot account at [LINE Developers Console](https://developers.line.biz/)
2. Create a new Messaging API channel
3. Get your Channel Access Token and Channel Secret
4. Set the webhook URL to your deployed application: `https://your-domain.com/webhook`
5. Enable "Use webhook" in your channel settings

## Deployment

### Using Docker
The application is containerized and ready for deployment on any platform that supports Docker:

- **Port**: 8000
- **Health Check**: Available via HTTP requests to `/webhook`
- **Environment**: Production-ready with Gunicorn WSGI server
- **Workers**: Configured with 2 sync workers for optimal performance

### Environment Requirements
- Minimum 512MB RAM
- Python 3.13+ support
- Network access for LINE API calls

## Development

### Adding New Commands
1. Create a new handler function in `controllers/`
2. Add command aliases and handler to `util/commands.py`
3. Update help message in `controllers/help.py`

### Data Structure
The schedule data follows a hierarchical structure:
- **Days** → **Student Initials** → **Schedule Details**
- Supports shift assignments (P=Pagi/Morning, M=Malam/Night)
- Flexible schedule detail format with time slots and descriptions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or support, please open an issue in the GitHub repository.

---

**Note**: Make sure to keep your LINE Bot credentials secure and never commit them to the repository. Always use environment variables for sensitive configuration.
