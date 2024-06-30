import instaloader
import pandas as pd
import os

# directory to store scraped images; you can scrape urls but they might expire before you use them to access images for OCR/translation
media_dir = 'downloaded_media'
os.makedirs(media_dir, exist_ok=True)

# initialise the instaloader pkg
L = instaloader.Instaloader(download_pictures=False, download_videos=False, download_video_thumbnails=False)

# enter public profile name
profile_name = 'sz'

profile = instaloader.Profile.from_username(L.context, profile_name)

posts_info = []

# scraping
for post in profile.get_posts():
    # scrape post caption if needed; this is useful to check translation accuracy 
    caption = post.caption if post.caption else ''
    
    media_paths = []
    if post.typename == 'GraphImage':
        media_file = L.download_pic(filename=os.path.join(media_dir, post.shortcode + '.jpg'), url=post.url, mtime=post.date_utc)
        media_paths.append(media_file)
    elif post.typename == 'GraphSidecar':
        for i, sidecar_node in enumerate(post.get_sidecar_nodes()):
            media_file = L.download_pic(filename=os.path.join(media_dir, f"{post.shortcode}_{i}.jpg"), url=sidecar_node.display_url, mtime=post.date_utc)
            media_paths.append(media_file)
    
    posts_info.append({
        'post_id': post.shortcode,
        'caption': caption,
        'media_paths': media_paths
    })

    # limit to 50 posts; change limit if needed but >100 is not recommended 
    if len(posts_info) >= 50:
        break

df = pd.DataFrame(posts_info)

# # uncomment to save df to csv if needed 
# df.to_csv('scraped_posts.csv', index=False)

print("Data has been saved to scraped_posts.csv")
