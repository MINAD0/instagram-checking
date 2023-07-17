from instaloader import Instaloader, Profile
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Menu design
menu_design = f"""
{Fore.GREEN}╔══════════════════════════════════════╗
{Fore.GREEN}║        Instagram Follower Checker      ║
{Fore.GREEN}╠══════════════════════════════════════╣
{Fore.GREEN}║                                        ║
{Fore.GREEN}║     {Fore.CYAN}1. Check Followers                {Fore.GREEN}║
{Fore.GREEN}║     {Fore.CYAN}2. Check Following                {Fore.GREEN}║
{Fore.GREEN}║     {Fore.CYAN}3. Find Unfollowers               {Fore.GREEN}║
{Fore.GREEN}║     {Fore.CYAN}4. Exit                            {Fore.GREEN}║
{Fore.GREEN}║                                        ║
{Fore.GREEN}╚══════════════════════════════════════╝
"""

# Color codes for different parts of the output
COLOR_FOLLOWERS = Fore.YELLOW
COLOR_FOLLOWING = Fore.MAGENTA
COLOR_UNFOLLOWERS = Fore.RED


def clear_screen():
    """Clear the console screen."""
    print("\033c", end="")


def count_followers(username, password):
    try:
        loader = Instaloader()
        loader.login(username, password)  # Login using the Instagram account

        profile = Profile.from_username(loader.context, username)

        followers_count = profile.followers
        following_count = profile.followees

        print(f"{COLOR_FOLLOWERS}Your Followers: {followers_count}")
        print(f"{COLOR_FOLLOWING}Your Following: {following_count}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def find_unfollowers(username, password):
    try:
        loader = Instaloader()
        loader.login(username, password)  # Login using the Instagram account

        profile = Profile.from_username(loader.context, username)

        followers = set(profile.get_followers())
        following = set(profile.get_followees())

        unfollowers = following - followers

        if unfollowers:
            print(f"{COLOR_UNFOLLOWERS}Users you follow but who don't follow you back:")
            for user in unfollowers:
                print(f"{COLOR_UNFOLLOWERS}{user.username} - did not follow you back")
        else:
            print(f"{COLOR_UNFOLLOWERS}No users found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    clear_screen()
    print(menu_design)
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            clear_screen()
            username = input("Enter your Instagram username: ")
            password = input("Enter your Instagram password: ")
            count_followers(username, password)
        elif choice == "2":
            clear_screen()
            username = input("Enter your Instagram username: ")
            password = input("Enter your Instagram password: ")
            count_following(username, password)
        elif choice == "3":
            clear_screen()
            username = input("Enter your Instagram username: ")
            password = input("Enter your Instagram password: ")
            find_unfollowers(username, password)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
