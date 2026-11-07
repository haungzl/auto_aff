# Catonlee

An independent English language editorial site about home appliances and everyday technology. The source is static Python-generated HTML, ready for Cloudflare Pages.

## Build

Run `python3 build.py`. Deploy the `dist/` directory. Run `python3 -m http.server 8000 --directory dist` to preview locally.

The 50 stories are planned in `articles.py`; photos and licenses are recorded in `image_credits.json`. Brand links are centralized in `build.py`, with sourcing notes for the ten newer guides in `new_guides.py`. Tracking IDs have not been supplied, so these are ordinary merchant links, not tracked affiliate links.

Policy text should be reviewed before commercial launch. Contact email delivery must be configured for `hello@catonlee.com` if reader messages are expected.
