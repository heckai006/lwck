import requests
from bs4 import BeautifulSoup
import time

URL = "https://pokemmo.lanbizi.com/alpha-spawn"

def get_latest_alpha():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        resp = requests.get(URL, headers=headers, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        table = soup.find("table", id="alphaTable")
        if not table:
            return "未找到数据"

        first = table.find("tbody").find_all("tr")[0]
        tds = first.find_all("td")

        return f"""
【最新头目】
宝可梦：{tds[0].text.strip()}
等级：{tds[1].text.strip()}
地点：{tds[2].text.strip()}
时间：{tds[3].text.strip()}
"""
    except Exception as e:
        return f"错误：{str(e)}"

if __name__ == "__main__":
    print("✅ PokeMMO 头目监控已启动")
    while True:
        print(get_latest_alpha())
        time.sleep(60)
