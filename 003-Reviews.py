import openai
import os
from openai.embeddings_utils import cosine_similarity
import myllm

# 获取"好评"这个关键字的embedding
positive_review = myllm.my_get_embedding("好评")
# 获取"差评"这个关键字的embedding
negative_review = myllm.my_get_embedding("差评")
# 获取"好评"的embedding
positive_example = myllm.my_get_embedding("一次买了两本，对于买书这块不能省，必须京东正版。认知边界扩展，获得的价值远超书本价格")
# 获取"差评"的embedding
negative_example = myllm.my_get_embedding("内容才刚看不做评价。纸张质量很差，感觉受过潮一样，纸很薄像极了盗版……这是这么多年买的书页质量最差的一本。")

def get_score(sample_embedding):
  return cosine_similarity(sample_embedding, positive_review) - cosine_similarity(sample_embedding, negative_review)

positive_score = get_score(positive_example)
negative_score = get_score(negative_example)

print("好评例子的评分 : %f" % (positive_score))
print("差评例子的评分 : %f" % (negative_score))