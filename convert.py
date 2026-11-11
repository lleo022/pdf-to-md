# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pymupdf4llm>=1.27.2.3",
# ]
# ///
import pymupdf4llm
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "converted"


def convert_pdf(pdf_path: Path) -> bool:
    try:
        result = pymupdf4llm.to_markdown(str(pdf_path))
        md_text = result if isinstance(result, str) else "\n\n".join(
            chunk.get("text", "") for chunk in result
        )
        output_file = OUTPUT_DIR / (pdf_path.stem + ".txt")
        output_file.write_text(md_text, encoding="utf-8")
        print(f"Converted: {pdf_path.name} -> converted/{output_file.name}")
        return True
    except Exception as e:
        print(f"Error converting {pdf_path.name}: {e}", file=sys.stderr)
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert.py <directory> [file1.pdf file2.pdf ...]")
        sys.exit(1)

    source_dir = Path(sys.argv[1]).expanduser().resolve()

    if not source_dir.exists():
        print(f"Error: '{source_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    if not source_dir.is_dir():
        print(f"Error: '{source_dir}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)

    if len(sys.argv) > 2:
        pdf_files = []
        for name in sys.argv[2:]:
            p = source_dir / name
            if not p.exists():
                print(f"Warning: '{name}' not found in {source_dir}, skipping.", file=sys.stderr)
            elif p.suffix.lower() != ".pdf":
                print(f"Warning: '{name}' is not a PDF file, skipping.", file=sys.stderr)
            else:
                pdf_files.append(p)
    else:
        pdf_files = sorted(source_dir.glob("*.pdf"))
        if not pdf_files:
            print(f"No PDF files found in '{source_dir}'.")
            sys.exit(0)

    success = sum(convert_pdf(pdf) for pdf in pdf_files)
    print(f"\nDone: {success}/{len(pdf_files)} file(s) converted. Output in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
