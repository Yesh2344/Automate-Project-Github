import streamlit as st
import json

# Load projects from JSON
def load_projects():
    try:
        with open("projects.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

projects = load_projects()

st.title("📌 My GitHub Projects")

if projects:
    for project in projects:
        st.subheader(f"🔹 {project['name']}")
        st.write(project['description'])
        st.markdown(f"[🔗 View on GitHub]({project['url']})")
else:
    st.write("No projects found. Run `fetch_github_projects.py` to update.")

