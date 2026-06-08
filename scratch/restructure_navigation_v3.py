import os
import glob
import re

TARGET_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website"

# 1. PCヘッダー内のドロップダウンからブログを削除するための正規表現
# <a href="blog.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">ブログ・活動報告</a>
# 前後の改行やインデントも含めて消せるようにマッチさせる
PC_DROP_PATTERN = r'[ \t]*<a href="blog\.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">ブログ・活動報告</a>\n?'

# 2. PCの「採用情報」の直後に「ブログ・活動報告」を追加
# 置換前: <a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>
# 置換後: <a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>\n                    <a href="blog.html" class="hover:text-brand-blue transition-colors">ブログ・活動報告</a>
PC_ADD_TARGET = '<a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>'
PC_ADD_REPLACEMENT = '<a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>\n                    <a href="blog.html" class="hover:text-brand-blue transition-colors">ブログ・活動報告</a>'

# 3. モバイルメニュー内のドロップダウンからブログを削除
# <a href="blog.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">ブログ・活動報告</a>
MOBILE_DROP_PATTERN = r'[ \t]*<a href="blog\.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">ブログ・活動報告</a>\n?'

# 4. モバイルメニューの「採用情報」の直後に「ブログ・活動報告」を追加
# 置換前: <a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>
# 置換後: <a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>\n                <a href="blog.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">ブログ・活動報告</a>
MOBILE_ADD_TARGET = '<a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>'
MOBILE_ADD_REPLACEMENT = '<a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>\n                <a href="blog.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">ブログ・活動報告</a>'

def main():
    # ルートディレクトリのHTMLファイルのみを対象にする (blog/配下は除外)
    html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))

    for filepath in html_files:
        filename = os.path.basename(filepath)
        print(f"Processing {filename}...")

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 改行コードを一旦 \n に統一して処理
        normalized_content = content.replace("\r\n", "\n")
        new_content = normalized_content

        # 既に昇格済み（第一階層に blog.html があって、かつドロップダウンから消えている）ならスキップする
        # （同じファイルを複数回実行した際の二重適用を防ぐ）
        is_already_promoted = (
            f'href="blog.html"' in new_content and 
            PC_ADD_REPLACEMENT in new_content
        )
        if is_already_promoted:
            print("  - Already promoted. Skipping.")
            continue

        # 1. PCドロップダウンからブログ行を削除
        new_content, count1 = re.subn(PC_DROP_PATTERN, "", new_content)
        if count1 > 0:
            print(f"  - Removed from PC drop-down ({count1} occurrence)")
        else:
            print("  - WARNING: PC Drop-down link not found")

        # 2. PC第一階層にブログリンクを追加
        if PC_ADD_TARGET in new_content:
            new_content = new_content.replace(PC_ADD_TARGET, PC_ADD_REPLACEMENT)
            print("  - Added to PC navigation")
        else:
            print("  - WARNING: PC Add Target not found")

        # 3. モバイルドロップダウンからブログ行を削除
        new_content, count2 = re.subn(MOBILE_DROP_PATTERN, "", new_content)
        if count2 > 0:
            print(f"  - Removed from Mobile drop-down ({count2} occurrence)")
        else:
            print("  - WARNING: Mobile Drop-down link not found")

        # 4. モバイル第一階層にブログリンクを追加
        if MOBILE_ADD_TARGET in new_content:
            new_content = new_content.replace(MOBILE_ADD_TARGET, MOBILE_REPLACEMENT)
            print("  - Added to Mobile navigation")
        else:
            print("  - WARNING: Mobile Add Target not found")

        # 変更があった場合のみ保存
        if new_content != normalized_content:
            # 元のファイルの改行コードに合わせて戻す
            if "\r\n" in content:
                final_content = new_content.replace("\n", "\r\n")
            else:
                final_content = new_content

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_content)
            print("  - Updated file successfully!")
        else:
            print("  - No changes made.")

if __name__ == "__main__":
    main()
