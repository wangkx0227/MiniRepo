import requests
import json

ZABBIX_URL = "http://192.168.85.143/zabbix"
USERNAME = "Admin"
PASSWORD = "zabbix"

# 要修改的主机名 和 实际 IP
HOSTNAME = "zabbix-proxy"
NEW_IP = "192.168.85.201"


# 登录获取 Token
def login():
    payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": USERNAME,
            "password": PASSWORD
        },
        "id": 1
    }
    res = requests.post(ZABBIX_URL + "/api_jsonrpc.php", json=payload)
    return res.json()["result"]


# 获取主机接口 ID
def get_interface_id(auth):
    payload = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "filter": {
                "host": [HOSTNAME]
            },
            "selectInterfaces": ["interfaceid", "ip"]
        },
        "auth": auth,
        "id": 2
    }
    res = requests.post(ZABBIX_URL + "/api_jsonrpc.php", json=payload)
    result = res.json()["result"]
    if not result:
        raise Exception("未找到主机：" + HOSTNAME)
    interface = result[0]["interfaces"][0]
    return interface["interfaceid"]


# 更新接口 IP
def update_ip(auth, interfaceid):
    payload = {
        "jsonrpc": "2.0",
        "method": "hostinterface.update",
        "params": {
            "interfaceid": interfaceid,
            "ip": NEW_IP
        },
        "auth": auth,
        "id": 3
    }
    res = requests.post(ZABBIX_URL + "/api_jsonrpc.php", json=payload)
    print(res.json())


if __name__ == "__main__":
    token = login()
    iface_id = get_interface_id(token)
    update_ip(token, iface_id)
