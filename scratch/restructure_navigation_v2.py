import os
import glob

# HTMLファイルが格納されているディレクトリ
TARGET_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website"

# PCナビゲーションの置換ターゲットと置換後
PC_TARGET = """                    <a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>
                    
                    <!-- Content Dropdown -->
                    <div class="relative group">
                        <button class="flex items-center gap-1 hover:text-brand-blue transition-colors py-2 focus:outline-none">
                            <span>コンテンツ</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <!-- Dropdown Menu -->
                        <div class="absolute left-0 mt-0 w-64 bg-white border border-brand-line rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 py-2 z-50">
                            <a href="pdf-library.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">PDF資料室</a>
                            <a href="blog.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">ブログ・活動報告</a>
                            <a href="gakkai-taikenki.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">学会体験記</a>"""

PC_REPLACEMENT = """                    <a href="recruit.html" class="hover:text-brand-blue transition-colors">採用情報</a>
                    <a href="blog.html" class="hover:text-brand-blue transition-colors">ブログ・活動報告</a>
                    
                    <!-- Content Dropdown -->
                    <div class="relative group">
                        <button class="flex items-center gap-1 hover:text-brand-blue transition-colors py-2 focus:outline-none">
                            <span>コンテンツ</span>
                            <svg class="w-4 h-4 transition-transform group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <!-- Dropdown Menu -->
                        <div class="absolute left-0 mt-0 w-64 bg-white border border-brand-line rounded-xl shadow-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 py-2 z-50">
                            <a href="pdf-library.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">PDF資料室</a>
                            <a href="gakkai-taikenki.html" class="block px-4 py-2 text-xs font-bold text-brand-navy hover:bg-brand-paper hover:text-brand-blue transition-colors">学会体験記</a>"""


# モバイルナビゲーションの置換ターゲットと置換後
MOBILE_TARGET = """                <a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>
                
                <!-- Mobile Content Accordion -->
                <div class="space-y-1">
                    <button class="flex items-center justify-between w-full py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors focus:outline-none" onclick="toggleMobileSubmenu('mobile-submenu-content', this)">
                        <span>コンテンツ</span>
                        <svg class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                        </svg>
                    </button>
                    <div id="mobile-submenu-content" class="hidden pl-4 pr-2 py-1 space-y-2 bg-brand-paper/50 rounded-lg">
                        <a href="pdf-library.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">PDF資料室</a>
                        <a href="blog.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">ブログ・活動報告</a>
                        <a href="gakkai-taikenki.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">学会体験記</a>"""

MOBILE_REPLACEMENT = """                <a href="recruit.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">採用情報</a>
                <a href="blog.html" class="block py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors">ブログ・活動報告</a>
                
                <!-- Mobile Content Accordion -->
                <div class="space-y-1">
                    <button class="flex items-center justify-between w-full py-2 border-b border-brand-line/40 hover:text-brand-blue transition-colors focus:outline-none" onclick="toggleMobileSubmenu('mobile-submenu-content', this)">
                        <span>コンテンツ</span>
                        <svg class="w-4 h-4 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                        </svg>
                    </button>
                    <div id="mobile-submenu-content" class="hidden pl-4 pr-2 py-1 space-y-2 bg-brand-paper/50 rounded-lg">
                        <a href="pdf-library.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">PDF資料室</a>
                        <a href="gakkai-taikenki.html" class="block py-1.5 text-xs text-brand-navy hover:text-brand-blue transition-colors">学会体験記</a>"""


def main():
    html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))
    # サブディレクトリ内のHTML (blog/など) もあるか確認
    html_files += glob.glob(os.path.join(TARGET_DIR, "blog", "*.html"))

    for filepath in html_files:
        filename = os.path.basename(filepath)
        print(f"Processing {filename}...")

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Windowsの改行コード対策
        normalized_content = content.replace("\r\n", "\n")
        
        # 置換実行
        new_content = normalized_content
        
        if PC_TARGET in new_content:
            new_content = new_content.replace(PC_TARGET, PC_REPLACEMENT)
            print("  - Replaced PC Nav Link")
        else:
            # 部分一致やインデントの違いがあるかもしれないため警告
            print("  - WARNING: PC Target not found exactly as expected")

        if MOBILE_TARGET in new_content:
            new_content = new_content.replace(MOBILE_TARGET, MOBILE_REPLACEMENT)
            print("  - Replaced Mobile Nav Link")
        else:
            print("  - WARNING: Mobile Target not found exactly as expected")

        # 内容が変わった場合のみ書き戻す
        if new_content != normalized_content:
            # 改行コードを書き戻す（オリジナルを尊重するため、ファイルごとの改行コードに合わせる）
            if "\r\n" in content:
                final_content = new_content.replace("\n", "\r\n")
            else:
                final_content = new_content
                
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_content)
            print("  - File updated successfully!")
        else:
            print("  - No changes made.")

if __name__ == "__main__":
    main()
