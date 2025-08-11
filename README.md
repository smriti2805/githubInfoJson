# 📂 Portfolio Helper Repository

This repository serves as a **supporting data source** for my main portfolio project: [Portfolio Website](https://github.com/kishandev2509/portfolio). It contains project data in JSON format and an automated update mechanism to keep the portfolio's project section up-to-date without requiring manual redeployment of the portfolio site.

---

## 📌 Purpose

* **Decoupling Data from Portfolio Code** – Prevents redeploying the portfolio site every time project data changes.
* **Automated Data Updates** – Uses a GitHub Actions workflow to periodically refresh `projects_data.json` with the latest repository information.
* **Centralized JSON Data** – Allows multiple projects or clients to access consistent and updated GitHub project information.

---

## 📁 Repository Contents

```
├── projects_data.json      # JSON file containing project details for portfolio
├── update_portfolio.py     # Python script to fetch GitHub repo data and update JSON
└── .github/workflows/
    └── update.yml          # GitHub Actions workflow to auto-update data hourly
```

---

## ⚙️ How It Works

1. **Data Source** – The `update_portfolio.py` script fetches all public, non-fork repositories for the GitHub user `kishandev2509` using the GitHub API.
2. **JSON Generation** – The script writes repository details (name, URL, description, created date, last updated date) into `projects_data.json`.
3. **Automation** – A GitHub Actions workflow (`update.yml`) runs hourly to:

   * Fetch updated repo data.
   * Commit changes to `projects_data.json`.
   * Push updates to this repository.
4. **Portfolio Integration** – The main portfolio site fetches `projects_data.json` from this repo, ensuring the project list stays fresh.

---

## 🚀 Usage

### 1. Clone this Repository

```bash
git clone https://github.com/kishandev2509/githubInfoJson.git
cd githubInfoJson
```

### 2. Run the Update Script Manually

You can run the script locally to regenerate the `projects_data.json` file:

```bash
python update_portfolio.py
```

*(Optional: Set a `GITHUB_TOKEN` environment variable to avoid API rate limits.)*

---

## 📜 License

This repository is licensed under the **MIT License**. You are free to use, modify, and distribute it with proper attribution.

---

## 🙋‍♂️ Author

**Kishan Dev (KD)**\
📧 [kishandevprajapati4@gmail.com](mailto:kishandevprajapati4@gmail.com)\
🔗 [LinkedIn](https://linkedin.com/in/kishandev2509)\
💻 [GitHub](https://github.com/kishandev2509)

> "Automating updates for a portfolio that evolves as you do."
