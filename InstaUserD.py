import instaloader
import csv
import sys


def banner():
   print("""
    \033[41m=[===> Mr. Tom | https://github.com/sunnamsriram1 <===]=\n\033[0m""")
banner()


def download_profile_info(username):
    loader = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        # Print basic profile information
        print(f"\033[32mUsername\033[0m: {profile.username}")
        print(f"\033[32mFull Name\033[0m: {profile.full_name}")
        print(f"\033[32mFollowers\033[0m: {profile.followers}")
        print(f"\033[32mFollowing\033[0m: {profile.followees}")
        print(f"\033[32mID\033[0m: {profile.userid}")
        print(f"\033[32mBio\033[0m: {profile.biography}")
        print(f"\033[32mProfile URL\033[0m: https://www.instagram.com/{profile.username}/")
        print(f"\033[32mUsername\033[0m: {profile.username}")
        print(f"\033[32mProfile Full_Name\033[0m: {profile.full_name}")
        print(f"\033[32mBiography\033[0m: {profile.biography}")
        print(f"\033[32mBusiness Category\033[0m: {profile.business_category_name}")
        print(f"\033[32mExternal URL\033[0m: {profile.external_url}")
        print(f"\033[32mFollowed by Viewer\033[0m: {profile.followed_by_viewer}")
        print(f"\033[32mProfile Followee\033[0m: {profile.followees}")
        print(f"\033[32mFollowed by Viewer\033[0m: {profile.followers}")
        print(f"\033[32mFollows Viewer\033[0m: {profile.follows_viewer}")
        print(f"\033[32mBlocked by Viewer\033[0m: {profile.blocked_by_viewer}")
        print(f"\033[32mHas Blocked Viewer\033[0m: {profile.has_blocked_viewer}")
        print(f"\033[32mHas Highlight Reels\033[0m: {profile.has_highlight_reels}")
        print(f"\033[32mHas Public Story\033[0m: {profile.has_public_story}")
        print(f"\033[32mHas Requested Viewer\033[0m: {profile.has_requested_viewer}")
        print(f"\033[32mRequested by Viewer\033[0m: {profile.requested_by_viewer}")
        print(f"\033[32mHas Viewable Story\033[0m: {profile.has_viewable_story}")
        print(f"\033[32mIGTV Count\033[0m: {profile.igtvcount}")
        print(f"\033[32mIs Business Account\033[0m: {profile.is_business_account}")
        print(f"\033[32mIs Private\033[0m: {profile.is_private}")
        print(f"\033[32mIs Verified\033[0m: {profile.is_verified}")
        print(f"\033[32mMedia Count\033[0m: {profile.mediacount}")
        print(f"\033[32mProfile Picture URL\033[0m: {profile.profile_pic_url}")


        loader.download_profilepic(profile)
        save_to_csv(profile)

        print(f"Profile information for {username} saved to CSV successfully.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile with username {username} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# def download_user_videos(username):
#     loader = instaloader.Instaloader(download_comments=False)

#     try:
#         profile = instaloader.Profile.from_username(loader.context, username)

#         for post in profile.get_posts():
#             if post.is_video:
#                 loader.download_post(post, target=f"{username}_videos")

#         print("Video download completed!")
#     except instaloader.exceptions.ProfileNotExistsException:
#         print("User profile does not exist.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def save_to_csv(profile):
    csv_file_name = f"{profile.username}_profile_data.csv"
    
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Attribute', 'Value'])
        # ... (writing profile data to CSV)
        writer.writerow(['Username =',  profile.username])
        writer.writerow(['Full Name =',  profile.full_name])
        writer.writerow(['Followers =',  profile.followers])
        writer.writerow(['Following =', profile.followees])
        writer.writerow(['ID =',  profile.userid])
        writer.writerow(['Bio =',  profile.biography])
        writer.writerow(['Profile URL =', f"https://www.instagram.com/{profile.username}/"])
        writer.writerow(['Business Category =', profile.business_category_name])
        writer.writerow(['External URL =', profile.external_url])
        writer.writerow(['Followed by Viewer =', profile.followed_by_viewer])
        writer.writerow(['Profile Followee =', profile.followees])
        writer.writerow(['Followed by Viewer =', profile.followers])
        writer.writerow(['Follows Viewer =', profile.follows_viewer])
        writer.writerow(['Blocked by Viewer =', profile.blocked_by_viewer])
        writer.writerow(['Has Blocked Viewer =', profile.has_blocked_viewer])
        writer.writerow(['Has Highlight Reels =', profile.has_highlight_reels])
        writer.writerow(['Has Public Story =', profile.has_public_story])
        writer.writerow(['Has Requested Viewer =', profile.has_requested_viewer])
        writer.writerow(['Requested by Viewer =', profile.requested_by_viewer])
        writer.writerow(['Has Viewable Story =', profile.has_viewable_story])
        writer.writerow(['IGTV Count =', profile.igtvcount])
        writer.writerow(['Is Business Account =', profile.is_business_account])
        writer.writerow(['Is Private =', profile.is_private])
        writer.writerow(['Is Verified =', profile.is_verified])
        writer.writerow(['Media Count =', profile.mediacount])
        writer.writerow(['Profile Picture URL =', profile.profile_pic_url])


        # download_profile_info(username)
        # download_user_videos(username)
# if __name__ == "__main__":
#     while True:
#         try:
#             username = input("\033[36mEnter an Instagram Username (or press Enter to exit): \033[0m").strip()
            
#             if not username:
#                 print("\nExiting...")
#                 sys.exit()
#             else:
#                 download_profile_info(username)
#                 download_user_videos(username)

#         except KeyboardInterrupt:
#             print("\nExiting...")
#             sys.exit()
if __name__ == "__main__":
    #print_banner()
    
    while True:
        try:
            username = input("\033[36mEnter a Instagram Username \033[0m: \033[36m")
            # # Instagram usernames of users
            # username = ["geeks_for_geeks", "chennaiipl", "mumbaiindians",
            #   "royalchallengersbangalore", "kkriders",
            #   "delhicapitals", "sunrisershyd", "kxipofficial"]
            #username = ["s","sprogram00","asha_vaddi","siri.soyam"]
            
            if username == "":
                print("\n\033[33mUnknown Command! Please Enter Instagram UserName\n")
                #sys.exit()
            else:
             #   pass
                download_profile_info(username)
                #download_user_videos(username)
            #else:
                
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
