# Ledger — Smart Expense Tracker

A small Flask + SQLite website with:

- **Authentication** — register/login/logout with hashed passwords and session cookies.
- **Expense tracking** — log expenses with amount, category, date, and note; see totals and a category breakdown.
- **Reminders** — set due dates for bills/payments, with a "due soon" banner on the dashboard and support for monthly recurring reminders.
- **AI chatbot** — a chat panel backed by the Groq API (Llama models) that can answer questions about your spending, using your own Groq API key.

## 1. Install

```bash
cd expense_tracker
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Configure your API key

Copy the example env file and fill in your own values:

```bash
cp .env.example .env
```

Then edit `.env`:

- `SECRET_KEY` — any long random string (used to sign login sessions).
- `GROQ_API_KEY` — get a free key at https://console.groq.com/keys
- `GROQ_MODEL` — optional, defaults to `llama-3.3-70b-versatile`.

**Never commit your real `.env` file or share your API key.**

## 3. Run it

```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser. The first run creates a local `expenses.db` SQLite file automatically.

## 4. Using the site

1. Register an account, then sign in.
2. **Expenses** — add entries with amount/category/date/note; remove any entry from the list.
3. **Reminders** — set a due date and optional amount for bills; mark them done, or check "repeats monthly" so completing one automatically reschedules it 30 days out.
4. **Ask the ledger** — chat with an assistant that knows your spending totals for the current month and can answer questions or give general budgeting suggestions.

## Notes on security

- Passwords are hashed with Werkzeug's `generate_password_hash` (never stored in plain text).
- Sessions are server-signed cookies; log out clears the session.
- The Groq API key stays on the server (in `.env`) and is never sent to the browser.
- This is a learning/demo project — for real production use, add HTTPS, CSRF protection, rate limiting, and a production-grade database (e.g. Postgres).

## Project structure

```
expense_tracker/
├── app.py                # Flask app: routes, auth, DB, Groq integration
├── requirements.txt
├── .env.example
├── templates/             # Jinja2 HTML templates
└── static/
    ├── style.css          # Ledger-inspired visual design
    └── script.js          # Chat panel AJAX
```
