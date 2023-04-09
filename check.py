# train.json 데이터를 확인하는 코드
import json 
with open('data/train.json', 'r') as f:
    train_data = json.load(f) 
train_data = [item for topic in train_data['data'] for item in topic['paragraphs'] ]

# 넘 많으니까 1000개만 데이터 사용하기
using_num_sample = 1000
train_data = train_data[:using_num_sample]

print(train_data)