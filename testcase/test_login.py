import pytest
import requests
from utils.excel_util import read_excel
from utils.rest_util import get_rest


class TestLogin:
    data = read_excel("./data/data.xlsx")

    @pytest.mark.parametrize("case",data)
    def test_login(self,case):
        case_data = get_rest(case)
        request_data = case_data

        res = requests.request(**request_data)
        assert res.json()["msg"] == case["expected"]
