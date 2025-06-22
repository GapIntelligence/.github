import subprocess
from pathlib import Path


def test_mkdocs_build(tmp_path: Path) -> None:
    """Ensure the mkdocs site builds successfully."""
    site_dir = tmp_path / "site"
    result = subprocess.run([
        "mkdocs",
        "build",
        "--site-dir",
        str(site_dir),
    ], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert site_dir.exists()
