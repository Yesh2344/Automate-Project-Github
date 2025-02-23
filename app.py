import streamlit as st
import json
import requests

# Load projects from JSON
def load_projects():
    try:
        with open("projects.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

projects = load_projects()

# Function to fetch GitHub stats (stars & forks)
def get_github_stats(repo_url):
    try:
        repo_name = "/".join(repo_url.split("/")[-2:])
        api_url = f"https://api.github.com/repos/{repo_name}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data.get("stargazers_count", 0), data.get("forks_count", 0)
    except:
        return 0, 0
    return 0, 0

# Custom CSS Styles
st.markdown("""
    <style>
        .project-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }
        .project-card {
            background: #1e1e2f;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
            transition: transform 0.3s ease-in-out;
            width: 300px;
        }
        .project-card:hover {
            transform: scale(1.07);
            box-shadow: 0px 8px 20px rgba(255, 215, 0, 0.5);
        }
        .project-title {
            font-size: 18px;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 5px;
        }
        .project-desc {
            font-size: 14px;
            color: #ddd;
            margin-bottom: 10px;
        }
        .github-link {
            font-size: 14px;
            color: #1DB954;
            font-weight: bold;
            text-decoration: none;
        }
        .github-link:hover {
            color: #ff5555;
        }
        .stats {
            font-size: 13px;
            color: #aaa;
        }
    </style>
""", unsafe_allow_html=True)

# Display Projects in a Responsive Grid
st.title("🚀 My GitHub Projects")

if projects:
    cols = st.columns(3)  # Creates a 3-column layout

    for i, project in enumerate(projects):
        stars, forks = get_github_stats(project["url"])  # Fetch GitHub stats

        with cols[i % 3]:  # Alternate between 3 columns
            st.markdown(f"""
                <div class="project-card">
                    <p class="project-title">🔹 {project['name']}</p>
                    <p class="project-desc">{project['description']}</p>
                    <p class="stats">⭐ {stars} | 🍴 {forks}</p>
                    <a class="github-link" href="{project['url']}" target="_blank">🔗 View on GitHub</a>
                </div>
            """, unsafe_allow_html=True)
else:
    st.warning("No projects found. Run `fetch_github_projects.py` to update.")
