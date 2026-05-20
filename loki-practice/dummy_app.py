import random
import time
import os
from datetime import datetime, timezone

LOG_PATH = os.path.join(os.path.dirname(__file__), "logs", "app.log")

MESSAGES = {
    "INFO": [
        "User login successful",
        "Request processed",
        "Cache hit",
        "Order created",
        "Payment completed",
        "Session started",
        "File uploaded",
        "Email sent",
    ],
    "WARN": [
        "Slow query detected",
        "Cache miss",
        "Retry attempt",
        "High memory usage",
        "Rate limit approaching",
    ],
    "ERROR": [
        "Database connection failed",
        "Request timeout",
        "Unhandled exception",
        "Auth token expired",
        "Service unavailable",
    ],
}

LEVELS = random.choices(["INFO", "WARN", "ERROR"], weights=[70, 20, 10], k=1000)


def pick_level():
    return random.choices(["INFO", "WARN", "ERROR"], weights=[70, 20, 10])[0]


def write_log(f, level, message, user_id, request_id, duration_ms):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    line = (
        f'{ts} level={level:<5} message="{message}" '
        f"user_id={user_id} request_id={request_id} duration_ms={duration_ms}\n"
    )
    f.write(line)
    f.flush()
    print(line, end="")


def main():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    print(f"Writing logs to {LOG_PATH}  (Ctrl+C to stop)\n")

    with open(LOG_PATH, "a") as f:
        while True:
            level = pick_level()
            message = random.choice(MESSAGES[level])
            user_id = random.randint(1, 500)
            request_id = f"req-{random.randint(10000, 99999)}"
            duration_ms = random.randint(5, 3000)

            write_log(f, level, message, user_id, request_id, duration_ms)
            time.sleep(random.uniform(0.5, 2.0))


if __name__ == "__main__":
    main()
