# hellopython
需求：获取目标网址的中每一天的水情公报，并保存进excel进行下一步处理。
分析水情公报url知，http://www.sxmwr.gov.cn/gb-zxfw-news-3-list-79501 中，list后数字并非序列，不规范。因此需要先抓取水情公报栏目每一页所有天的水情公报链接，然后，进入每一链接抓取公报内容存储为本地文件。
详细步骤参考：http://www.jianshu.com/p/eacde7b9cce2
