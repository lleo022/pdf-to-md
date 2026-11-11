# PDF to TXT Converter

Converts PDF files to plain text using [pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/index.html). Output is formatted as Markdown and saved to the `converted/` folder in this project.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

```bash
git clone https://github.com/lleo022/pdf-to-md.git
cd pdf-to-md
```

**With uv:** no further setup. `uv run` installs dependencies (and Python 3.14 if needed) on first run.

**With pip:**

```bash
python3.14 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pymupdf4llm
```

## Usage

```bash
# Convert all PDFs in a directory
python convert.py /path/to/pdfs

# Convert specific files in a directory
python convert.py /path/to/pdfs file1.pdf file2.pdf

# Using uv (handles dependencies automatically)
uv run convert.py /path/to/pdfs
uv run convert.py /path/to/pdfs file1.pdf file2.pdf
```

Converted `.txt` files are saved to `converted/` in the project root, named after the original PDF (e.g. `report.pdf` → `converted/report.txt`).

## Examples

```bash
# Convert everything in ~/Documents/papers
uv run convert.py ~/Documents/papers

# Convert only two specific files
uv run convert.py ~/Documents/papers thesis.pdf appendix.pdf
```
