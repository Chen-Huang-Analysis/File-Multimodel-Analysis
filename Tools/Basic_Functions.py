import os
import json
def list_pdfs_in_folder(path):
    if not os.path.isdir(path):
        raise ValueError(f"this path is not a folder: {path}")

    pdf_paths = {}
    for name in os.listdir(path):
        full = os.path.join(path, name)

        if not os.path.isfile(full):
            raise ValueError(f"this is not a file: {full}")

        if not name.lower().endswith('.pdf'):
            raise ValueError(f"some file is not pdf: {full}")
        pdf_paths[name] = full

    return pdf_paths

def save_dict_to_json(data: dict, filepath: str, *, indent: int = 4, ensure_ascii: bool = False) -> None:
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=ensure_ascii)