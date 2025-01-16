import logging
from jinja2 import Template
import pytest
from config.config import EXCEL_FILE, SHEET_NAME
from utils.allure_utils import allure_init
from utils.asserts_utlis import http_assert, jdbc_assert
from utils.excel_util import read_excel
from utils.analysis_case import analysis_case
from utils.extractor_utils import jdbc_extractor, json_extractor
from utils.send_request import send_http_request


class TestLogin:
    data = read_excel(file_path=EXCEL_FILE,sheet_name=SHEET_NAME)
    all = {}

    @pytest.mark.parametrize("case",data)
    def test_login(self,case):
        
        all = self.all

        # 模板渲染
        case = eval(Template(str(case)).render(all))

        # allure 初始化
        allure_init(case) 

        # 测试用例的描述信息日志
        logging.info(f"0.用例ID:{case["id"]} 模块:{case["feature"]} 场景:{case["story"]} 标题:{case["title"]}")

        # 解析用例数据
        request_data = analysis_case(case)

        # 发送请求
        res = send_http_request(**request_data)
        
        # http断言
        http_assert(case, res)

        # 数据库断言
        jdbc_assert(case)

        # json提取
        json_extractor(case,all,res)
            
        # 数据库提取
        jdbc_extractor(case,all)