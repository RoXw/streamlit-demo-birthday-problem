import streamlit as st
from src.birthdayProblem import birthday_paradox
from src.plot import default_birthday_paradox_plot, \
                        default_birthday_problem_plot, \
                        birthday_problem_plot

number_of_days = st.number_input(label="Enter the number of days in year :", min_value=1, step=1)
st.write("Minimum number of individuals required for probability > 50%:", birthday_paradox(number_of_days))
st.plotly_chart(birthday_problem_plot(number_of_days))

days = [10, 100, 365, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]
st.plotly_chart(default_birthday_paradox_plot(days))

