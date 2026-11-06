# Changelog

## [1.1.0] — Hardening

- Persist the selected language in `localStorage` and synchronize it with compatible embedded apps.
- Add a loading spinner and stale-load protection while embedded apps are decoded.
- Gzip-compress the embedded apps and decompress them asynchronously in the browser.
- Show localized fallback messages when the overview video or presentation PDFs are unavailable.
- Add a name-freeze check and embedded-app size reporting to continuous integration.
