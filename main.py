import streamlit as st
from bot_commenter import comment_on_users
from bot_hashtags import get_trending_hashtags
from playwright.sync_api import sync_playwright
import random

# Lista komentara koji će biti korišćeni
comments = [
    "Great video!",
    "I love this!",
    "Amazing content!",
    "Keep up the great work!",
    "This is hilarious!"
]

# Lista hashtagova za pretragu
hashtags = ['#travel', '#funny', '#sports', '#food', '#music']

import asyncio

# Funkcija za nasumično komentarisanje
async def comment_on_video(page):
    # Odaberi nasumičan hashtag
    random_hashtag = random.choice(hashtags)
    print(f"Searching videos for hashtag: {random_hashtag}")
    
    # Otvori stranicu sa hashtagom
    await page.goto(f'https://www.tiktok.com/tag/{random_hashtag}')

    # Čekaj dok se videoe ne učitaju
    await page.wait_for_selector('div[data-e2e="feed-item"]')
    videos = await page.query_selector_all('div[data-e2e="feed-item"]')

    # Nasumično odaberi jedan video
    video = random.choice(videos)

    try:
        # Klikni na dugme za komentarisanje
        comment_button = await video.locator('button[data-e2e="comment-button"]')
        await comment_button.click()

        # Čekaj da se učita tekstualni okvir za komentar
        await page.wait_for_selector('textarea[placeholder="Add a comment..."]')
        comment_box = await page.locator('textarea[placeholder="Add a comment..."]')

        # Nasumično izaberi komentar
        random_comment = random.choice(comments)
        await comment_box.fill(random_comment)

        # Pošaljite komentar
        await comment_box.press("Enter")
        print(f"Comment posted: {random_comment}")
    except Exception as e:
        print(f"Error posting comment: {e}")


st.title("TikTok Bot Dashboard 🤖")

# Dodaj unos za korisničko ime i lozinku
username_input = st.text_input("TikTok korisničko ime")
password_input = st.text_input("TikTok lozinka", type="password")

st.header("1. Auto-comment bot")
usernames_input = st.text_area("TikTok usernames (jedan po liniji)", key="usernames_input")
comments_input = st.text_area("Komentari (jedan po liniji)", key="comments_input")


if st.button("Pokreni auto-komentarisanje", key="start_commenting"):
    users = [u.strip() for u in usernames_input.split("\n") if u.strip()]
    comms = [c.strip() for c in comments_input.split("\n") if c.strip()]
    if users and comms and username_input and password_input:
        st.success("Bot pokrenut!")
        comment_on_users(users, comms, username_input, password_input)
    else:
        st.warning("Popuni oba polja.")

if st.button("Prikaži trendove", key="show_trends"):
    tags = get_trending_hashtags()
    st.write("🔻 Trenutno popularno:")
    for tag in tags:
        st.markdown(f"- {tag}")



import streamlit as st
from bot_commenter import comment_on_users
from bot_hashtags import get_trending_hashtags

st.title("TikTok Bot Dashboard 🤖")

st.header("1. Auto-comment bot")
usernames_input = st.text_area("TikTok usernames (jedan po liniji)")
comments_input = st.text_area("Komentari (jedan po liniji)")

if st.button("Pokreni auto-komentarisanje"):
    users = [u.strip() for u in usernames_input.split("\n") if u.strip()]
    comms = [c.strip() for c in comments_input.split("\n") if c.strip()]
    if users and comms:
        st.success("Bot pokrenut!")
        comment_on_users(users, comms)
    else:
        st.warning("Popuni oba polja.")

st.markdown("---")

st.header("2. Trending Hashtags")
if st.button("Prikaži trendove"):
    tags = get_trending_hashtags()
    st.write("🔻 Trenutno popularno:")
    for tag in tags:
        st.markdown(f"- {tag}")


import asyncio
import json
from playwright.async_api import async_playwright

async def login_to_tiktok():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Pokrećemo u normalnom režimu, ne headless
        context = await browser.new_context()

        # Pokušaj učitati kolačiće, ako postoje
        try:
            with open('cookies.json', 'r') as f:
                cookies = json.load(f)
                await context.add_cookies(cookies)
        except FileNotFoundError:
            print("No cookies found, login required.")

        page = await context.new_page()
        await page.goto("https://www.tiktok.com/login")

        # Ako nismo logovani, moramo se logovati
        if page.url == "https://www.tiktok.com/login":
            print("Login required manually.")
            input("Press Enter after logging in manually...")

            # Sačuvaj kolačiće nakon logovanja
            cookies = await context.cookies()
            with open('cookies.json', 'w') as f:
                json.dump(cookies, f)

        return page, browser
    # Funkcija za pokretanje bota
async def main():
    # Prvo se loguj u TikTok
    page, browser = await login_to_tiktok()

    # Postaviće se automatski komentari svakih 30 do 60 sekundi
    try:
        while True:
            await comment_on_video(page)  # Poziva funkciju za komentarisanje
            print("Waiting before next comment...")
            await asyncio.sleep(random.randint(30, 60))  # Pauza između komentara
    except KeyboardInterrupt:
        print("Bot stopped manually.")
    finally:
        await browser.close()
# Pokreni asinhroni main
if __name__ == "__main__":
    asyncio.run(main())

    
