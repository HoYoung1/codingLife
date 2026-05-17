import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent

AOAI_ENDPOINT = os.getenv("AOAI_ENDPOINT")
AOAI_API_KEY = os.getenv("AOAI_API_KEY")
AOAI_DEPLOY_GPT4O_MINI = os.getenv("AOAI_DEPLOY_GPT4O_MINI", "gpt-4o-mini")
AOAI_DEPLOY_GPT4O = os.getenv("AOAI_DEPLOY_GPT4O", "gpt-4o")
AOAI_DEPLOY_EMBED_3_SMALL = os.getenv("AOAI_DEPLOY_EMBED_3_SMALL", "text-embedding-3-small")
AOAI_API_VERSION = "2024-02-01"

DATA_DIR = BASE_DIR / "data"
CONTRACTS_DIR = DATA_DIR / "contracts"
VECTOR_STORE_DIR = BASE_DIR / "vector_store"

CARD_CSV = DATA_DIR / "access_cards.csv"
ENROLLMENT_CSV = DATA_DIR / "training_enrollment.csv"
ATTENDANCE_CSV = DATA_DIR / "training_attendance.csv"

CARD_ALERT_DAYS = 30
