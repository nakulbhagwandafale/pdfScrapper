📄 PDF Scrapper – Letters.org Automation

🚀 Overview

PDF Scrapper is a Python-based automation tool built using Playwright that navigates through category pages on letters.org and downloads each individual letter page as a clean, full-height PDF file.

The script intelligently handles:

Dynamic page loading

Link extraction

Filename sanitization

Organized folder storage

🛠 Features

✅ Automated navigation through multiple category pages
✅ Extracts individual letter page links
✅ Converts each letter page into a full-height PDF
✅ Automatically removes invalid filename characters
✅ Organized folder structure (category/page_x/)
✅ Skips unwanted pages (Privacy Policy, Contact, etc.)
✅ Headless Chromium browser automation

📸 Project Workflow

You can add screenshots inside a folder named assets in your repo.

Example structure:

pdfScrapper/
│
├── scraper.py
├── README.md
└── assets/
    ├── workflow.png
    ├── output_example.png


Then use:

![Workflow](assets/workflow.png)


Example:

🔍 Script Execution

📂 Folder Structure
downloaded_letters/
    invitation-letter/
        page_1/
        page_2/
        page_3/

⚙️ Tech Stack

Python 3.x

Playwright

OS Module

Regex (re module)

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/nakulbhagwandafale/pdfScrapper.git
cd pdfScrapper

2️⃣ Install Dependencies
pip install playwright
playwright install

▶️ Usage

Update configuration inside the script:

CATEGORY_NAME = "invitation-letter"
PAGE_URLS = [
    "https://www.letters.org/category/invitation-letter",
]


Run the script:

python scraper.py

🧠 How It Works

Launches headless Chromium browser

Navigates to category pages

Extracts valid letter links

Visits each letter page

Injects CSS to avoid page breaks

Generates full-height single-page PDF

Saves into structured folders

🎯 Use Cases

Bulk document archiving

Automation practice project

Web scraping learning

Portfolio project for recruiters

⚠️ Disclaimer

This project is for educational purposes only. Please respect website terms and conditions before scraping.

👨‍💻 Author

Nakul Dafale
GitHub: https://github.com/nakulbhagwandafale