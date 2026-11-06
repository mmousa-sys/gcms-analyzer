import { readFileSync, statSync, writeFileSync } from "node:fs";
import { gzipSync } from "node:zlib";

const file = process.argv[2];

if (!file) {
  throw new Error("Usage: node tools/compress-apps.mjs <html-file>");
}

const beforeBytes = statSync(file).size;
const html = readFileSync(file, "utf8");
let payloadCount = 0;

const compressedHtml = html.replace(
  /(lab|gcms|hplc|gcms3d):\s*"([A-Za-z0-9_+/=]+)"/g,
  (match, moduleName, payload) => {
    payloadCount += 1;
    if (payload.startsWith("gz_")) return match;
    const compressed = gzipSync(Buffer.from(payload, "base64"), { level: 9 }).toString("base64");
    return `${moduleName}: "gz_${compressed}"`;
  }
);

if (payloadCount !== 4) {
  throw new Error(`Expected four embedded app payloads; found ${payloadCount}.`);
}

writeFileSync(file, compressedHtml);
const afterBytes = statSync(file).size;
console.log(`Before: ${beforeBytes} bytes`);
console.log(`After:  ${afterBytes} bytes`);
console.log(`Reduced: ${((1 - afterBytes / beforeBytes) * 100).toFixed(1)}%`);
