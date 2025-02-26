import requests
import os
import json
import matplotlib.pyplot as plt
import io
import numpy as np

# Telegram Bot Token 和 Chat ID
BOT_TOKEN = "8066724727:AAETF9yyI1m-i70PxKPNRXpxtjKvT_pX3_U"
CHAT_ID = "7481915128"

# Allure 报告目录
ALLURE_REPORT_DIR = "report"  # 替换为你的 Allure 报告目录

def send_telegram_message(message):
    """发送 Telegram 消息."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"  # 支持 HTML 格式
    }
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # 检查是否有 HTTP 错误
        print("Telegram message sent successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")

def create_bar_chart(total, passed, failed, skipped, broken):
    """创建柱状图."""
    labels = ['总测试用例数', '通过', '失败', '跳过', '损坏']
    values = [total, passed, failed, skipped, broken]
    colors = ['blue', 'green', 'red', 'orange', 'purple']

    x = np.arange(len(labels))  # the label locations
    width = 0.7  # the width of the bars

    fig, ax = plt.subplots()
    rects = ax.bar(x, values, width, color=colors)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Tests')
    ax.set_title('Allure 报告摘要图表')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(rects[:1], ['Tests'])  # Only need one legend entry

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects)

    fig.tight_layout()

    # Save the plot to a BytesIO object
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)  # Rewind to the beginning of the buffer
    plt.close(fig)  # Close the figure to free memory

    return img_buf

def send_photo_to_telegram(image_data, caption="Allure Report Summary"):
    """发送图片到 Telegram."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": image_data}
    data = {"chat_id": CHAT_ID, "caption": caption}
    try:
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        print("Photo sent to Telegram successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending photo to Telegram: {e}")

def send_allure_report_to_telegram():
    """发送 Allure 报告到 Telegram."""

    # 1. 生成 Allure 报告 (如果还没有生成)
    # 假设你已经有生成 Allure 报告的命令，例如：
    # os.system("allure generate allure-results -o allure_report --clean")

    # 2. 压缩 Allure 报告
    report_zip_path = "allure_report.zip"
    os.system(f"zip -r {report_zip_path} {ALLURE_REPORT_DIR}")

    # 3. 发送压缩包
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(report_zip_path, "rb") as f:
        files = {"document": f}
        data = {"chat_id": CHAT_ID}
        try:
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            print("Allure report sent to Telegram successfully.")
        except requests.exceptions.RequestException as e:
            print(f"Error sending Allure report to Telegram: {e}")

    # 4. (可选) 发送报告的摘要信息
    try:
        summary_file_path = os.path.join(ALLURE_REPORT_DIR, "html/widgets", "summary.json")
        with open(summary_file_path, "r") as f:
            summary = json.load(f)

        total_tests = summary["statistic"]["total"]
        passed_tests = summary["statistic"]["passed"]
        failed_tests = summary["statistic"]["failed"]
        skipped_tests = summary["statistic"]["skipped"]
        broken_tests = summary["statistic"]["broken"]

        # Create and send the bar chart
        image_data = create_bar_chart(total_tests, passed_tests, failed_tests, skipped_tests, broken_tests)
        send_photo_to_telegram(image_data)


#         summary_message = f"""
# <b>Allure 报告摘要：</b>
# 总测试用例数: {total_tests}
# 通过: {passed_tests}
# 失败: {failed_tests}
# 跳过: {skipped_tests}
# 损坏: {broken_tests}
# """
#         send_telegram_message(summary_message)

    except FileNotFoundError:
        print(f"Error: summary.json not found in {ALLURE_REPORT_DIR}/widgets/")
        send_telegram_message("Failed to get Allure report summary (summary.json not found).")
    except json.JSONDecodeError:
        print(f"Error: Could not decode summary.json in {ALLURE_REPORT_DIR}/widgets/")
        send_telegram_message("Failed to get Allure report summary (Could not decode summary.json).")
    except KeyError as e:
        print(f"Error: Key not found in summary.json: {e}")
        send_telegram_message(f"Failed to get Allure report summary (Key not found: {e}).")
    except Exception as e:
        print(f"Error getting Allure report summary: {e}")
        send_telegram_message("Failed to get Allure report summary.")

# Example usage (you'll need to adapt this to your specific workflow)
# if __name__ == "__main__":
#     send_allure_report_to_telegram()
