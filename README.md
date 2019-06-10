# anki_spider
Crawl english dictionary book and add it to ankidroid.

爬取网上资源制作ankidroid单词书，字段包括：单词、音标、释义、例句

**Requirements**:

- lxml
- json
- requests
- beautifulsoup4
- jupyter[optional]

**Usage**

> 从网络爬取单词、音标、释义、例句、例句释义，方便导入到ankidroid,自己制作词典
> 建议在jupyter中使用，需要配置几个参数：
>
> - book_id    单词书的ID
> - group_id的范围，每本书的范围列表
> - page_max   每个单词组的最大页数
>
> 示例链接：```http://book.qsbdc.com/word_list.php?tag=all&book_id=1732&group_id=24530```
>
> 详细使用方法：[usage](http://blog.niuhemoon.xyz/pages/2019/06/02/anki-python/)



------------------

示例anki单词包，内含800条编程常用英语词汇和注解。

链接：https://pan.baidu.com/s/1yM5Ftt_wrgdETSBA8CatCA 
提取码：w22d 
