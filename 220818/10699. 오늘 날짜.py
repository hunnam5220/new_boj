from datetime import datetime
# 현재 시간 기준 -12시간 이전
print("{}-{:02}-{:02}".format(datetime.now().year, datetime.now().month, datetime.now().day + 1))