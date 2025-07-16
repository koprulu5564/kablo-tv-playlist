import requests
from datetime import datetime
import os

def fetch_and_update_playlist():
    SOURCE_URL = "https://mth.tc/kaaablotv"
    OUTPUT_FILE = "playlist.m3u"
    
    try:
        response = requests.get(SOURCE_URL, timeout=10)
        response.raise_for_status()
        
        updated_content = f"""#EXTM3U
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Source: {SOURCE_URL}
# Update Interval: 6 hours

{response.text}"""
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"Playlist başarıyla güncellendi: {OUTPUT_FILE}")
        return True
        
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return False

if __name__ == "__main__":
    fetch_and_update_playlist()
