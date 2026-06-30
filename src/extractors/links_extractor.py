import re


class LinksExtractor:

    @staticmethod
    def extract(text):

        links = {}

        github = re.search(
            r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+",
            text,
            re.I,
        )

        linkedin = re.search(
            r"https?://(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
            text,
            re.I,
        )

        website = re.search(
            r"https?://[^\s]+",
            text,
            re.I,
        )

        if github:
            links["github"] = github.group()

        if linkedin:
            links["linkedin"] = linkedin.group()

        if website:
            links["website"] = website.group()

        return links