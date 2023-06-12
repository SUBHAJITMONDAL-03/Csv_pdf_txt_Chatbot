import streamlit as st

class Sidebar:
    

    MODEL_OPTIONS = ["gpt-3.5-turbo", "gpt-4"]
    TEMPERATURE_MIN_VALUE = 0.0
    TEMPERATURE_MAX_VALUE = 1.0
    TEMPERATURE_DEFAULT_VALUE = 0.0
    TEMPERATURE_STEP = 0.01
    CHUNK_SIZE_MIN_VALUE = 0
    CHUNK_SIZE_MAX_VALUE = 2500
    CHUNK_SIZE_DEFAULT_VALUE = 0
    CHUNK_SIZE_STEP = 50

    @staticmethod
    def about():
        about = st.sidebar.expander("🧠 About Pwcbot ")
        sections = [
            "#### PwCbot is an AI chatbot with a conversational memory, designed to allow users to discuss their data in a more intuitive way. 📄",
            "#### It uses large language models to provide users with natural language interactions about user data content. 🌐",
            "#### Powered by [Langchain](https://github.com/hwchase17/langchain), [OpenAI](https://platform.openai.com/docs/models/gpt-3-5) and [Streamlit](https://github.com/streamlit/streamlit) ⚡",
            "**Mail** : subhajit8903@gmail.com",
            "**Created by Subhajit Mondal**",

      ]
        for section in sections:
            about.write(section)

    @staticmethod
    def reset_chat_button():
        if st.button("Reset chat"):
            st.session_state["reset_chat"] = True
        st.session_state.setdefault("reset_chat", False)

    def model_selector(self):
        model = st.selectbox(label="Model", options=self.MODEL_OPTIONS)
        st.session_state["model"] = model

    def temperature_slider(self):
        temperature = st.slider(
            label="Temperature",
            min_value=self.TEMPERATURE_MIN_VALUE,
            max_value=self.TEMPERATURE_MAX_VALUE,
            value=self.TEMPERATURE_DEFAULT_VALUE,
            step=self.TEMPERATURE_STEP,
        )
        st.session_state["temperature"] = temperature
    def chunk_size_slider(self):
        chunk_size = st.slider(
            label="Chunk Size (Word Count)",
            min_value=self.CHUNK_SIZE_MIN_VALUE,
            max_value=self.CHUNK_SIZE_MAX_VALUE,
            value=self.CHUNK_SIZE_DEFAULT_VALUE,
            step=self.CHUNK_SIZE_STEP,
        )
        st.session_state["chunk_size"] = chunk_size
        
    def show_options(self):
        with st.sidebar.expander("🛠️ PwCbot's Tools", expanded=False):

            self.reset_chat_button()
            self.model_selector()
            self.temperature_slider()
            st.session_state.setdefault("model", self.MODEL_OPTIONS[0])
            st.session_state.setdefault("temperature", self.TEMPERATURE_DEFAULT_VALUE)
            st.session_state.setdefault("chunk_size", self.CHUNK_SIZE_DEFAULT_VALUE)

    