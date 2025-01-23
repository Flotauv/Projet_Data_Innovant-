import streamlit as st
import pandas as pd
import os 
result = os.popen('pip list').read()
st.code(result, language=None)

print(os.name)


def main():
    st.header('HOME PAGE')
    st.title('Dashboard mobilité')



if __name__ == '__main()__':
    main()

