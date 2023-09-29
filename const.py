from datetime import datetime

FOLDER = "./data/files/"

date_time = datetime.now()
MIN = date_time.strftime("%M")
HOUR = date_time.strftime("%H")
DAY = date_time.strftime("%d")
MONTH = date_time.strftime("%b")
WK_DAY = date_time.strftime("%a")
DATE = date_time.date()