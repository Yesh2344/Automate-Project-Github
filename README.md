# GitHub Projects Showcase 🚀

A dynamic Streamlit web application that automatically showcases your GitHub repositories with a beautiful, responsive card-based interface. The app features real-time GitHub statistics, automatic daily updates, and a modern dark theme design.

## ✨ Features

- **Responsive Grid Layout**: Projects displayed in an elegant 3-column grid
- **Real-time GitHub Stats**: Shows stars and forks for each repository
- **Automatic Updates**: Daily repository synchronization via GitHub Actions
- **Interactive Cards**: Hover effects and smooth animations
- **Dark Theme**: Modern dark interface with gold accents
- **Easy Deployment**: Ready for Streamlit deployment

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/github-projects-showcase.git
cd github-projects-showcase
```

2. Install required dependencies:
```bash
pip install streamlit requests
```

3. Configure your GitHub username:
   - Open `fetch_github_projects.py`
   - Update `GITHUB_USERNAME` with your GitHub username

## 🚀 Usage

1. Run the initial project fetch:
```bash
python fetch_github_projects.py
```

2. Start the Streamlit app:
```bash
streamlit run app.py
```

3. Visit `http://localhost:8501` in your browser

## 🔄 Automatic Updates

The project includes a GitHub Actions workflow that automatically updates your project list daily. The workflow:
- Runs every day at midnight UTC
- Fetches your latest GitHub repositories
- Updates the `projects.json` file
- Commits and pushes changes automatically

