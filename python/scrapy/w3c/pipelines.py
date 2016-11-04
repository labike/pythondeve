import json
import codecs

class W3CPipeline(object):
	def __init__(self):
		#打开文件
		self.file = codecs.open("w3c.json","wb",encoding="utf-8")
	def process_item(self,item,spider):
		line = json.dumps(item["title"],ensure_ascii=False) + "\t"
		line = line + json.dumps(item["link"],ensure_ascii=False) + "\t"
		line = line + json.dumps(item["link"],ensure_ascii=False) + "\t"
		#写入文件
		self.file.write(line)