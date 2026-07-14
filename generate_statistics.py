import json
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "statistics_data.json"
OUTPUT_FILE = ROOT / "Statistics.html"


def load_entries():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError:
        return []


def build_html(entries):
    rows = ""
    for entry in entries:
        rows += f"""
        <tr>
            <td>{escape(entry['source'])}</td>
            <td>{escape(entry['metric'])}</td>
            <td>{escape(str(entry['value']))}</td>
            <td>{escape(entry.get('notes', ''))}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Statistics</title>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body class=\"home-page\">
    <div class=\"detailed-header\">
        <h1>Statistics Overview</h1>
    </div>

    <nav class=\"section-nav\">
        <ul class=\"section-nav-links\">
            <li><a href=\"Home.html\">Home</a></li>
            <li><a href=\"EvergreenStudios.html\">Where Winds Meet</a></li>
            <li><a href=\"Sega.html\">Sega Sonic</a></li>
            <li><a href=\"Information.html\">About Us</a></li>
        </ul>
    </nav>

    <main class=\"stats-panel\">
        <h2>Collected data</h2>
        <div class=\"chart-card\">
            <table>
                <thead>
                    <tr>
                        <th>Source</th>
                        <th>Metric</th>
                        <th>Value</th>
                        <th>Notes</th>
                    </tr>
                </thead>
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    </main>
</body>
</html>
"""


def main():
    entries = load_entries()
    OUTPUT_FILE.write_text(build_html(entries), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
