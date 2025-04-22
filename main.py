import streamlit as st
from bot_commenter import comment_on_users
from bot_hashtags import get_trending_hashtags

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