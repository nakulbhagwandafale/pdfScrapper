# 📄 PDF Scrapper – Letters.org Automation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 🚀 Overview

**PDF Scrapper** is a Python-based automation tool built using **Playwright** that navigates through category pages on *letters.org* and downloads each individual letter page as a clean, full-height PDF file.

The script intelligently handles:

- Dynamic page loading  
- Link extraction  
- Filename sanitization  
- Organized folder storage  

---

## 🛠 Features

- ✅ Automated navigation through multiple category pages  
- ✅ Extracts individual letter page links  
- ✅ Converts each letter page into a full-height PDF  
- ✅ Automatically removes invalid filename characters  
- ✅ Organized folder structure (`category/page_x/`)  
- ✅ Skips unwanted pages (Privacy Policy, Contact, etc.)  
- ✅ Headless Chromium browser automation  

---

## 📂 Folder Structure

pdfScrapper/
│
├── scraper.py
├── README.md
└── downloaded_letters/
└── invitation-letter/
├── page_1/
├── page_2/
└── page_3/


---

## ⚙️ Tech Stack

- **Python 3.x**
- **Playwright**
- OS Module
- Regex (`re` module)

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
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

Injects CSS to prevent page breaks

Generates full-height single-page PDF

Saves into structured folders

🎯 Use Cases
Bulk document archiving

Automation practice project

Web scraping learning

Portfolio project for recruiters

⚠️ Disclaimer
This project is for educational and automation purposes only.
Please respect website terms and conditions before scraping content.

👨‍💻 Author
Nakul Dafale
GitHub: https://github.com/nakulbhagwandafale

⭐ Support
If you find this project helpful, consider giving it a star ⭐ on GitHub.


---

# ✅ Now Your README Will:

- Show proper heading sizes  
- Look professional  
- Be clean and structured  
- Impress recruiters  

If you want, I can now make a **premium portfolio-level README (9.5/10 quality)** with GIF demo a
