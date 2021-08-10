import re
text = '''Совет. По этому запросу вы можете
найти сайты на русском языке.
Указать предпочтительные языки для 
результатов поиска можно в разделе Настройки.
+996-555-888-948
+996-505-888-448 '''

res = "и"
# result = re.match(res, text)
# print (result.group())

resul = re.findall(res, text)
print(resul)