import yaml
from datetime import datetime

print(yaml.safe_load(open('data/config.yaml', encoding='utf-8')), 1111111111)
# 获取当前时间
current_time = datetime.now()
print(current_time, 2222222222)
yaml.safe_dump([str(current_time)], open('data/config.yaml','w', encoding='utf-8'))

print(123456)
