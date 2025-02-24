import psycopg2
import os
from faker import Faker

fake = Faker()

db_url = os.getenv("DATABASE_URL", "postgresql://viacheslav:ghj123YUI@localhost:5432/task_manager")


def seed_database():
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        # Insert predefined statuses
        statuses = ['new', 'in progress', 'completed']
        cur.executemany("INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING;",
                        [(status,) for status in statuses])

        # Insert random users
        users = [(fake.name(), fake.email()) for _ in range(10)]
        cur.executemany("INSERT INTO users (fullname, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;", users)

        # Fetch user and status IDs
        cur.execute("SELECT id FROM users;")
        user_ids = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT id FROM status;")
        status_ids = [row[0] for row in cur.fetchall()]

        # Insert random tasks
        tasks = [(fake.sentence(), fake.text(), fake.random.choice(status_ids), fake.random.choice(user_ids)) for _ in
                 range(20)]
        cur.executemany("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);", tasks)

        conn.commit()
        cur.close()
        conn.close()
        print("Database seeded successfully.")
    except Exception as e:
        print(f"Error seeding database: {e}")


if __name__ == "__main__":
    seed_database()
