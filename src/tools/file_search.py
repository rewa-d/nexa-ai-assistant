from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def search_files(filename: str) -> str:
    """
    Search for files by name inside the NEXA project.
    This tool is read-only.
    """

    if not filename or not filename.strip():
        return "Please provide a filename to search for."

    matches = []

    for path in PROJECT_ROOT.rglob("*"):
        if any(
            part.startswith(".")
            for part in path.relative_to(PROJECT_ROOT).parts
        ):
            continue

        if path.is_file() and filename.lower() in path.name.lower():
            matches.append(str(path.relative_to(PROJECT_ROOT)))

        if len(matches) >= 20:
            break

    if not matches:
        return f"No files found matching '{filename}'."

    return "Matching files:\n" + "\n".join(matches)
