# HPV and Cervical Cancer Prevention Website

Created by Haley for HPE 4010 (Disease Prevention in Public Health), University of Cincinnati.
For education only, not medical advice.

## What's in this folder

| Path | What it is |
| --- | --- |
| `index.html` … `references.html` | **The deployable website.** Seven plain HTML pages with no build step and no server code. |
| `source/generator/` | Python scripts that generate every page. `common.py` holds the shared colors, icons, nav, and footer. Each other script builds one page. |
| `source/canvas/` | The same pages in Claude Design canvas format (`.dc.html` + `canvas.json`). These only run inside the Claude Design editor, **not** on a normal web host. |

Pages: `index.html` (Home), `numbers.html`, `risk-factors.html`, `prevention.html`, `resources.html`, `quiz.html`, `references.html`.

## Deploying

Upload the seven `.html` files at the top of this folder to any static host. You don't need to upload the `source/` folder. Some options:

- **GitHub Pages:** push this folder to a repository, then go to Settings → Pages → Deploy from branch (root).
- **Netlify Drop:** drag this folder onto https://app.netlify.com/drop.
- **Locally:** double-click `index.html` to open it in a browser.

The pages load the Figtree font from Google Fonts. All other styles and the quiz script are inside each HTML file.

## Editing and rebuilding

Edit the text in `source/generator/*.py`, then run this from `source/generator/` (Python 3, no extra packages needed):

```
python build.py          # rebuilds the 7 HTML pages in this folder
python build.py canvas   # rebuilds the Claude Design canvas files in source/canvas/
```

Note: rebuilding overwrites the HTML pages, so edit the generator scripts, not the HTML files themselves.
