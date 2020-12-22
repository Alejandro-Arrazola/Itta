import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
ITEM_SHEET = "items"
CLIENT_SHEET = 'items'
SPREAD_SHEET_KEY = "1NOqIWV5xVBagI_8OwMWNP2FUrFjVAE5tKnsMvVO1y5A"
CREDS_JSON = "Config\Itta-109ed1ef7cab.json"

class gsheet_helper:
    def __init__(self):
        scope=["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            CREDS_JSON,
            scope
        )
        self.client = gspread.authorize(creds)
        self.gsheet = self.client.open_by_key(SPREAD_SHEET_KEY)
    def get_items(self):
        items = self.get_sheet(ITEM_SHEET)
        return items
    def get_sheet(self,sheet_name):
        sheet = self.gsheet.worksheet(CLIENT_SHEET)
        items = pd.DataFrame(sheet.get_all_records())
        return items
    def store_user(self, user_dic):
        sheet = self.gsheet.worksheet(CLIENT_SHEET)
        clients = pd.Dataframe(self.get_sheet(CLIENT_SHEET))

        cond = clients[clients["id"] == user_dic["id"]].empty
        if cond:
            sheet.add_rows(1)
            sheet.append_row([element for element in user_dic.values()])
        else:
            print("mi vieja burra ya no es lo que era ya no es lo que era")
    def set_data(self,data):
        sheet = self.gsheet.worksheet(CLIENT_SHEET)
        sheet.append_row(data)
if __name__ == "__main__":
    print(gsheet_helper().get_items())