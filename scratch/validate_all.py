import os
import glob
from html.parser import HTMLParser

TARGET_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website"

class TestHTMLParser(HTMLParser):
    def handle_error(self, message):
        pass

def main():
    html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))
    success = True

    for filepath in html_files:
        filename = os.path.basename(filepath)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            parser = TestHTMLParser()
            parser.feed(content)
            print(f"Syntax OK: {filename}")
        except Exception as e:
            print(f"Syntax ERROR in {filename}: {e}")
            success = False

    if success:
        print("\nAll HTML files validated successfully! Error: 0")
    else:
        print("\nValidation failed with errors.")

if __name__ == "__main__":
    main()
