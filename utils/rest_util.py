def get_rest(case):
    method = case["method"]
    url = "http://212.50.233.129:81/" + case["path"]
    headers = eval(case["headers"]) if isinstance(["headers"],str) else None
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
    return request_data
