import streamlit as st
import streamlit.components.v1 as components

st.title("Breast Cancer Assistant")

# Use TRIPLE quotes (three " in a row) to wrap the HTML
chat_code = """
<link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
<script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
<df-messenger
  project-id="breast-cancer-489817"
  agent-id="92851c2f-3fb9-4ff2-b49b-9212d79796e9"
  language-code="en"
  max-query-length="-1">
  <df-messenger-chat-bubble
    chat-title="Breast Cancer Chatbot">
  </df-messenger-chat-bubble>
</df-messenger>
<style>
  df-messenger {
    z-index: 999;
    position: fixed;
    --df-messenger-font-color: #000;
    --df-messenger-font-family: Google Sans;
    --df-messenger-chat-background: #f3f6fc;
    --df-messenger-message-user-background: #d3e3fd;
    --df-messenger-message-bot-background: #fff;
    bottom: 16px;
    right: 16px;
  }
</style>
"""

# This line turns that text into a working chat bubble
components.html(chat_code, height=600)
