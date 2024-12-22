import streamlit as st
import time
import webbrowser
st.markdown("<h1 style='text-align: center; color: blue;'>Troll password</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>"
            "I am here to help you to create the strongest password in the world</p>", unsafe_allow_html=True)
def check(p):
    сurrent = time.localtime()
    год = time.strftime("%Y", сurrent)
    day = time.strftime("%a", сurrent)
    date = time.strftime("%m/%d/%Y, %H:%M:%S")
    countnum = 0
    countletrus = 0
    countletrus2 = 0
    for symbol in p:
        if symbol in "1234567890":
            countnum +=1
    for symbol in p:
        if symbol in "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
            countletrus +=1
    for symbol in p:
        if symbol in "йцукенгшщзхъфывапролджэячсмитьбю":
            countletrus2 +=1
    if len(p) <= 3:
        st.text("маловато будет")
    elif len(p) > 28:
        st.text("тормози слишком много")
    elif год in p:
        st.text("этот год плохой он мне не нравится")
    elif "9" in p:
        st.text("я запрещаю тебе эту цифру")
    elif "123" in p:
        st.text("вот каких паролей тебе стоит избегать:")
        webbrowser.open("https://www.novostiitkanala.ru/news/detail.php?ID=175274#:~:text=%D0%9F%D0%BE%20%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B0%D0%BC%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%20%D0%B2%D1%81%D0%B5%D0%B9%20%D0%BC%D0%B0%D1%81%D1%81%D1%8B,%2C%2012345678%2C%20111111%20%D0%B8%201q2w3e.")
    elif day not in p:
        st.text("Пароль должен содержать сегодняшний день недели с сокращённым названием ")
    elif date in p:
        st.text("зачем ты полную дату поставил чудила?")
    elif countnum <= 3:
        st.text("Мало цифр")
    elif countletrus >0 or countletrus2 >0:
        st.text("Нельзя русские буквы")
    else:
        st.text("неплохой пароль,хорошая работа,вот твоя награда")
        st.link_button( "награда","https://www.youtube.com/watch?v=dQw4w9WgXcQ")
p = st.text_input('Enter a password', max_chars = 15 , type = "password" )
check(p)