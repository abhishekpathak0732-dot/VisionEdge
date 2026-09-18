import json
from pathlib import Path

def save_report(report, output_dir):
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    report_path = output / "analysis_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report_path
