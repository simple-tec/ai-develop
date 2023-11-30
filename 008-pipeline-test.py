from transformers import pipeline
classifier = pipeline(model="uer/roberta-base-finetuned-jd-binary-chinese", task="sentiment-analysis", device=-1)
preds = classifier("这个餐馆太难吃了。")
print(preds)

