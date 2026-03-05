# 📍 Bukamalu - Two-Way Location Sharing

A simple, privacy-focused web app that allows two people to share their locations with each other in real-time. Perfect for helping visitors find their way to your location.

## Features

- ✅ **One-click sharing** - Create a shareable link instantly
- ✅ **Two-way location** - Both parties see each other on the map
- ✅ **Live updates** - Locations update in real-time
- ✅ **No registration** - No login or account needed
- ✅ **Privacy first** - Sessions auto-expire, no permanent storage
- ✅ **Mobile friendly** - Works great on phones
- ✅ **Elder friendly** - Big buttons, clear text, simple UI

## How It Works

1. **Host** opens the app and clicks "Share My Location"
2. A unique link is generated
3. Host sends the link to the **Visitor** (via WhatsApp, SMS, etc.)
4. Visitor opens the link and allows location access
5. Both can now see each other on the map!

## Tech Stack

- **Backend**: Django 4.2
- **Database**: SQLite (can be changed to PostgreSQL)
- **Maps**: Leaflet.js with OpenStreetMap tiles
- **Frontend**: Vanilla HTML, CSS, JavaScript

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone or download the project**

```bash
cd bukamalu
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

6. **Open in browser**

Visit `http://localhost:8000`

## Production Deployment

For production, make sure to:

1. Set `DEBUG=False` in settings
2. Set a secure `DJANGO_SECRET_KEY` environment variable
3. Configure `ALLOWED_HOSTS` properly
4. Use a production database (PostgreSQL recommended)
5. Serve static files with a web server (nginx/Apache)
6. Use HTTPS (required for geolocation on most browsers)

### Environment Variables

```bash
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
# Optional: Mapbox map tiles (get a public token at https://account.mapbox.com/)
MAPBOX_ACCESS_TOKEN=pk.your_mapbox_public_token
```

## Project Structure

```
bukamalu/
├── app/                    # Main Django app
│   ├── models.py          # LocationSession model
│   ├── views.py           # Views and API endpoints
│   └── urls.py            # URL routing
├── bukamalu/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html          # Share button page
│   ├── share.html         # Visitor view
│   └── host.html          # Host view
├── static/
│   ├── css/style.css      # Styles
│   └── js/location.js     # Location utilities
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with share button |
| `/share/<code>` | GET | Visitor map view |
| `/host/<code>` | GET | Host map view |
| `/api/create-session` | POST | Create new session |
| `/api/update/<code>` | POST | Update location |
| `/api/locations/<code>` | GET | Get both locations |
| `/api/stop/<code>` | POST | Stop session |

## Privacy & Security

- Location is shared only with explicit permission
- Sessions automatically expire after 2 hours
- No user accounts or personal data stored
- Location data deleted when session ends
- HTTPS required for geolocation in production

## Browser Support

- Chrome 50+
- Firefox 55+
- Safari 10+
- Edge 79+
- Mobile browsers (iOS Safari, Chrome for Android)

**Note**: Geolocation requires HTTPS in production (localhost works for development).

## License

MIT License - Feel free to use and modify!

## Contributing

Contributions welcome! Please feel free to submit issues or pull requests.
