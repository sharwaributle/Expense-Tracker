import sqlite3
import os
from datetime import date, datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")

def seed():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Pehle user_id nikalte hain (default pehla user)
    user = cur.execute("SELECT id FROM users LIMIT 1").fetchone()
    if not user:
        print("Pehle app me register ya login karke ek user banayein!")
        conn.close()
        return

    user_id = user[0]
    today = date.today().isoformat()
    now_ts = datetime.utcnow().isoformat()

    # 2. Realistic Demo Expenses
    demo_expenses = [
        (user_id, 1200.00, "Housing", "Room Rent Advance", today, now_ts),
        (user_id, 350.00, "Food", "Team Dinner / Swiggy", today, now_ts),
        (user_id, 180.00, "Transport", "Uber to Client Office", today, now_ts),
        (user_id, 450.00, "Shopping", "Office Stationeries", today, now_ts),
        (user_id, 220.00, "Utilities", "Broadband Wi-Fi Bill", today, now_ts),
        (user_id, 90.00, "Entertainment", "Movie Night", today, now_ts),
    ]

    cur.executemany(
        """INSERT INTO expenses (user_id, amount, category, note, spent_on, created_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        demo_expenses,
    )

    # 3. Upcoming Demo Reminders
    next_week = (date.today() + timedelta(days=4)).isoformat()
    demo_reminders = [
        (user_id, "AWS Cloud Server", 45.00, next_week, "Monthly infrastructure invoice", 1, 0, now_ts),
        (user_id, "Office Internet Bill", 25.00, next_week, "High-speed broadband", 1, 0, now_ts),
    ]

    cur.executemany(
        """INSERT INTO reminders (user_id, title, amount, due_date, note, is_recurring, is_done, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        demo_reminders,
    )

    conn.commit()
    conn.close()
    print("✓ Demo data successfully inject ho gaya hai!")

if __name__ == "__main__":
    seed()