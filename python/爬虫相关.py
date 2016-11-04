#发送带有cookies的请求流程一般为首先获取cookies
mycookies = requests.get(url).headers.get("cookie")

#保持会话,使用requests.Session()可以保持会话

#使用代理
	proxies = {"http":"<a href="http://xx.xx.xx.xx:xxxx"}">http://xx.xx.xx.xx:xxxx}</a>
	response = requests.get(url=url,proxies=proxies)

#伪装浏览器,设置头部
headers = {"User-Agent":"xxxx","Referer":"xxxx"}
response = requests.get(url=url,headers=headers)