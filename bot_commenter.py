from playwright.sync_api import sync_playwright
import time, random

# Funkcija za login na TikTok
def login_to_tiktok(page, username, password):
    page.goto("https://www.tiktok.com/login")
    time.sleep(2)

    # Unos korisničkog imena
    page.fill("input[name='username']", username)
    time.sleep(1)

    # Unos lozinke
    page.fill("input[name='password']", password)
    time.sleep(1)

    # Klikni na login dugme
    page.click("button[type='submit']")
    time.sleep(5)  # Sačekaj da se uloguje

# Funkcija za komentarisanje
def comment_on_users(usernames, comments, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Login na TikTok prije svega
        login_to_tiktok(page, username, password)

        for user in usernames:
            try:
                page.goto(f"https://www.tiktok.com/@{user}")
                page.wait_for_timeout(3000)
                page.click('xpath=(//div[@data-e2e="user-post-item"])[1]')  # prvi video
                page.wait_for_timeout(5000)

                comment = random.choice(comments)
                page.click('xpath=//div[contains(@class,"public-DraftStyleDefault-block")]')
                page.keyboard.type(comment)
                page.keyboard.press("Enter")
                time.sleep(4)
            except Exception as e:
                print(f"[!] Greška za korisnika {user}: {e}")

        browser.close()


from playwright.sync_api import sync_playwright
import random

# Funkcija za komentarisanje
def comment_on_users(usernames, comments, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Login na TikTok prije svega
        login_to_tiktok(page, username, password)

        for user in usernames:
            try:
                page.goto(f"https://www.tiktok.com/@{user}")
                page.wait_for_timeout(random.randint(8, 15) * 1000)  # Nasumično čekanje između 8 i 15 sekundi
                page.click('xpath=(//div[@data-e2e="user-post-item"])[1]')  # prvi video
                page.wait_for_timeout(random.randint(10, 20) * 1000)  # Nasumično čekanje između 10 i 20 sekundi

                comment = random.choice(comments)
                page.click('xpath=//div[contains(@class,"public-DraftStyleDefault-block")]')
                page.keyboard.type(comment)
                page.keyboard.press("Enter")
                
                # Dodajemo veću nasumičnost između 6-12 sekundi nakon komentarisanja
                time.sleep(random.randint(6, 12))

            except Exception as e:
                print(f"[!] Greška za korisnika {user}: {e}")

        browser.close()
