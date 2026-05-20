import streamlit as st

from chatbot import generate_response


st.set_page_config(

    page_title="AI Internal Knowledge Chatbot",

    page_icon="🤖",

    layout="centered"
)


with st.sidebar:

    st.header("📘 About")

    st.write(
        """
        This AI chatbot uses Retrieval-Augmented Generation (RAG)
        to answer questions from internal company documents.
        """
    )

    st.markdown("---")

    st.subheader("📂 Knowledge Sources")

    st.write("- HR Policy")
    st.write("- Onboarding Guide")
    st.write("- Technical Wiki")


st.title("🤖 AI Internal Knowledge Chatbot")

st.markdown(
    "Ask questions about company policies, onboarding, or technical documentation."
)


if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


if st.button("🗑 Clear Chat"):

    st.session_state.chat_history = []

    st.rerun()


user_query = st.text_input(

    "Enter your question:"
)


if st.button("Generate Response"):

    if user_query:

        with st.spinner("Generating response..."):

            response, sources = generate_response(user_query)

        st.session_state.chat_history.append(

            ("You", user_query, None)
        )

        st.session_state.chat_history.append(

            ("Bot", response, sources)
        )


for sender, message, sources in st.session_state.chat_history:

    if sender == "You":

        st.markdown("### 🧑 You:")

        st.write(message)

    else:

        st.markdown("### 🤖 Bot:")

        st.write(message)

        if sources:

            st.markdown("#### 📚 Sources Used:")

            for doc in sources:

                source = doc.metadata.get(
                    "source",
                    "Unknown"
                )

                st.write(f"- {source}")