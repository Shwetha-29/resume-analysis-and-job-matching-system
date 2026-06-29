import re
from typing import List

import pdfplumber
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


STOP_WORDS = set(stopwords.words("english"))
NON_ALPHABET_PATTERN = re.compile(r"[^a-zA-Z\s]")


def extract_text_from_pdf(file) -> str:
    """
    Extract text from a PDF file.

    Parameters:
        file: Uploaded PDF file

    Returns:
        Extracted text as a string.
    """

    pages = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                pages.append(page_text)

    text = "\n".join(pages)

    # Remove extra spaces and blank lines
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text: str) -> List[str]:
    """
    Clean extracted text for keyword analysis.

    Steps:
    - Convert to lowercase
    - Remove punctuation and numbers
    - Tokenize
    - Remove stopwords
    - Remove single-character words
    """

    text = text.lower()
    text = NON_ALPHABET_PATTERN.sub(" ", text)

    return [
        word
        for word in word_tokenize(text)
        if len(word) > 1 and word not in STOP_WORDS
    ]