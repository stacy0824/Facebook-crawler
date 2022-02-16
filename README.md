# Facebook-crawler
此程式碼用於爬取FACEBOOK社團貼文及貼文留言

程式執行後，將會進行爬取，並將貼文及留言存成CSV檔在該目錄底下


## 先決條件
此爬蟲程式使用selenium透過ChromeDriver進行爬取，搭配 BeautifulSoup 解析 HTML 網頁原始碼

故需先安裝相關使用套件及WebDriver

### 下載ChromeDriver
1. 到Chrome設定>>關於Chrome，查看版本號碼

<img src="https://user-images.githubusercontent.com/91735053/154321337-0a121d5d-fdfc-42a6-a140-3f74a220815e.png" width="60%" height="60%" alt=""/><br/>

2. 從[selenium](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)官方網站下載正確版本的ChromeDriver

<img src="https://user-images.githubusercontent.com/91735053/154322621-43582c8a-6ace-47ce-a936-ea1cb84b2f1b.png" width="60%" height="60%" alt=""/><br/>

3. 若未有相同的版本號，可下載版本開頭的數字相同的即可

<img src="https://user-images.githubusercontent.com/91735053/154322783-c5d6a82f-fe4a-43c6-9d94-db46d3ea2968.png" width="60%" height="60%" alt=""/><br/>

4. 選擇作業系統

<img src="https://user-images.githubusercontent.com/91735053/154325388-9ce0ee56-23ac-4059-a60e-c519f5cf9a04.png" width="60%" height="60%" alt=""/><br/>

5. 下載完後解壓縮，將chromedriver.exe移到與程式相同的目錄下



***


### 安裝相關套件

此程式碼使用了一下套件，若環境中未有下列套件，需先安裝

**1. webdriver_manager**

   此套件會自動根據你的Chrome下載的版本開啟chromedriver
   
   ```python
   pip install webdriver-manager
   ```
   
**2. selenium**

   程式使用selenium進行爬蟲，故需安裝此套件

   ```python
   pip install selenium
   ```
   
**3. pandas**
   
   將抓取的貼文及留言使用pandas以Dataframe儲存成csv檔，故需安裝此套件
   
   ```python
   pip install pandas
   ```
