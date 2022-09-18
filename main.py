import requests
from lxml import etree

header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = "https://blog.csdn.net/it_xf?viewmode=contents"

html = requests.get(url, headers=header)

# CSDN 开启了反爬虫机制，需要修改header来避免被识别为爬虫

# print(html.text)

# Xpath
# 解释：// 定位根节点， / 往下层寻找， /text())提取文本内容， /@xxxx提取属性内容
# 表达式：//*[@id="mainBox"]/main/div[2]/div[1]/h4/a

# 我们来琢磨琢磨，首先，//表示根节点，也就是说啊，这//后面的东西为根，则说明只有一个啊
# 也就是说，我们需要的东西，在这里面
# 然后/表示往下层寻找，根据图片，也显而易见，div -> main -> div[2] -> div[1] -> h4 -> a
# 追踪到a这里，我想，你们应该也就看得懂了，然后我们在后面加个/text，表示要把元素的内容提取出来，所以我们最终的表达式长这样：

# //*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()

# 该表达式只针对这个网页的元素

etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="userSkin"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/article/a/div/h4')

# 表达式：//*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()
# 其实我们能够很容易发现，main->div[2]其实包含所有文章，只是我们取了main->div[2]->div[1]，也就是说我们只是取了第一个而已。所以，其实表达式写出这样，就可以得到所有的文章了
# 在xpath中可以更改div，带有[1]和[2]似乎就是向下的层级关系，删掉[1]保留div就可以往上一层

for each in content:
    print(each.text)