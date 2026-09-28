# Krishna Kankipati — personal site

An architecture-dossier portfolio with a separate detailed work record, independent of Wix. Plain HTML and CSS; no build step or runtime dependencies. `index.html` contains three flagship system dossiers, `cv.html` holds the broader project inventory and detailed CV, and `work.html` redirects old project links to the flagship systems section.

## Preview locally

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Publish on GitHub Pages

The site uses relative links and works at a project repository URL. GitHub Pages should deploy from the repository's default branch and root directory. The GoDaddy domain can be connected after review.

## Content notes

The CV copy draws on Krishna's [public Notion profile](https://sharp-orbit-352.notion.site/Hi-there-I-am-Krishna-Kankipati-265320b3ca8d81618759cb94e03307bf), [LinkedIn](https://www.linkedin.com/in/krishnacse/), [GitHub](https://github.com/Krishna2709), the existing Wix page, and copy supplied directly by Krishna in September 2026. The current headshot was supplied directly by Krishna and exported for the web without embedded camera or location metadata.

The homepage case studies draw on the local `apex-7` project documentation. The full record repeats the three flagship systems with matching status and architecture claims; Chronoscope is a research note on the homepage and an active exploration in the CV inventory. SpendRule is described at a public architectural level, without internal counts or customer financial data. Chronoscope is labeled an active exploration. SafeScreen's deepfake detector is framed as an uncertain secondary signal; its NPU port is not claimed as complete. ARIA's second-place award is identified only as a prize track because the specific track has not been independently confirmed. The public [PyTorch winners recap](https://pytorch.org/blog/building-the-future-of-on-device-ai-at-the-executorch-hackathon/) confirms SafeScreen's first place.

## Content map

| System | Homepage | Work record |
| --- | --- | --- |
| SpendRule | Full dossier; production contract and invoice validation | Experience plus flagship index entry |
| SafeScreen AI | Full dossier; on-device privacy and bounded warnings | Award plus flagship index entry |
| ARIA | Full dossier; risk gates and paper trading | Award plus flagship index entry |
| Chronoscope | Evaluation field note; active exploration | Research index entry |
| Other projects | Linked from the full inventory | Broader research, interfaces, and infrastructure index |

Keep project status, award language, and technical limits aligned on both pages. ARIA's specific second-place prize track remains unnamed because the public team page does not identify it; that placement comes from Krishna. SafeScreen's application is described as on-device, while the NPU benchmarking work is not presented as a fully shipped app integration.
