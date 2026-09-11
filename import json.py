import json

student = {"name": "张三", "score": 88}

text = json.dumps(student, ensure_ascii=False)
print(text)