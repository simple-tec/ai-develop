from langchain.text_splitter import CharacterTextSplitter

c_splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator = ' '
)
# 案例1：
# 没有匹配到separator,超过chunk_size也不切割
list = c_splitter.split_text("123456789abc")
print(list)


# 案例2：
# 匹配到一个或者多个separator的情况下，才会按照chunk_size长度切割
list = c_splitter.split_text("123456789abc 12 34 56 78 9a bc")
print(list)


# 案例3：
# 严格按照长度切割
c_splitter = CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator = ''
)
list = c_splitter.split_text("123456789abc")
print(list)