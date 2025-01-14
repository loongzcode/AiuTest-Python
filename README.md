# AiuTest-Python
## 技术栈
```python
1. python
2. pytest
3. pymysql
4. allure
5. requests
6. openpyxl
7. pip
```
## 目录结构
|目录名|作用|
|---|---|
|config|配置信息|
|data|测试数据|
|log|日志|
|report|测试报告|
|testcase|测试脚本|
|utils|工具类|
|pytest.ini|pytest配置文件|
|run.py|启动类|
|conftest.py|夹具类，存放测试用例执行前后的数据初始化和销毁|

## 使用方法
- 先在data文件的data.xlsx里填入测试数据
- 然后在run.py点击运行即可
## data.xlsx字段介绍
|字段名称|英文(key)|用途|
|---|---|---|
|编号|id| allure报告展示|
|模块|feature|
|场景|story|
|标题|title|
|请求方式|method|http请求|
|路径|path|
|请求头|headers|
|url参数|params|
|data参数|data|
|json参数|json|
|文件参数|files|
|校验字段|check|断言和JDBC请求|
|预期结果|expected|
|数据库校验内容|sql_check|
|数据库预期结果|sql_expected|
|json提取|jsonExData|提取|
|sql提取|sqlExData|
|是否执行|is_true|分组执行|

