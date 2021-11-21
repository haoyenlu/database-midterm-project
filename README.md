# 全台遊憩水域資訊系統
使用者輸入縣市、鄉鎮市區後，可以得知該地的水域、海灘相關資訊。

> 此文件參考助教所提供之1101_NTUIM_DBM_web_tutorial/readme.md

### Contributors & Tasks
- 林奕帆 Database schema design, data collection and process using postgreSQL
- 王佑豪 Database schema design, data collection and process using postgreSQL
- 呂皓恩 Back-end using Django, connect backend and frontend
- 陳德安 Frontend using ReactJS
- 劉為德 Report, video

## Database
- 使用 PostgreSQL 13 及 pgAdmin 4
- db資料夾中的 SURF_empty.sql 和 SURF.sql 分別是僅有table，沒有資料的空檔案及已預先填入資料的檔案
- data_crawl.ipynb 是負責爬取資料和將資料導入PostgreSQL的程式
- 建立Database
     * 方案一 : 直接將現有資料庫 SURF.sql 匯入 PostgreSQL，方法可以參考[這裡](https://www.youtube.com/watch?v=C30q5i1e9KE)
     * 方案二 : 執行 data_crawl.ipynb ，注意事項如下:
         + 程式使用到 Selenium 控制 Chrome 瀏覽器，所以請確保電腦上有安裝 [Chrome](https://support.google.com/chrome/answer/95346?hl=zh-Hant&co=GENIE.Platform%3DDesktop)
         + 程式使用到 Google Map API 中，所以需要一組 API KEY ([申請教學可以參考這裡](https://www.ibest.com.tw/news-detail/google-map-api/))，請確認有啟用 Places API 及 Geocoding API
           或者可以直接使用我們附在書面報告中的KEY
         + 請確認db資料夾中的 spots.csv 和程式是在同一個目錄下
         + 程式的執行時間大約是 10 ~ 15分鐘，請耐心等待


### API
- **討論文件**：https://hackmd.io/_vPVxhaGRT6TIeWEMzvgWA
- **API endpoint**: http://127.0.0.1:8000/api
- **四個接口**
    >GET /town_list
    
    >POST /town_list
    
    >POST /beach_search

    >POST /beach_information

## Backend

確定電腦有安裝 `python3` 以及完成上述資料匯入資料庫的指令後打開終端機執行以下指令：

```shell
# for mac
cd backend
python3 -m venv tutorial-env #建立虛擬環境 #-m: module-name
source tutorial-env/bin/activate #啟動虛擬環境 for mac
```

```shell
# for windows
cd backend
python3 -m venv tutorial-env #建立虛擬環境 #-m: module-name
tutorial-env\Scripts\activate.bat #啟動虛擬環境 for windows
```

成功的話，command prompt 前面應該會多出 `(tutorial-env)` 的字樣，代表已經進入這個虛擬環境。如果未來你想退出這個虛擬環境，可以輸入 `deactivate`。
接著下載所需套件，需要的套件與版本已定義在 `requirements.txt`，下載完輸入`pip list`檢查所有用 `pip` 下載的套件。

```shell
python -m pip install --upgrade pip #pip更新至最新版本
pip install -r requirements.txt
pip list
```
```
Package             Version
------------------- -------
asgiref             3.4.1
dj-database-url     0.5.0
Django              3.2.6
django-cors-headers 3.10.0
djangorestframework 3.12.4
pip                 21.3
psycopg2            2.9.1
psycogp2-binary     2.9.2
python-decouple     3.4
pytz                2021.1
setuptools          47.1.0
sqlparse            0.4.1
```

安裝完套件後複製 `.env.example` 的內容到 `.env`。

>`.env`裡存的是環境變數，裡面通常會放一些機密資訊（如 `SECRET_KEY`、資料庫資訊等），這種檔案通常不會傳上版本控制系統（如 Github），但此為教學專案為了方便講解上傳，同學們實作專案時記得避免。

```shell
# for mac
cp .env.example .env
```

```shell
# for windows
copy .env.example .env
```

接著可以將 `.env` 當中的變數改成符合你電腦資料庫的值。

```shell
SECRET_KEY={aaaaaaaaa}
DEBUG=True
ALLOWED_HOSTS=.localhost,127.0.0.1
DATABASE_URL={postgres://USER:PASSWORD@HOST:PORT/NAME}
```

最後，同步資料庫並啟動 backend server。

```shell
python manage.py migrate
python manage.py runserver
```

用瀏覽器打開  http://127.0.0.1:8000/api/town_list ，如果有順利拿到資源表示後端起成功。
![image](https://user-images.githubusercontent.com/74141558/142758897-f352d316-ddbe-4d72-901b-8c479cf19158.png)

## Frontend

#### Step 0. 安裝 yarn
如果你還沒有安裝 yarn，請參考官網 https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable ，依照步驟安裝。

#### Step 1. 安裝 packages
第一次開啟專案請先用以下指令安裝所有需要的 packages，之後再次開啟專案跳過這個指令即可。
```shell
cd frontend
yarn
```

#### Step 2. 開啟前端
```shell
cd frontend
yarn start
```
#### Step 3. 開啟瀏覽器 
一般情況會自動開啟瀏覽器，若沒有請手動開啟 http://127.0.0.1:3000/ ，看到以下畫面即代表成功開啟前端且前後端連接成功。

#### Step 4. 下載react-router-dom
如果遇到react-router-dom的相關error，請依照所使用的作業系統下載react-router-dom。

```shell
# for mac
yarn add react-router-dom
```
### Reference for frontend
- **Navbar and side menu**：https://www.youtube.com/watch?v=I2UBjN5ER4s&t=4863s



