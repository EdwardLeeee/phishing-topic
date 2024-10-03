# 專題使用手冊
## latex

### 安裝latex
```
sudo apt-get update
sudo apt-get install texlive-full
```
### 標楷體設定
```
sudo cp kaiu.ttf /usr/share/fonts/truetype/
sudo fc-cache -fv
```
### 建立latex 檔
```
vim example.tex
```
### 把latex 轉 pdf
```
xelatex example.tex
```
### open pdf
```
evince file_name.pdf
```
## Neo4j
[說明網站](https://www.virtono.com/community/tutorial-how-to/how-to-install-neo4j-on-ubuntu-22-04/)
### 安裝
```
sudo apt-get install apt-transport-https
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable latest' | sudo tee /etc/apt/sources.list.d/neo4j.list
sudo apt-get update
sudo apt-get install neo4j
```
### 使用
狀態
```
sudo systemctl status neo4j
```
啟用
```
sudo systemctl start neo4j
```
打開圖形化界面
> 在瀏覽器輸入
```
localhost:7474
```

## auditd
### 安裝與啟動
```
sudo apt-get install auditd
sudo systemctl start auditd
```
### 追蹤檔案

> 這條命令的具體參數解釋：
> 
> `-w /path/to/file1.c`：監控 /path/to/file.c 文件的路徑。
> 
> `-p war`：監控寫入 (w)、屬性修改 (a)、讀取 (r) 行為。
> 
> `-k file1_c_edit`：設置一個標識 (key)，以便日後方便檢索日誌。
>
```
sudo auditctl -w /path/to/file1.c -p war -k file1_c_edit
```

### 查看 audit log
> 這條命令會返回所有與 file1_c_edit 標識相關的事件
>
`sudo ausearch -k file1_c_edit`

### 停止追蹤檔案
```
sudo auditctl -W /path/to/file1.c -k file1_c_edit
```

## 路由器設定
### 要把欲使用防火牆打開
> 80 是 HTTP 的 port 
> 443 是 HTTPS 的 port 

```
sudo ufw allow 80
sudo ufw allow 443
```
### 把 router 的 port 打開
1.登入設定畫面
```
192.168.0.1
```
2.輸入帳號 `admin`（密碼留白）
3.選擇進階->虛擬伺服器

## nginx
### 開機自動啟動
```
sudo systemctl enable nginx
```
### 開啟
```
sudo systemctl start nginx
```
### 設定
#### 申請 SSL certificate
```
sudo apt update
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx
```
#### 製作設定檔
```
vim xxx.conf 
```
```nginx
# HTTP server配置，用於將所有HTTP請求重定向到HTTPS
server {
    listen 80;
    server_name need-a-dentist.publicvm.com;

    # 將所有HTTP請求重定向到HTTPS
    return 301 https://$host$request_uri;
}

# HTTPS server配置，代理到Flask應用
server {
    listen 443 ssl; # 暫時註釋掉SSL憑證配置，直到憑證生成完成
    server_name need-a-dentist.publicvm.com;

    # 暫時註釋掉SSL憑證配置，直到憑證生成完成
    ssl_certificate /etc/letsencrypt/live/need-a-dentist.publicvm.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/need-a-dentist.publicvm.com/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
#### 把設定檔掛到「可用的」站點配置文件
```
sudo cp xxx.conf /etc/nginx/sites-available/xxx.conf
```
#### 把設定檔掛到「以啟用的」站點配置文件 
```
sudo ln -s /etc/nginx/sites-available/xxx.conf /etc/nginx/sites-enabled/
```
