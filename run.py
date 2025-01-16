import os
import pytest


if __name__ == "__main__":
    pytest.main(["-vs", "--alluredir", "./report/tmp", "--clean-alluredir"])
    os.system("allure generate ./report/tmp -o ./report/html --clean")
    # os.system("allure serve ./report/tmp -h 127.0.0.1 -p 9999")