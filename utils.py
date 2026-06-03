from pypdf import PdfReader
from pathlib import Path
from datetime import datetime


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from an uploaded PDF file."""
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"
        return text.strip()
    except Exception as exc:
        raise RuntimeError(f"Could not read PDF file: {exc}")


def save_report(report_text: str) -> str:
    """Save report to outputs folder and return file path."""
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = output_dir / f"career_report_{timestamp}.md"
    file_path.write_text(report_text, encoding="utf-8")
    return str(file_path)


def load_sample_file(path: str) -> str:
    file_path = Path(path)
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return ""
