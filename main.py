from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets bağlantısı
scopes = ["https://docs.google.com/spreadsheets/d/16ZJmLx86ZZu2PjnCQ-K2SCOGijSNbGnAJoYOp86i8vY/edit?gid=0#gid=0"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("SUUD").sheet1  # SHEET ADI BURASI

today = datetime.now().strftime("%Y-%m-%d")

sheet.append_row([
    today,
    "TEST ÜRÜN",
    "ZARA",
    "2999 TL"
])
