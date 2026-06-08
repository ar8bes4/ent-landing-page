import os
import glob
import re

TARGET_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website"

# 1. PC外部サイトドロップダウンの削除用正規表現
# <!-- External Site Dropdown -->
PC_EXTERNAL_PATTERN = re.compile(
    r"[ \t]*<!-- External Site Dropdown -->\s*<div class=\"relative group\">.*?<!-- Dropdown Menu -->\s*<div[^>]*>.*?</div>\s*</div>\n?",
    re.DOTALL
)

# 2. モバイル外部サイトアコーディオンの削除用正規表現
# <!-- Mobile External Links Accordion -->
MOBILE_EXTERNAL_PATTERN = re.compile(
    r"[ \t]*<!-- Mobile External Links Accordion -->\s*<div class=\"space-y-1\">.*?<div id=\"mobile-submenu-external\"[^>]*>.*?</div>\s*</div>\n?",
    re.DOTALL
)

# 3. フッターグリッドコンテナ md:grid-cols-4 -> md:grid-cols-5 の置換
GRID_PATTERN = re.compile(
    r"(<!-- Footer -->\s*<footer[^>]*>\s*<div[^>]*>\s*<div class=\"grid grid-cols-1 )md:grid-cols-4( gap-8)",
    re.DOTALL
)

# 4. フッターの活動報告と外部サイトの分割用正規表現
FOOTER_PATTERN = re.compile(
    r"[ \t]*<!-- Col 4: Activity & External Links -->\s*<div class=\"space-y-3\">.*?<h4[^>]*>活動報告 &amp; 外部サイト</h4>.*?</div>\s*</div>",
    re.DOTALL
)

# 分割後のフッターHTML（インデントも含めて挿入）
FOOTER_REPLACEMENT = """                <!-- Col 4: Activity -->
                <div class="space-y-3">
                    <h4 class="text-xs font-black text-brand-teal uppercase tracking-wider">活動報告</h4>
                    <div class="flex flex-col gap-2 text-xs font-bold text-brand-muted">
                        <a href="blog.html" class="hover:text-brand-blue transition-colors">ブログ</a>
                        <a href="pdf-library.html" class="hover:text-brand-blue transition-colors">PDF資料室</a>
                        <a href="gakkai-taikenki.html" class="hover:text-brand-blue transition-colors">学会体験記</a>
                    </div>
                </div>
                <!-- Col 5: External Links -->
                <div class="space-y-3">
                    <h4 class="text-xs font-black text-brand-teal uppercase tracking-wider">外部サイト</h4>
                    <div class="flex flex-col gap-2 text-xs font-bold text-brand-muted">
                        <a href="http://www.hama-med.ac.jp/index.html" target="_blank" rel="noopener noreferrer" class="hover:text-brand-blue flex items-center gap-1 transition-colors">
                            <span>浜松医科大学HP</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                        <a href="http://www.shizuoka-jibika.jp/" target="_blank" rel="noopener noreferrer" class="hover:text-brand-blue flex items-center gap-1 transition-colors">
                            <span>静岡県地方部会</span>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                        <a href="https://www.hmsol.co.jp/products/index/6" target="_blank" rel="noopener noreferrer" class="hover:text-brand-teal flex items-center gap-1 transition-colors font-extrabold">
                            <span>H型耳垢鉗子 (浜松医大式)</span>
                            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                        </a>
                    </div>
                </div>"""

def main():
    html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        print(f"=== Processing {filename} ===")
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # 改行コードの正規化
        normalized_content = content.replace("\r\n", "\n")
        new_content = normalized_content
        
        # 1. PC外部サイトドロップダウンの削除
        new_content, pc_count = PC_EXTERNAL_PATTERN.subn("", new_content)
        if pc_count > 0:
            print(f"  - Removed PC External Site Dropdown ({pc_count} occurrence)")
        else:
            print("  - [WARNING] PC External Site Dropdown not found")
            
        # 2. モバイル外部サイトアコーディオンの削除
        new_content, mobile_count = MOBILE_EXTERNAL_PATTERN.subn("", new_content)
        if mobile_count > 0:
            print(f"  - Removed Mobile External Links Accordion ({mobile_count} occurrence)")
        else:
            print("  - [WARNING] Mobile External Links Accordion not found")
            
        # 3. フッターグリッドを md:grid-cols-5 に変更
        new_content, grid_count = GRID_PATTERN.subn(r"\g<1>md:grid-cols-5\g<2>", new_content)
        if grid_count > 0:
            print(f"  - Updated Footer Grid to md:grid-cols-5 ({grid_count} occurrence)")
        else:
            print("  - [WARNING] Footer Grid container not found or already modified")
            
        # 4. フッターカラム4の分割
        new_content, footer_count = FOOTER_PATTERN.subn(FOOTER_REPLACEMENT, new_content)
        if footer_count > 0:
            print(f"  - Split Footer Column 4 into Activity and External Links ({footer_count} occurrence)")
        else:
            print("  - [WARNING] Footer Column 4 not found or already modified")
            
        # 5. 残った「ブログ・活動報告」を「ブログ」に置換
        blog_count = new_content.count("ブログ・活動報告")
        if blog_count > 0:
            new_content = new_content.replace("ブログ・活動報告", "ブログ")
            print(f"  - Replaced 'ブログ・活動報告' with 'ブログ' ({blog_count} occurrences)")
        else:
            print("  - 'ブログ・活動報告' not found in file")
            
        # 変更の保存
        if new_content != normalized_content:
            # 改行コードの復元
            if "\r\n" in content:
                final_content = new_content.replace("\n", "\r\n")
            else:
                final_content = new_content
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_content)
            print("  - Saved changes successfully!")
        else:
            print("  - No changes made.")

if __name__ == "__main__":
    main()
