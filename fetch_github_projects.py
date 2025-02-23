import requests
import json

GITHUB_USERNAME = "yesh2344"
API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

def fetch_github_projects():
    response = requests.get(API_URL)
    if response.status_code == 200:
        projects = [
            {
                "name": proj["name"],
                "description": proj["description"] or "No description available.",
                "url": proj["html_url"]
            }
            for proj in response.json()
        ]
        with open("projects.json", "w") as file:
            json.dump(projects, file, indent=4)
        print("✅ GitHub Projects Updated!")
    else:
        print("❌ Failed to fetch projects.")

if __name__ == "__main__":
    fetch_github_projects()
