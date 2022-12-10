class Solution:
    def lengthLongestPath(self, input: str) -> int:
        dict = {}
        longest = 0
        fileList = input.split("\n")
        for i in fileList:
            if "." not in i:  #是文件夹
                key = i.count("\t") #是几级文件夹
                value = len(i.replace("\t","")) #除去\t后的长度，是实际长度
                dict[key] = value
            else: #是文件。
                key = i.count("\t")
                #　文件的长度：所有目录的长度＋文件的长度＋“\”的数量
                length = sum([dict[j] for j in dict.keys() if j < key]) + len(i.replace("\t","")) + key
                longest = max(longest,length)
        return longest