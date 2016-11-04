import requests
stockList = []
crawlSite = "http://hq.sinajs.cn/list=s_sh000001"
res = requests.get(crawlSite)
data = res.content
stockList = data.split(",")

#获取页面代码
html = requests.get(url).text
#用beautifulSoup解析页面
soup = BeautifulSoup(html)
#使用css selecetor或者xpath选取页面信息
#获取超链接地址
href = soup.xpath("//a/@href")
#获取文本信息
text = soup.xpath("//li/a/text()")
#获取图片信息
imgSrc = soup.xpath("//a//course/123456789/img/@src")