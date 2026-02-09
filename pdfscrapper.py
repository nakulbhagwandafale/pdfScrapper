import os
import re
from playwright.sync_api import sync_playwright

# Configuration - Update these for each run
CATEGORY_NAME = "invitation-letter"

PAGE_URLS = [
    "https://www.letters.org/category/invitation-letter",
    "https://www.letters.org/category/invitation-letter/page/2",
    "https://www.letters.org/category/invitation-letter/page/3",
    "https://www.letters.org/category/invitation-letter/page/4",
    "https://www.letters.org/category/invitation-letter/page/5",
    "https://www.letters.org/category/invitation-letter/page/6",
]

OUTPUT_BASE_DIR = "downloaded_letters"


def sanitize_filename(name):
    """Clean the title to be a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()


def main():
    if not PAGE_URLS:
        print("No URLs provided in PAGE_URLS. Exiting.")
        return

    total_downloaded_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        print(f"Starting download for category: {CATEGORY_NAME}")
        print(f"Total pages to process: {len(PAGE_URLS)}\n")

        for i, page_url in enumerate(PAGE_URLS, start=1):
            print(f"--- Processing Page {i}/{len(PAGE_URLS)}: {page_url} ---")

            current_output_dir = os.path.join(
                OUTPUT_BASE_DIR, CATEGORY_NAME, f"page_{i}"
            )
            os.makedirs(current_output_dir, exist_ok=True)

            try:
                print(f"Navigating to {page_url}...")
                page.goto(page_url, wait_until="networkidle")

                # Scroll to bottom for lazy-loaded elements
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(2000)

                # Extract letter links
                links = page.locator("a").evaluate_all("""
                    elements => elements
                        .map(e => ({href: e.href, text: e.innerText}))
                        .filter(link =>
                            link.href.includes('/invitation-letter/') &&
                            link.href.endsWith('.html'))
                """)

                # Deduplicate links
                unique_links = {}
                for link in links:
                    if link["href"] not in unique_links:
                        unique_links[link["href"]] = link["text"]

                print(f"Found {len(unique_links)} potential letters on page {i}.")

                initial_page_count = 0

                for url, title in unique_links.items():
                    term_check = (title or "").lower()
                    url_check = url.lower()

                    if (
                        "privacy policy" in term_check
                        or "contact" in term_check
                        or "privacy-policy" in url_check
                        or "/contact" in url_check
                    ):
                        print(f"Skipping ignored page: {title} ({url})")
                        continue

                    try:
                        if not title or title.strip() == "":
                            title = (
                                url.split("/")[-1]
                                .replace(".html", "")
                                .replace("-", " ")
                                .title()
                            )

                        filename = sanitize_filename(title) + ".pdf"
                        filepath = os.path.join(current_output_dir, filename)

                        print(f"Downloading: {title} -> {filename}")

                        page.goto(url, wait_until="networkidle")

                        # Prevent page breaks inside elements
                        page.add_style_tag(content="""
                            p, h1, h2, h3, h4, h5, h6, li, blockquote,
                            pre, code, table, tr, th, td {
                                page-break-inside: avoid;
                                break-inside: avoid;
                            }
                            div {
                                page-break-inside: auto;
                            }
                        """)

                        full_height = page.evaluate("document.body.scrollHeight")
                        pdf_height = full_height + 50

                        page.pdf(
                            path=filepath,
                            width="1200px",
                            height=f"{pdf_height}px",
                            print_background=True,
                        )

                        total_downloaded_count += 1
                        initial_page_count += 1

                    except Exception as e:
                        print(f"Failed to download {url}: {e}")

                print(
                    f"Finished Page {i}. Downloaded {initial_page_count} PDFs."
                )

            except Exception as e:
                print(f"Failed to process page URL {page_url}: {e}")

        browser.close()

    print(f"\nAll pages processed for '{CATEGORY_NAME}'.")
    print(f"Total PDFs downloaded: {total_downloaded_count}")


if __name__ == "__main__":
    main()
