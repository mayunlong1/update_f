import yaml
from datetime import datetime

print(yaml.safe_load(open('data/config.yaml', encoding='utf-8')))
# 获取当前时间
current_time = datetime.now()
yaml.safe_dump([current_time], open('data/config.yaml','w', encoding='utf-8'))