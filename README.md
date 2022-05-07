# SiteMapFuck
离线生成(Offline generation) 不请求网站(Site will not be requested) 速度极快 (Etremely fast )

# 原理
# 遍历枚举物理目录,拼接URL路径
#Principle
#Traverse and enumerate physical directories and splice URLs

由于目前有些网站的JS特性，网站不能被通常的Sitemap工具枚举出列表，本人找了很多都没找到，非常的法克！
所以想到了一个野路子方法，枚举本地物理路径，拼接URL即可
最后生成3种类型的sitemap文件/txt/xml/html
