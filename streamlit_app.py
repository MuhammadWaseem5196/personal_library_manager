import streamlit as st
import json


def load_library():
    try:
        with open("library.json", "r") as file:  
            return json.load(file)
    except FileNotFoundError:
        return []


def save_library():
    with open("library.json", "w") as file: 
        json.dump(library, file, indent=4)  
        
library = load_library()

st.title("Personal Library Manager")

menu = st.sidebar.radio("Select an option", ["View Library", "Search Book", "Add Book", "Remove Book", "Save & Exit"])

if menu == "View Library":
    st.sidebar.header("Your Library")  
    if library:
        st.table(library)
    else:
        st.write("Library is Empty. Would you like to add Books?")

elif menu == "Add Book":
    st.sidebar.header("Add Book")  
    title = st.text_input("Title")  
    author = st.text_input("Author")  
    year = st.number_input("Select Year", max_value=2026, min_value=2000, step=1)  
    genre = st.text_input("Genre")  
    read_status = st.checkbox("Have you read this book?")  

    if st.button("Add Book"):
        library.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        })
        save_library()
        st.success("Book Added Successfully")
        

elif menu == "Remove Book":
    st.sidebar.header("Remove Book")  
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select Book To Remove", book_titles)  
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library()
            st.success("Book Removed Successfully")
            st.rerun()
    else:
        st.warning("Library is empty. Add some books first!")

elif menu == "Search Book":
    st.sidebar.header("Search Book")  
    search = st.text_input("Enter Title of Book")  

    if st.button("Search"):
        result = [book for book in library if search.lower() in book["title"].lower()]  # Fixed incorrect search reference

        if result:
            st.table(result)
        else:
            st.warning("Book not found.")

elif menu == "Save & Exit":
    st.sidebar.header("Save & Exit") 
    if st.button("Save"):
        st.table(library)
        save_library()
        st.success("Library Saved Successfully")
