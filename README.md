# Catonlee

An independent English language editorial site about home appliances and everyday technology. The source is static Python-generated HTML, ready for Cloudflare Pages.

## Build

Run `python3 build.py` to generate the `dist/` directory. Run `python3 -m http.server 8000 --directory dist` to preview locally.

## Publishing

The production site at `catonlee.com` is connected to the `main` branch of `haungzl/auto_aff` through Cloudflare Pages project `catonlee`. Cloudflare runs `python3 build.py` from the repository root and publishes `dist/`. Build watch paths include all files (`*`). To update the site, edit the source files and push a commit to `main`; Cloudflare will build and deploy that commit automatically. Check the Pages deployment status before treating the update as live. The repository, not the generated `dist/` folder, is the source of truth.

The 50 stories are planned in `articles.py`; photos and licenses are recorded in `image_credits.json`. Brand links are centralized in `build.py`, with sourcing notes for the ten newer guides in `new_guides.py`. Tracking IDs have not been supplied, so these are ordinary merchant links, not tracked affiliate links.

Policy text should be reviewed before commercial launch. Contact email delivery must be configured for `hello@catonlee.com` if reader messages are expected.
