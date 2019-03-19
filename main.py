# _*_ coding:utf-8 _*_
from selenium import webdriver
import time
from bs4 import BeautifulSoup

web = webdriver.Chrome(executable_path='source/chromedriver.exe')

def login():
    try:
        url = 'https://passport.csdn.net/account/login'
        web.get(url)
        switch_button = web.find_element_by_css_selector('body > div.main > div > div > div:nth-child(2) > div > h3 > a')
        switch_button.click()

        time.sleep(1)
        name = web.find_element_by_css_selector('#username')
        name.send_keys('461842952@qq.com')

        time.sleep(1)
        pwd = web.find_element_by_css_selector('#password')
        pwd.send_keys('java123456789')

        login = web.find_element_by_css_selector('#fm1 > input.logging')
        login.click()
        # print('login 执行成功')
        return web.page_source
    except Exception as e:
        print(e)
        return login()


def main():
    keywords = input('请输入要查询的关键字:')
    html = login()
    url = 'https://so.csdn.net/so/'
    web.get(url)

    key_input = web.find_element_by_css_selector('#keyword')
    key_input.send_keys(keywords)

    search = web.find_element_by_css_selector('#queryform > div.search-btn-con > input')
    search.click()

    soup = BeautifulSoup(web.page_source, 'html.parser')
    dls = soup.find_all('dl', attrs={'class': 'search-list J_search'})
    page = 1
    while web.find_element_by_css_selector(
            'body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next'):
        n = 1
        if page == 1:
            n = 2
            for i in range(len(dls) - 1):
                try:
                    title = web.find_element_by_css_selector(
                    'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                        n))
                    title.click()
                    web.switch_to_window(web.window_handles[1])
                except Exception as e:
                    print("此处广告，自动跳过...")
                    n+=1
                    try:
                        title = web.find_element_by_css_selector(
                        'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                            n))
                        title.click()
                        web.switch_to_window(web.window_handles[1])
                    except Exception as e:
                        web.close()
                        web.switch_to_window(web.window_handles[0])
                        n += 1
                        title = web.find_element_by_css_selector(
                            'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                                n))
                        title.click()
                        web.switch_to_window(web.window_handles[1])
                        # web.switch_to_window(web.window_handles[error_page_num])


                try:
                    comment_content = web.find_element_by_css_selector('#comment_content')
                    comment_content.send_keys('写的真好')
                    time.sleep(1)

                    try:
                        web.find_element_by_css_selector('#commentform > div > div.right-box > input').click()
                    except Exception as e:
                        # print(e)
                        try:
                            web.switchTo().alert().accept();
                        except Exception as e:
                            continue
                        web.close()
                        web.switch_to_window(web.window_handles[0])
                        n += 1
                        time.sleep(2)

                    try:
                        title = web.find_element_by_css_selector(
                            '#mainBox > main > div.blog-content-box > div.article-title-box > h1').text
                        print(title + '     留言成功')
                    except Exception as e:
                        # print(e)
                        print('留言成功')
                    time.sleep(1)

                    web.close()
                    web.switch_to_window(web.window_handles[0])
                    n += 1
                    time.sleep(2)
                except Exception as e:
                    print('此文博主禁止评论')
                    web.close()
                    web.switch_to_window(web.window_handles[0])
                    n += 1
                    time.sleep(2)
        else:
            for i in range(len(dls) - 1):
                # title = web.find_element_by_css_selector(
                #     'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                #         n))
                # title.click()
                # web.switch_to_window(web.window_handles[1])
                try:
                    title = web.find_element_by_css_selector(
                    'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                        n))
                    title.click()
                    web.switch_to_window(web.window_handles[1])
                except Exception as e:
                    print("此处广告，自动跳过...")
                    n+=1
                    try:
                        title = web.find_element_by_css_selector(
                        'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                            n))
                        title.click()
                        web.switch_to_window(web.window_handles[1])
                    except Exception as e:
                        web.close()
                        web.switch_to_window(web.window_handles[0])
                        n += 1
                        title = web.find_element_by_css_selector(
                            'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                                n))
                        title.click()
                        web.switch_to_window(web.window_handles[1])
                        # web.switch_to_window(web.window_handles[error_page_num])
                try:
                    comment_content = web.find_element_by_css_selector('#comment_content')
                    comment_content.send_keys('写的真好')
                    time.sleep(1)

                    try:
                        web.find_element_by_css_selector('#commentform > div > div.right-box > input').click()
                    except Exception as e:
                        # print(e)
                        try:
                            web.switchTo().alert().accept();
                        except Exception as e:
                            continue
                        try:
                            title = web.find_element_by_css_selector(
                                '#mainBox > main > div.blog-content-box > div.article-title-box > h1').text
                            print(title + '     留言成功')
                        except Exception as e:
                            # print(e)
                            print('留言成功')
                        time.sleep(1)

                        web.close()
                        web.switch_to_window(web.window_handles[0])
                        n += 1
                        time.sleep(2)
                    try:
                        title = web.find_element_by_css_selector(
                            '#mainBox > main > div.blog-content-box > div.article-title-box > h1').text
                        print(title + '     留言成功')
                    except Exception as e:
                        #
                        print('留言成功')
                    time.sleep(1)
                    time.sleep(1)

                    web.close()
                    web.switch_to_window(web.window_handles[0])
                    n += 1
                    time.sleep(2)
                except Exception as e:
                    print('该博主禁止评论')
                    web.close()
                    web.switch_to_window(web.window_handles[0])
                    n += 1
                    time.sleep(2)

        print('第%d页评论完毕' % page)
        time.sleep(5)
        next = web.find_element_by_css_selector(
            'body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next')
        next.click()
        page += 1


def parse(html, keywords):
    # html = search(html, keywords)
    soup = BeautifulSoup(html, 'html.parser')
    dls = soup.find_all('dl', attrs={'class':'search-list J_search'})
    page = 1
    while web.find_element_by_css_selector('body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next'):
        n = 1
        if page == 1:
            n = 2
            for i in range(len(dls)-1):
                # title = web.find_element_by_css_selector('body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child({})'.format(n,page))
                title = web.find_element_by_css_selector('body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(n))
                title.click()
                web.switch_to_window(web.window_handles[1])

                comment_content = web.find_element_by_css_selector('#comment_content')
                # comment_content.click()
                comment_content.send_keys('可以留个微信讨论下吗')
                time.sleep(1)

                web.find_element_by_css_selector('#commentform > div > div.right-box > input').click()
                print(title.text + '留言成功')
                time.sleep(1)

                web.close()
                web.switch_to_window(web.window_handles[0])
                n += 1
                time.sleep(2)
        else:
            for i in range(len(dls) - 1):
                title = web.find_element_by_css_selector(
                    'body > div.main-container > div.con-l > div.search-list-con.csdn-tracking-statistics > dl:nth-child({}) > dt > a:nth-child(1)'.format(
                        n))
                title.click()
                web.switch_to_window(web.window_handles[1])

                comment_content = web.find_element_by_css_selector('#comment_content')
                # comment_content.click()
                comment_content.send_keys('可以留个微信讨论下吗')
                time.sleep(1)

                web.find_element_by_css_selector('#commentform > div > div.right-box > input').click()
                print(title.text + '留言成功')
                time.sleep(1)

                web.close()
                web.switch_to_window(web.window_handles[0])
                n += 1
                time.sleep(2)

        print('第%d页评论完毕' % page)
        time.sleep(10)
        next = web.find_element_by_css_selector('body > div.main-container > div.con-l > div.csdn-pagination.hide-set > span.page-nav > a.btn.btn-xs.btn-default.btn-next')
        next.click()
        page += 1


if __name__ == '__main__':
    main()
    # keywords = input('请输入要查询的关键字:')
    # html = login()
    # search(keywords, html)