import os
import glob
import re

TARGET_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website"

# フッターボトムバーのサブリンク削除用正規表現
BOTTOM_BAR_PATTERN = re.compile(
    r"[ \t]*<div class=\"flex flex-wrap justify-center sm:justify-start gap-x-6 gap-y-2\">\s*<a href=\"index\.html\" class=\"hover:text-brand-blue transition-colors\">ホーム</a>.*?</div>",
    re.DOTALL
)

# 置換後のボトムバーHTML（インデントも含めて挿入）
BOTTOM_BAR_REPLACEMENT = """                <div class="flex flex-wrap justify-center sm:justify-start gap-x-6 gap-y-2">
                    <a href="index.html" class="hover:text-brand-blue transition-colors">ホーム</a>
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
        
        # ボトムバーサブリンクの削除
        new_content, count = BOTTOM_BAR_PATTERN.subn(BOTTOM_BAR_REPLACEMENT, new_content)
        if count > 0:
            print(f"  - Removed bottom bar sublinks ({count} occurrence)")
        else:
            print("  - [WARNING] Bottom bar links not found or already modified")
            
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
