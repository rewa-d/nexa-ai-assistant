
import subprocess


ALLOWED_APPS = {
    "calculator": "Calculator",
    "calendar": "Calendar",
    "notes": "Notes",
    "safari": "Safari",
    "finder": "Finder",
    "textedit": "TextEdit",
}


def open_application(app_name: str) -> str:
    """Open an approved macOS application."""

    if not isinstance(app_name, str):
        return "Application name must be text."

    app_key = app_name.strip().lower()

    if app_key not in ALLOWED_APPS:
        return (
            f"Application '{app_name}' is not approved. "
            f"Available applications: {', '.join(ALLOWED_APPS)}"
        )

    application = ALLOWED_APPS[app_key]

    try:
        subprocess.run(
            ["open", "-a", application],
            check=True,
            capture_output=True,
            text=True,
            timeout=10
        )
    except (subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
            OSError) as error:
        return f"Unable to open {application}: {error}"

    return f"Successfully opened {application}."
