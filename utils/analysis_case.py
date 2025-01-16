import logging
import allure

from config.config import BASE_URL


@allure.step("1.解析请求数据")
def analysis_case(case):
    method = case["method"]
    url = BASE_URL + case["path"]
    headers = eval(case["headers"]) if isinstance(case["headers"],str) else None
    data = eval(case["data"]) if isinstance(case["data"],str) else None
    json = eval(case["json"]) if isinstance(case["json"],str) else None
    files = eval(case["files"]) if isinstance(case["files"],str) else None
    request_data = {
       "method" : method,
        "url" : url,
        "headers" : headers,
        "data" : data,
        "json" : json,          
        "files" : files
    }

    logging.info(f"1.解析请求数据, 请求数据为: {request_data}")
    return request_data
