《用Python写网络爬虫》（第2版）源代码

中文书名：用Python写网络爬虫
英文书名：Python Web Scraping Second Edition

作者：
    [德] 凯瑟琳·雅姆尔（Katharine Jarmul）
    [澳] 理查德·劳森（Richard Lawson）

译者：
    李斌

出版社：
    人民邮电出版社

ISBN：
    978-7-115-47967-9

源代码下载地址：
    https://www.epubit.com/bookDetails?id=N33225
    https://box.lenovo.com/l/yJ4Vfj                 提出码：6f7c

示例网站运行注意事项：
1. 下载 web2py
    wget http://www.web2py.com/examples/static/web2py_src.zip
    unzip web2py_src.zip

2. 下载网站代码
    cd web2py/applications
    wget http://download.python-scraping.com/wswp-places.zip
    unzip wswp-places.zip

3. 运行网站
    cd ..
    python web2py.py --password=<password>

在运行示例网站前需要修改示例网站源代码中的 places/models/1_db.py  文件的如下代码：
    response.generic_patterns = ['*'] if request.is_local else []

    from gluon.tools import Auth, Crud, Service, PluginManager, Recaptcha, prettydate
    auth = Auth(db)

    crud, service, plugins = Crud(db), Service(), PluginManager()

中的  Recaptcha 修改为 Recaptcha2:
    response.generic_patterns = ['*'] if request.is_local else []

    from gluon.tools import Auth, Crud, Service, PluginManager, Recaptcha2, prettydate
    auth = Auth(db)

    crud, service, plugins = Crud(db), Service(), PluginManager()

注意：运行示例网站需要使用 Python 2.x 来运行，否则会报错。



Chapter01   第1章 网络爬虫简介                                         ===> 介绍了什么是网络爬虫，以及如何爬取网站
    01. Download.py                                                 ===> 使用 urllib 模块下载网页
    02. SafeDownload.py                                             ===> 更稳健的下载网页的方法
    03. RetryDownload.py                                            ===> 支持重试的下载网页方法
    04. UserAgentDownload.py                                        ===> 支持设置代理的下载网页方法
    05. CrawlSitemap.py                                             ===> 爬取网站地图数据
    06. IdIterationCrawler.py                                       ===> ID 遍历爬虫
    07. IdIterationCrawler02.py                                     ===> ID 遍历爬虫改进版，允许下载错误多次后才退出
    08. LinkCrawler.py                                              ===> 只下载符合要求的页面
    09. RobotParser.py                                              ===> 解析 robots.txt 文件
    10. RobotsLinkCrawler.py                                        ===> 在 LinkCrawler.py 的基础上添加 robots.txt 文件的解析
    11. ProxyDownload.py                                            ===> 支持代理的网页下载方法
    12. Throttle.py                                                 ===> 实现下载限速的类
    13. MaxDepthLinkCrawler.py                                      ===> 避免爬虫陷阱
    14. RequestDownload.py                                          ===> 使用 requests 模块实现爬虫

Chapter02   第2章 数据抓取                                            ===> 展示了如何使用几种库从网页中抽取数据
    01. ScrapingArea.py                                             ===> 使用正则表达式抓取国家面积
    02. BeautifulSoupUse.py                                         ===> Beautiful Soup 模块的使用
    03. Html5libUse.py                                              ===> 使用 html5lib 作为 Beautiful Soup 的解析器
    o4. FindByBeautifulSoup.py                                      ===> 使用 Beautiful Soup 定位元素
    05. ScrapingArea02.py                                           ===> 使用 BeautifulSoup 模块获取国家面积
    06. LxmlUse.py                                                  ===> 使用 lxml 解析不完整 HTML
    07. ScrapingArea03.py                                           ===> 使用 lxml 模块获取国家面积
    08. ScrapingArea04.py                                           ===> 使用 XPath 语法获取国家面积
    09. PerformanceCompare.py                                       ===> 性能对比代码
    10. TestPerformance.py                                          ===> 测试性能代码
    11. CallbackLinkCrawler.py                                      ===> 带回调的 link_crawler
    12. CsvCallback.py                                              ===> Callback 类

Chapter03   第3章 下载缓存                                            ===> 介绍了如何通过缓存结果避免重复下载的问题



Chapter04   第4章 并发下载                                            ===> 教你如何通过并行下载网站加速数据抓取



Chapter05   第5章 动态内容                                            ===> 介绍了如何通过几种方式从动态网站中抽取数据



Chapter06   第6章 表单交互                                            ===> 展示了如何使用输入及导航等表单进行搜索和登录



Chapter07   第7章 验证码处理                                          ===> 阐述了如何访问被验证码图像保护的数据



Chapter08   第8章 Scrapy                                            ===> 介绍了如何使用 Scrapy 进行快速并行的抓取，以及使用 Portia 的 Web 界面构建网络爬虫



Chapter09   第9章 综合应用                                           ===> 对你在本书中学习到的爬虫技术进行总结



