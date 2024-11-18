import streamlit as st
from rag_chatbot_ import query_with_memory

st.set_page_config(page_title="Chatbot for Indian Constitution")
with st.sidebar:
    st.title('Chatbot for Indian Constitution')

# Function for generating LLM response
def generate_response(input):
    result = query_with_memory(input)
    return result

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, Ask your questions"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Getting your answer"):
            response = generate_response(input)
            st.write(response['source_documents'][0].page_content)
    message = {"role": "assistant", "content": response['source_documents'][0].page_content}
    st.session_state.messages.append(message)

