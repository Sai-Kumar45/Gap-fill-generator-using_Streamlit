import streamlit as st


# Page 1
def page_home():
    centered_text_style = """
        text-align: center;
    """

    markdown_text = """
    <div style="{}">
    <h3>ENTER TITLE AND TEXT</h3>
    </div>
    """.format(centered_text_style)

    st.markdown(markdown_text, unsafe_allow_html=True)


    if "text_input_value" not in st.session_state:
        st.session_state.text_input_value = ""

    st.session_state.title=st.text_input("  ", placeholder="Enter the title and instructions (optional)")
    text_input = st.text_area(" ", placeholder="Enter the text or a list of questions")
    st.session_state.text_input_value = text_input
    if st.button("Next"):
        st.session_state.page = "Next"

# Page 2
def page_Next():
    st.subheader("select the words to make them gap")

    text_input_value = st.session_state.text_input_value
    if True:
        # st.write(text_input_value)

        selected_words = st.multiselect("Select Words", text_input_value.split())
        text_input_lines = text_input_value.split("\n")
        modified_lines = []
        for line in text_input_lines:
            words = line.split()
            st.session_state.modified_words = []
            for word in words:
                if word in selected_words:
                    st.session_state.modified_words.append("_____")
                else:
                    st.session_state.modified_words.append(word)
            modified_line = ' '.join(st.session_state.modified_words)
            modified_lines.append(modified_line)
            st.write(modified_line)
        st.session_state.modified_text = '\n'.join(modified_lines)

        if st.button("Home"):
            st.session_state.page = "Home"
        if st.button("Next") and selected_words:
            st.session_state.page = "Contact"

# Page 3
def page_contact():
    st.subheader("settings and preview")

    if "selected_option" not in st.session_state:
        st.session_state.selected_option = "show modified text"  # Initialize with the default option

    selected_option = st.selectbox("Select an Option", ["show modified text", "Show only spaces", "Show First Letter", "No Vowels", "No Consonants"])

    # Check if the selected option has changed, if so, update the session state
    if selected_option != st.session_state.selected_option:
        st.session_state.selected_option = selected_option

    st.write("preview")
    title = st.session_state.get("title")
    st.write(title)
    st.write("Student: ","_"*10)
    st.write("date: ","_"*10)
    original_words = st.session_state.text_input_value.split()
    modified_words = st.session_state.modified_words.copy()  # Make a copy to preserve the original modified_words

    if st.session_state.selected_option == "Show only spaces":
        for i in range(len(modified_words)):
            if modified_words[i] == "_____":
                modified_words[i] = "_ " * len(original_words[i])

    elif st.session_state.selected_option == "Show First Letter":
        for i in range(len(modified_words)):
            if modified_words[i] == "_____":
                word = original_words[i]
                first_letter = word[0]
                remaining_letters = " _ " * (len(word) - 1)
                modified_words[i] = f"{first_letter} {remaining_letters}"

    elif st.session_state.selected_option == "No Vowels":
        for i in range(len(modified_words)):
            if modified_words[i] == "_____":
                word = original_words[i]
                modified_word = ''.join(['_' if letter.lower() in 'aeiouAEIOU' else letter for letter in word])
                modified_words[i] = modified_word

    elif st.session_state.selected_option == "No Consonants":
        for i in range(len(modified_words)):
            if modified_words[i] == "_____":
                word = original_words[i]
                modified_word = ''.join(['_' if letter.lower() not in 'aeiouAEIOU' else letter for letter in word])
                modified_words[i] = modified_word

    modified_text = ' '.join(modified_words)
    st.session_state.modified_words = modified_words
    st.session_state.modified_text = modified_text  # Update the modified text
    st.write(modified_text)

    st.write("You can contact us at contact@example.com.")
    if st.button("previous"):
        st.session_state.page = "Next"

if "page" not in st.session_state:
    st.session_state.page = "Home"

if st.session_state.page == "Home":
    page_home()
elif st.session_state.page == "Next":
    page_Next()
elif st.session_state.page == "Contact":
    page_contact()





