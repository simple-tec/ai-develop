import myllm
from openai.embeddings_utils import cosine_similarity

def get_cosine(sample_embedding, base_embedding):
    return cosine_similarity(sample_embedding, base_embedding)

query = "篮子里放着5种水果，分别是苹果、葡萄、梨、西瓜和香蕉"
t1_text = "篮子里5种蔬菜"
t2_text = "篮子里放着5种水果，分别是苹果、葡萄、梨、西瓜和杏"
t3_text = "篮子里放着5种水果，分别是香蕉、苹果、葡萄、梨和西瓜"
t4_text = "篮子里放着苹果、葡萄、梨、西瓜和香蕉这5种水果"
query_embs = myllm.myembeddings.embed_query(query)
t1_text_embs = myllm.myembeddings.embed_query(t1_text)
t2_text_embs = myllm.myembeddings.embed_query(t2_text)
t3_text_embs = myllm.myembeddings.embed_query(t3_text)
t4_text_embs = myllm.myembeddings.embed_query(t4_text)

cosine1 = get_cosine(query_embs, t1_text_embs)
cosine2 = get_cosine(query_embs, t2_text_embs)
cosine3 = get_cosine(query_embs, t3_text_embs)
cosine4 = get_cosine(query_embs, t4_text_embs)

print("t1 cosine : %f" % (cosine1))
print("t2 cosine : %f" % (cosine2))
print("t3 cosine : %f" % (cosine3))
print("t4 cosine : %f" % (cosine4))