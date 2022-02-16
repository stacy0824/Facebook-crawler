import random
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.facebook.com/groups/1260448967306807"
# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(URL)
time.sleep(10)

switch = True
# 計算全部迴圈(貼文)的次數
allPostCounts = 0

for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("Scroll")
    time.sleep(5)

# 載入文章內容及顯示更多
while switch:

    # POST及MESSAGE寫入dataframe，建立dataframe
    dataRow = 0
    df = pd.DataFrame(columns=["POST", "MESSAGE"])

    # 計算當次迴圈(貼文)次數
    postCounts = 0

    # 展開貼文
    openPostsAndMessages = driver.find_elements(
        By.CLASS_NAME, "du4w35lb.k4urcfbm.l9j0dhe7.sjgh65i0"
    )
    for openPostAndMessage in openPostsAndMessages:
        postCounts += 1
        if allPostCounts > postCounts:
            pass

        else:
            allPostCounts += 1
            print(allPostCounts)
            try:
                openSeeMores = openPostAndMessage.find_element(
                    By.CLASS_NAME, "ecm0bbzt.hv4rvrfc.ihqw7lf3.dati1w0a"
                )

            except Exception:
                print("no Post")

            else:
                try:
                    seeMore = openSeeMores.find_element(
                        By.CLASS_NAME,
                        "oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz."
                        "rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8."
                        "oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso."
                        "i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id."
                        "lrazzd5p",
                    )

                except Exception:
                    print("no more Post")

                else:
                    driver.execute_script("arguments[0].click()", seeMore)
                    time.sleep(random.randint(1, 2))

                # 展開留言及留言回覆
                x = 1
                clickCount = 0
                while x == 1:
                    clickCount += 1
                    if (clickCount / 20) == 1:
                        time.sleep(20)

                    try:
                        moreMessage = openPostAndMessage.find_element(
                            By.CLASS_NAME,
                            "oajrlxb2.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2."
                            "goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l."
                            "agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.p7hjln8o."
                            "kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz."
                            "jb3vyjys.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr."
                            "f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql."
                            "pq6dq46d.btwxx1t3.abiwlrkh.lzcic4wl.bp9cbjyn.m9osqain."
                            "buofh1pr.g5gj957u.p8fzw8mz.gpro0wi8",
                        )

                        # 同個classc同時是展開留言及隱藏留言的按鈕，故利用文字來區分展開及隱藏
                        hideMessage = 0
                        if str("隱藏") in moreMessage.text:
                            hideMessage += 1
                            moreMessage = openPostsAndMessages.find_elements(
                                By.CLASS_NAME,
                                "oajrlxb2.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2."
                                "goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l."
                                "agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.p7hjln8o."
                                "kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz."
                                "jb3vyjys.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr."
                                "f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql."
                                "pq6dq46d.btwxx1t3.abiwlrkh.lzcic4wl.bp9cbjyn.m9osqain."
                                "buofh1pr.g5gj957u.p8fzw8mz.gpro0wi8",
                            )[int(hideMessage)]

                    except Exception:
                        print("no more message")
                        x = 0

                    else:
                        driver.execute_script("arguments[0].click()", moreMessage)
                        time.sleep(random.randint(5, 8))

                        # 展開留言內的顯示更多
                        try:
                            ReplyMores = openPostAndMessage.find_element(
                                By.TAG_NAME, "ul"
                            )
                            ReplyMore = ReplyMores.find_element(
                                By.CLASS_NAME,
                                "oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz."
                                "rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8."
                                "oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso."
                                "i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gpro0wi8.oo9gr5id."
                                "lrazzd5p",
                            )

                        except Exception:
                            print("no more Reply")

                        else:
                            print("clicked")
                            driver.execute_script("arguments[0].click()", ReplyMore)
                            time.sleep(random.randint(2, 4))

            if (allPostCounts / (13 or 35)) == 1:
                time.sleep(random.randint(60, 120))

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 定位貼文及留言
    PostsAndMessagesSoup = soup.find_all(
        "div", class_="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"
    )

    for PostAndMessage in PostsAndMessagesSoup:

        # 貼文
        Posts = PostAndMessage.find_all(
            "div", class_="ecm0bbzt hv4rvrfc ihqw7lf3 dati1w0a"
        )
        for Post in Posts:
            Postdata = Post.text

            # 留言
            Messages = PostAndMessage.find_all("div", class_="cwj9ozl2 tvmbv18p")
            for Message in Messages:
                messages = Message.find_all(
                    "div", class_="kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"
                )
                for message in messages:
                    MessageData = message.text

                    # 寫入每行dataframe
                    df.loc[dataRow] = [Postdata, MessageData]
                    dataRow += 1

    df.to_csv(r"./fabebookcrawler.csv", encoding="utf-8")
    print("----------save rawdata----------")

    for x in range(2):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print("Scroll")
        time.sleep(random.randint(5, 20))

    # 檢視未登入窗格，若出現unloginError時停止
    try:
        unloginError = driver.find_element(
            By.CLASS_NAME,
            "gs1a9yip.rq0escxv.j83agx80.cbu4d94t.taijpn5t.kb5gq1qc.h3gjbzrl",
        )

    except Exception:
        switch = True

    else:
        switch = False

    try:
        finallyMoreMessage = driver.find_element(
            By.CLASS_NAME,
            "oajrlxb2.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje."
            "s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9."
            "mg4g778l.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz."
            "jb3vyjys.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb."
            "n00je7tq.arfg74bv.qs9ysxi8.k77z8yql.pq6dq46d.btwxx1t3.abiwlrkh.lzcic4wl."
            "bp9cbjyn.m9osqain.buofh1pr.g5gj957u.p8fzw8mz.gpro0wi8",
        )

        if str("隱藏") in finallyMoreMessage.text:
            hideMessage += 1
            moreMessage = openPostsAndMessages.find_elements(
                By.CLASS_NAME,
                "oajrlxb2.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2."
                "goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l."
                "agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.mg4g778l.p7hjln8o."
                "kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz."
                "jb3vyjys.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr."
                "f1sip0of.du4w35lb.n00je7tq.arfg74bv.qs9ysxi8.k77z8yql."
                "pq6dq46d.btwxx1t3.abiwlrkh.lzcic4wl.bp9cbjyn.m9osqain."
                "buofh1pr.g5gj957u.p8fzw8mz.gpro0wi8",
            )[int(hideMessage)]

    except Exception:
        switch = False

time.sleep(10)
driver.quit()
