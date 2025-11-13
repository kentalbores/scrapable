# pip install pymupdf

import fitz  # PyMuPDF
from pathlib import Path

pdf_path = "pdfs/f7358c63-c2d4-43ed-a7d7-95eb1d13cb9d.pdf"
out_dir = Path("extracted_images")
out_dir.mkdir(exist_ok=True)

with fitz.open(pdf_path) as doc:
    img_count = 0
    for page_index, page in enumerate(doc, start=1):
        # get_images(full=True) lists embedded images used on the page
        for img in page.get_images(full=True):
            xref = img[0]  # XREF of the image object
            base = doc.extract_image(xref)
            img_bytes = base["image"]
            ext = base.get("ext", "png")  # usually 'png' or 'jpeg'
            img_count += 1
            (out_dir / f"p{page_index:03d}_img{img_count:04d}.{ext}").write_bytes(
                img_bytes
            )

print("Done.")