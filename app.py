import streamlit as st
from pathlib import Path
import base64

# Initial page config

st.set_page_config(
     page_icon='streamlit.png',
     page_title='Streamlit-Cheat-Sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

# Thanks to streamlitopedia for the following code snippet

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar

def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=275 height=140>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Streamlit cheat sheet')
    st.sidebar.markdown('''<small>Developed by <b>Jayanthan Senthilkumar<b></small>''', unsafe_allow_html=True)
    st.sidebar.markdown('''
<small>For more [Contributions](https://docs.streamlit.io/library/cheatsheet), as of [Streamlit v1.32.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__Install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.code('''
# Import convention
>>> import streamlit as st
''')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
# Just add it after st.sidebar:
>>> a = st.sidebar.radio(\'Choose:\',[1,2])
    ''')

    st.sidebar.markdown('__Magic commands__')
    st.sidebar.code('''
'_This_ is some __Markdown__'
a=3
'dataframe:', data
''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')
    st.sidebar.markdown('<small>Learn more about [experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>', unsafe_allow_html=True)
    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>May 2024 | [<b>Jayanthan Senthilkumar<b>](https://github.com/jayanthansenthilkumar)</small>''', unsafe_allow_html=True)
    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():
    st.title("Streamlit - The Framework in Python")
    st.header("What is Streamlit ???")
    st.markdown("Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. Build and deploy powerful data apps in minutes. Let's get started!")
    col1, col2, = st.columns(2)
    #######################################
    # COLUMN 1
    #######################################
    # Display text
    col1.title('Display text')
    col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

    ''')

    # Display data

    col1.title('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')
    # Display media
    col1.title('Display media')
    col1.code('''
st.image('./header.png')
st.audio(data)
st.video(data)
    ''')
    # Columns
    col1.title('Columns')
    col1.code('''
col1, col2 = st.columns(2)
col1.write('Column 1')
col2.write('Column 2')

# Three columns with different widths
col1, col2, col3 = st.columns([3,1,1])
# col1 is wider
              
# Using 'with' notation:
>>> with col1:
>>>     st.write('This is column 1')
              
''')
    # Tabs
    col1.title('Tabs')
    col1.code('''
# Insert containers separated into tabs:
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> tab1.write("this is tab 1")
>>> tab2.write("this is tab 2")

#How to create a Column inside the tab
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
>>> with tab1:
        col1,col2=st.columns(2)
        col1.write("this is tab 1 and col1")
        col2.write("this is tab 2 and col2")
>>> with tab2:
        col1,col2=st.columns(2)
        col1.write("this is tab 1 and col1")
        col2.write("this is tab 2 and col2")
              
# You can also use "with" notation:
>>> with tab1:
>>>   st.radio('Select one:', [1, 2])
''')
    # Control flow
    col1.title('Control flow')
    col1.code('''
# Stop execution immediately:
st.stop()
# Rerun script immediately:
st.experimental_rerun()

# Group multiple widgets:
>>> with st.form(key='my_form'):
>>>   username = st.text_input('Username')
>>>   password = st.text_input('Password')
>>>   st.form_submit_button('Login')
''')
    # Personalize apps for users
    col1.title('Personalize apps for users')
    col1.code('''
# Show different content based on the user's email address.
>>> if st.user.email == 'jane@email.com':
>>>    display_jane_content()
>>> elif st.user.email == 'adam@foocorp.io':
>>>    display_adam_content()
>>> else:
>>>    st.write("Please contact us to get access!")
''')
    #######################################
    # COLUMN 2
    #######################################
    # Display interactive widgets
    col2.title('Display interactive widgets')
    col2.code('''
st.button('Hit me')
st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
    ''')
    col2.code('''
# Use widgets\' returned values in variables
>>> for i in range(int(st.number_input('Num:'))): foo()
>>> if st.sidebar.selectbox('I:',['f']) == 'f': b()
>>> my_slider_val = st.slider('Quinn Mallory', 1, 88)
>>> st.write(slider_val)
    ''')
    col2.code('''
# Disable widgets to remove interactivity:
>>> st.slider('Pick a number', 0, 100, disabled=True)
              ''')
    # Build chat-based apps
    col2.title('Build chat-based apps')
    col2.code('''
# Insert a chat message container.
>>> with st.chat_message("user"):
>>>    st.write("Hello 👋")
>>>    st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
>>> st.chat_input("Say something")          
''')

    col2.markdown('<small>Learn how to [build chat-based apps](https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps)</small>', unsafe_allow_html=True)

    # Mutate data

    col2.title('Mutate data')
    col2.code('''
# Add rows to a dataframe after
# showing it.
>>> element = st.dataframe(df1)
>>> element.add_rows(df2)

# Add rows to a chart after
# showing it.
>>> element = st.line_chart(df1)
>>> element.add_rows(df2)
''')
    # Display code
    col1.title('Display code')
    col1.code('''
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')
    # Placeholders, help, and options
    col2.title('Placeholders, help, and options')
    col2.code('''
# Replace any single element.
>>> element = st.empty()
>>> element.line_chart(...)
>>> element.text_input(...)  # Replaces previous.

# Insert out of order.
>>> elements = st.container()
>>> elements.line_chart(...)
>>> st.write("Hello")
>>> elements.text_input(...)  # Appears above "Hello".
              
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
st.experimental_show(objects)
st.experimental_get_query_params()
st.experimental_set_query_params(**params)
    ''')
    #######################################
    # COLUMN 3
    #######################################
    # Connect to data sources
    col1.title('Connect to data sources')
    col1.code('''
st.experimental_connection('pets_db', type='sql')
conn = st.experimental_connection('sql')
conn = st.experimental_connection('snowpark')
>>> class MyConnection(ExperimentalBaseConnection[myconn.MyConnection]):
>>>    def _connect(self, **kwargs) -> MyConnection:
>>>        return myconn.connect(**self._secrets, **kwargs)
>>>    def query(self, query):
>>>       return self._instance.query(query)
              ''')
    # Optimize performance
    col2.title('Optimize performance')
    col2.write('Cache data objects')
    col2.code('''
# E.g. Dataframe computation, storing downloaded data, etc.
>>> @st.cache_data
... def foo(bar):
...   # Do something expensive and return data
...   return data
# Executes foo
>>> d1 = foo(ref1)
# Does not execute foo
# Returns cached item by value, d1 == d2
>>> d2 = foo(ref1)
# Different arg, so function foo executes
>>> d3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear values from *all* in-memory or on-disk cached functions
>>> st.cache_data.clear()
    ''')
    col2.write('Cache global resources')
    col2.code('''
# E.g. TensorFlow session, database connection, etc.
>>> @st.cache_resource
... def foo(bar):
...   # Create and return a non-data object
...   return session
# Executes foo
>>> s1 = foo(ref1)
# Does not execute foo
# Returns cached item by reference, s1 == s2
>>> s2 = foo(ref1)
# Different arg, so function foo executes
>>> s3 = foo(ref2)
# Clear all cached entries for this function
>>> foo.clear()
# Clear all global resources from cache
>>> st.cache_resource.clear()
    ''')
    col2.write('Deprecated caching')
    col2.code('''
>>> @st.cache
... def foo(bar):
...   # Do something expensive in here...
...   return data
>>> # Executes foo
>>> d1 = foo(ref1)
>>> # Does not execute foo
>>> # Returns cached item by reference, d1 == d2
>>> d2 = foo(ref1)
>>> # Different arg, so function foo executes
>>> d3 = foo(ref2)
    ''')
    # Display progress and status
    col1.title('Display progress and status')
    col1.code('''
# Show a spinner during a process
>>> with st.spinner(text='In progress'):
>>>   time.sleep(3)
>>>   st.success('Done')

# Show and update progress bar
>>> bar = st.progress(50)
>>> time.sleep(3)
>>> bar.progress(100)

st.balloons()
st.snow()
st.toast('Mr Stay-Puft')
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
    ''')
    return None
# Run main()
if __name__ == '__main__':
    main()