import os
import shutil
import urllib.request

# 設定
IMAGE_DIR = r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website\images"
ATTACHED_PHOTO = r"C:\Users\yert1\.gemini\antigravity\brain\2df59089-7ec8-4381-a527-a208a0413eab\media__1780927272382.png"

# ダウンロード対象
assets = {
    "images/flyer_2026.png": "https://static.wixstatic.com/media/2db1a0_0adaae958b04467d85d699656fc0216a~mv2.png/v1/fill/w_1025,h_1491,al_c,q_90,enc_avif,quality_auto/2026_11.png",
    "images/recruit_graph.png": "https://static.wixstatic.com/media/2db1a0_c5d6d309ab944cb19c0f19cf23fe4fc3~mv2.png/v1/crop/x_0,y_10,w_948,h_546/fill/w_947,h_546,al_c,q_90,enc_avif,quality_auto/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-14%20145022.png",
    "images/ear_forceps.png": "https://static.wixstatic.com/media/2db1a0_adb61dbe6fea4453bf1a140c1cb6e41d~mv2.png/v1/fill/w_979,h_459,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-02-15%20114656.png"
}

def main():
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
        print(f"Created directory: {IMAGE_DIR}")

    # 1. Wix画像のダウンロード
    for rel_path, url in assets.items():
        dest = os.path.join(r"c:\Users\yert1\Documents\agy\50_SNS-WebSite\new-ent-website", rel_path.replace("/", "\\"))
        print(f"Downloading {url} to {dest}...")
        try:
            # User-Agentを指定してダウンロードエラーを防ぐ
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req) as response, open(dest, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
            print("Success!")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

    # 2. 添付集合写真のコピー
    dest_photo = os.path.join(IMAGE_DIR, "group_photo_2026.png")
    print(f"Copying {ATTACHED_PHOTO} to {dest_photo}...")
    try:
        shutil.copy(ATTACHED_PHOTO, dest_photo)
        print("Success!")
    except Exception as e:
        print(f"Error copying photo: {e}")

if __name__ == "__main__":
    main()
