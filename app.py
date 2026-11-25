import streamlit as st


//1

st.title("Обичаш ли Python?")

answer = st.radio("Обичаш ли Python?",
    ["да", "не"]
)


//2

if answer == "да":
    st.success("Супер!")
else:
    st.error("Ще го харесаш!")

    import streamlit as st

st.title("Голямо или малко число?")

number = st.number_input("Въведи число:")

if number > 10:
    st.write("Голямо число")
else:
    st.write("Малко число")

    //3

    import streamlit as st

st.title("Мини тест по математика")

answer = st.number_input("Колко е 5 × 5?", step=1)

if st.button("Провери"):
    if answer == 25:
        st.success("Вярно! Браво!")
    else:
        st.error("Грешно! Опитай отново!")

        //4

        import streamlit as st

st.title("Калкулатор за оценка")

grade = st.number_input(
    "Въведи оценка от 2 до 6:",
    min_value=2,
    max_value=6,
    step=1
)

if st.button("Провери"):
    if grade == 6:
        st.success("Отличен резултат!")
    elif grade == 5:
        st.success("Много добър резултат!")
    elif grade == 4:
        st.info("Добър резултат!")
    elif grade == 3:
        st.warning("Среден резултат!")
    else:
        st.error("Слаб резултат!")

        //5

        st.title("Игра: Познай числото")

# Правилното число
pravilno_chislo = 7

# Поле за въвеждане на число
chislo = st.number_input("Въведете число:", step=1)

# Бутон за проверка
if st.button("Провери"):
    if chislo == pravilno_chislo:
        st.success("Поздравления! Позна!")
    elif chislo > pravilno_chislo:
        st.warning("Опитай с по-малко число!")
    else:
        st.info("Опитай с по-голямо число!")
