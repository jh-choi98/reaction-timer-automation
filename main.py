from playwright.sync_api import sync_playwright

VIEW_SPLASH = "view-splash"
VIEW_WAITING = "view-waiting"
VIEW_GO = "view-go"
VIEW_RESULT = "view-result"
VIEW_SCORE = "view-score"


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://humanbenchmark.com/tests/reactiontime")
        play_board = page.query_selector("div[class*='view-']")
        cur_class_name = play_board.get_attribute("class")

        while not VIEW_SCORE in cur_class_name:
            cur_class_name = play_board.get_attribute("class")
            if not VIEW_WAITING in cur_class_name:
                play_board.click()
        input()


if __name__ == "__main__":
    main()
