# APT-attack-defense
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
