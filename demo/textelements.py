import streamlit as st

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

md = st.text_area('Type in your markdown string (without outer quotes)',
                  "Happy Streamlit-ing! :balloon:")

st.code(f"""
import streamlit as st

st.markdown('''{md}''')
""")

st.markdown(md)

st.title('这个是一个标题')

st.title('_Streamlit_ is :bulue[cool] :sunglasses:')

st.header('这个是一个头部',divider='rainbow')

st.header('_Streamlit_ is :blue[cool] :sunglasses:')

st.subheader('这是一个子标题',divider='rainbow')

st.caption('这是一个说明栏.')


st.title('下面是一段python代码')
code = '''def hello():
        print("Hello,Streamlit!")'''
st.code(code,language='python')


st.text('This is some text.')

st.latex(r'''
         a+ar+a r^2+a r^3+\cdots + a r^{n-1}=
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^{n}}{1-r}\right)''')

st.divider()

st.write("This is some text.")
st.text('This is som text')

st.slider("This is a slider",0,100,(25,75))
st.divider()