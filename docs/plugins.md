# Right Panel plugins

Plugins are local `.rpp` (ZIP) packages installed from **Settings → Plugins**. They are unpacked into the platform data directory under `plugins/<id>` and can be enabled, disabled, reordered with built-in tools, reloaded, or uninstalled. A malformed package is rejected without stopping Right Panel.

Each package has `manifest.json` and an HTML `entry`. Manifest and API version 1 are supported. IDs match `[a-z0-9][a-z0-9._-]*`; paths must be local relative paths with no traversal. Package files are limited and Zip Slip paths are rejected.

See [plugin-manifest.md](plugin-manifest.md), [plugin-api.md](plugin-api.md), and [plugin-security.md](plugin-security.md). Build examples with `python scripts/package-plugins.py`.
