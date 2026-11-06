"""Build the HPV and Cervical Cancer Prevention website.

Usage (from this folder):
    python build.py            # writes the deployable site to ../../ (the project root)
    python build.py canvas     # writes Design canvas files to ../canvas/
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = ["home", "numbers", "risk", "prevention", "resources", "quiz", "references"]
mode = sys.argv[1] if len(sys.argv) > 1 else "static"
out = os.path.abspath(os.path.join(HERE, "..", "..") if mode == "static" else os.path.join(HERE, "..", "canvas"))
env = dict(os.environ, HPV_MODE=mode, HPV_OUT=out)
for p in PAGES:
    subprocess.run([sys.executable, os.path.join(HERE, p + ".py")], check=True, env=env, cwd=HERE)
print(f"Built {mode} site in {out}")
