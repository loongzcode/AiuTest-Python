import os
import pytest

from utils.send_report_tg_utils import send_allure_report_to_telegram

if __name__ == "__main__":
    pytest.main(["-vs", "--alluredir", "./report/tmp", "--clean-alluredir"])
    os.system("allure generate ./report/tmp -o ./report/html --clean")
    send_allure_report_to_telegram()
    os.system("allure serve ./report/tmp -h 127.0.0.1 -p 9999")

