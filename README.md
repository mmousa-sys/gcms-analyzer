## 🛠️ Development

Compress the embedded apps with Node.js:

```sh
node tools/compress-apps.mjs Lab_Technician_Suite_Offline.html
```

The top-bar language selector sends `{ type: "uals:setLang", lang }` to the active embedded app with `postMessage`. Apps may also expose `setLang(lang)` or `setLanguage(lang)`, or provide a `#langSelect` control for the suite to update.

The 3D guide supports Arabic and English; selecting German uses its English interface. HPLC retains its existing language behavior.
