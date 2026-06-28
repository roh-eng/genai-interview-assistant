import sys

import pdfplumber


def extract_resume_text(pdf_path):
    """
    Extract text from uploaded resume PDF
    """

    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python resume_parser.py <path-to-resume.pdf>")
        sys.exit(1)

    pdf_file = sys.argv[1]

    text = extract_resume_text(pdf_file)

    print(text[:1000])