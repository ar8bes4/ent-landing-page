# 🏥 ENT Landing Page

> 浜松医科大学 耳鼻咽喉科・頭頸部外科 — 入局者向けランディングページ

![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v3-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Cloudflare Pages](https://img.shields.io/badge/Cloudflare_Pages-Hosted-F38020?style=flat-square&logo=cloudflare&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-ar8bes4/ent--landing--page-181717?style=flat-square&logo=github)

## 🚀 概要

Wix 製の既存サイトを完全コードベースで再構築した、学生・若手医師向けのモダンなランディングページです。  
Tailwind CSS (CDN) + Vanilla JS の **単一 HTML ファイル**で完結しており、ビルドツール不要です。

## 📁 構成

```
ent-landing-page/
├── index.html             # メインページ（Tailwind CSS + JS 完全内包）
├── introduction.html      # 教室紹介・教授挨拶ページ
├── student-clerkship.html # 学生病院実習のご案内ページ
├── recruit.html           # 採用情報・専門研修ページ
├── assets/
│   └── images/            # スタッフ写真・OGP 画像などを配置
└── README.md
```

## 🛠 ローカル確認

```bash
# ブラウザで直接開くだけで動作します
start index.html
```

## ☁️ デプロイ (Cloudflare Pages)

1. GitHub にプッシュ
2. Cloudflare Pages ダッシュボードでこのリポジトリを接続
3. ビルドコマンド: なし（静的ファイル）
4. 公開ディレクトリ: `/`（ルート）

## 📷 スタッフ写真の差し替え

`assets/images/` フォルダに写真を配置し、`index.html` 内の `img` タグの `src` を更新してください。

```html
<!-- 差し替え例 -->
<img src="assets/images/staff_morita.jpg" alt="森田 浩太朗" />
```
