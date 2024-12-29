import re
import os
import csv


def md_to_csv(md_file_path):
    """
    Parses a markdown file that contains multiple sections (companies)
    with markdown tables of questions and outputs each section
    into a separate CSV file.
    """

    # Regex to detect section headers.
    # Adjust the pattern for your actual headings, e.g. r"##\s+(\d\.\s+)?(.*)" if needed.
    section_header_pattern = re.compile(r"^#+\s+(\d\.\s+)?(.*)")

    # Regex to detect table rows of the form: |1  | [Title](https://link) |
    # We capture:
    #   group(1) -> question number
    #   group(2) -> question text
    #   group(3) -> question link
    row_pattern = re.compile(r"^\|\s*(\d+)\s*\|\s*\[(.*?)\]\((.*?)\)\s*\|?")

    current_section = None  # Keep track of which company's section we're in
    rows = []  # Accumulate rows for the current section

    with open(md_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Check if the line is a new section header
            header_match = section_header_pattern.match(line)
            if header_match:
                # If we already have a current_section, write out CSV for that section
                if current_section and rows:
                    write_rows_to_csv(current_section, rows)
                    rows = []

                # Extract the name from the header
                # group(2) should be the section name for this pattern
                current_section = header_match.group(2).strip()
                # You might want to clean the name, e.g. remove punctuation or spaces
                current_section = sanitize_filename(current_section)
                continue

            # Check if the line matches a table row for a question
            row_match = row_pattern.match(line)
            if row_match:
                # question_number = row_match.group(1).strip()
                question_text = row_match.group(2).strip()
                question_link = row_match.group(3).strip()

                rows.append((question_text, question_link))

        # End of file: if there's a last section with rows, write them out
        if current_section and rows:
            write_rows_to_csv(current_section, rows)


def write_rows_to_csv(section_name, rows):
    """
    Writes the collected rows (questions) for a given section (company) into a CSV file.
    CSV format:
        No., Question, Link
    """
    csv_filename = f"{section_name}.csv"
    print(f"Creating CSV: {csv_filename} with {len(rows)} rows...")

    with open(csv_filename, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Question", "Link"])
        writer.writerows(rows)


def sanitize_filename(name):
    """
    Helper function to create a valid filename from a string.
    Removes or replaces invalid characters for Windows, Linux, etc.
    """
    # Remove or replace characters like /, \, :, ?, *, <, >, |, etc.
    return re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")


if __name__ == "__main__":
    # Adjust the path to your actual .md file
    md_file = "coding_questions.md"
    md_to_csv(md_file)
