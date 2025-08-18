import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo

import requests


def convert_utc_to_ist(utc_time_str: str) -> str:
    utc_time = datetime.strptime(utc_time_str, "%Y-%m-%dT%H:%M:%SZ") # Parse the UTC datetime string
    utc_time = utc_time.replace(tzinfo=ZoneInfo("UTC")) # Convert to UTC (just to ensure it's aware)
    ist_time = utc_time.astimezone(ZoneInfo("Asia/Kolkata")) # Convert to IST (Asia/Kolkata)
    return ist_time.strftime("%Y-%m-%d %H:%M") # Return the formatted time in the desired format
    
def get_projects(username: str):
    url = f"https://api.github.com/users/{username}/repos"

    # Optional: GitHub token to avoid rate limiting
    # headers = { "Authorization": "token YOUR_GITHUB_TOKEN" }

    response = requests.get(url)  # add headers=headers if using token
    projects_data = []
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            project = {}
            if repo["fork"]:
                continue
            project["display_name"] = " ".join(re.split("[-_]", repo["name"])).title()
            project["name"] = repo["name"]
            project["html_url"] = repo["html_url"]
            project["description"] = repo["description"]
            project["user"] = repo["owner"]["login"]
            project["created_at"] = convert_utc_to_ist(repo["created_at"])
            project["updated_at"] = convert_utc_to_ist(repo["updated_at"])
            project["homepage"] = repo["homepage"]
            projects_data.append(project)

        with open("projects_data.json", "w", encoding="utf-8") as f:
            json.dump(projects_data, f, indent=4)

        print("✅ Repository data saved to 'projects_data.json'")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    get_projects("smriti2805")
