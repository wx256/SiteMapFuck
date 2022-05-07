import os, re


def make_sitemap(domain_realpath, sitemap_type, sitemap_outpath):
    total = 0
    sitemap = ''

    for dirpath, dirnames, filenames in os.walk(domain_realpath):
        for filename in filenames:
            if str(filename).endswith('html'):
                # --------------------------合成txt--------------------------
                if sitemap_type == 'txt':
                    sitemap = sitemap + '%s%s/%s\n' % (domain, (dirpath.replace(domain_realpath, '')), filename)
                    print(sitemap)


                # --------------------------合成xml--------------------------
                if sitemap_type == 'xml':
                    sitemap_xmp_body = '''<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">%s</urlset>  '''  # 这段HTML最好左对齐,不然生成出来的就不好看了

                    row = '''  
<url>
    <loc>%s</loc>
    <priority>1.00</priority>
</url>\n'''  # 这段XML最好左对齐,不然生成出来的就不好看了
                    href = '%s%s/%s' % (domain, (dirpath.replace(domain_realpath, '')), filename)
                    sitemap = sitemap + row % (href)
                    print(href)



                # --------------------------合成html--------------------------
                if sitemap_type == 'html':
                    sitemap_html_body = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>SiteMap</title>
</head>
<body>
<ul>
%s
</ul>
</body>
</html>
                    '''  # 这段HTML最好左对齐,不然生成出来的就不好看了
                    li = '''<li class="aurl"><a href="%s" data-lastfrom="%s" title="%s">%s</a></li>\n'''

                    f_html_handle = open(os.path.join(dirpath, filename), 'r')
                    f_html = f_html_handle.read()
                    try:
                        title = re.findall(r'<title>(.*?)</title>', f_html)[0]
                    except:
                        title = ""

                    if title:
                        href = '%s%s/%s' % (domain, (dirpath.replace(domain_realpath, '')), filename)
                        sitemap = sitemap + li % (href, title, title, title)
                        print(href)

                total += 1

    if sitemap_type == 'xml':
        sitemap = sitemap_xmp_body % (sitemap)
    if sitemap_type == 'html':
        sitemap = sitemap_html_body % (sitemap)

    f = open(sitemap_outpath, 'w')
    f.write(sitemap)
    f.close()
    print("total:%s" % total)


#------------------------run------------------------
domain = "https://www.wx256.com"             # 全程离线生成,不会访问该域名,仅用作于拼接
domain_realpath = "/opt/django/wx256_front"  # 网站的真是路径,用于扫描本地的html文件
sitemap_type = 'html'                        # txt,xml,html
sitemap_outpath = '/opt/django/wx256_front/sitemap.html'  # 输出的路径
make_sitemap(domain_realpath, sitemap_type, sitemap_outpath)


# 原理
# 遍历枚举物理目录,拼接URL路径
#Principle
#Traverse and enumerate physical directories and splice URLs



#out file example
#txt
# https://www.wx256.com/view/document/tab.html
# https://www.wx256.com/view/document/treetable.html
# https://www.wx256.com/view/document/card.html
# https://www.wx256.com/view/document/tinymce.html
# https://www.wx256.com/view/document/dtree.html
# https://www.wx256.com/view/document/area.html
# https://www.wx256.com/view/document/select.html
# https://www.wx256.com/view/document/tabContent.html
# https://www.wx256.com/view/document/notice.html


#xml
# < ?xml
# version = "1.0"
# encoding = "utf-8"? >
# < urlset
# xmlns = "http://www.sitemaps.org/schemas/sitemap/0.9"
# xmlns: xsi = "http://www.w3.org/2001/XMLSchema-instance"
# xsi: schemaLocation = "http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" >
# < url >
# < loc > https: // www.wx256.com / sitemap.html < / loc >
# < priority > 1.00 < / priority >
# < / url >
#
# < url >
# < loc > https: // www.wx256.com / login.html < / loc >
# < priority > 1.00 < / priority >
# < / url >
# </urlset>



#html
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <title>SiteMap</title>
# </head>
# <body>
# <ul>
# <li class="aurl"><a href="https://www.wx256.com/sitemap.html" data-lastfrom="SiteMap" title="SiteMap">SiteMap</a></li>
# <li class="aurl"><a href="https://www.wx256.com/login.html" data-lastfrom="Wecent Admin" title="Wecent Admin">Wecent Admin</a></li>
# <li class="aurl"><a href="https://www.wx256.com/index.html" data-lastfrom="Wecent Admin" title="Wecent Admin">Wecent Admin</a></li>
# </body>
# </html>
