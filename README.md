# 華語學堂 Mandarin School — 網站

中文學校展示網站（靜態多頁），參考 BumbleBerry English 佈局與風格。

## 頁面
- `index.html` — 主頁（Hero、課程亮點、老師預覽、直接聯絡）
- `about.html` — 關於我們
- `courses.html` — 課程列表
- `teachers.html` — 老師介紹
- `contact.html` — 聯絡我們（WhatsApp / 電郵 / 表單）

## 聯絡資訊（已置於頂部聯絡條與各頁）
- WhatsApp：`phil.deng`
- Email：`phoenixdkd@gmail.com`

## 技術
- 純靜態 HTML / CSS / JS，無建置步驟
- 響應式：桌面、平板、手機皆友好（mobile-first）
- 自寫 CSS（無框架），手機選單由 `assets/js/main.js` 控制

## 本地預覽
```bash
cd chinese-school
python3 -m http.server 8080
# 開瀏覽器 http://localhost:8080
```

## 部署（GitHub Pages）
推送至 `main` 分支後，於倉庫 Settings → Pages 選 `main` / root 即可上線。

## 目錄
```
chinese-school/
├─ index.html about.html courses.html teachers.html contact.html
├─ assets/
│  ├─ css/style.css
│  ├─ js/main.js
│  └─ img/
```
