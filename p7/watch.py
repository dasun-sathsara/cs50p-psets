import re


def main():
    url = """
        <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>"""

    print(parse(url))


def parse(html_str: str) -> str:
    template = "https://youtu.be/"
    url_extract = r"src=\"(?:https?://)?(?:www.)?\w+\.\w+/embed/([^/\s\"]+)"
    video_id = re.search(url_extract, html_str)

    if video_id:
        return f"{template}{video_id.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
