from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

print("BASLADI")

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("SUUD").worksheet("SUUD")

today = datetime.now().strftime("%Y-%m-%d")

sheet.append_row([
    today,
    "SISTEM TEST",
    "OK"
])

print("SHEETS YAZILDI")
