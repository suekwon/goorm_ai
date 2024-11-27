# %%
# pip install win10toast
import time
import schedule
from win10toast import ToastNotifier
# %%
toaster = ToastNotifier()
toaster.show_toast("제목", "내용", duration=10)

# %%


def lunch_notification():
    toaster = ToastNotifier()
    toaster.show_toast(
        "점심시간 알림",
        "점심시간 5분전입니다",
        # duration=10,
        threaded=True
    )


# 매일 11:31에 알림 설정
schedule.every().day.at("11:31").do(lunch_notification)

# 프로그램 계속 실행
while True:
    schedule.run_pending()
    time.sleep(1)

# %%
