# Krishna Kankipati — personal site

A narrative portfolio with a separate detailed CV, independent of Wix. Plain HTML and CSS; no build step or runtime dependencies. `index.html` is the homepage, `cv.html` is the detailed CV, and `work.html` redirects old project links to the selected work section.

## Preview locally

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Publish on GitHub Pages

The site uses relative links and works at a project repository URL. GitHub Pages should deploy from the repository's default branch and root directory. The GoDaddy domain can be connected after review.

## Content notes

The CV copy draws on Krishna's [public Notion profile](https://sharp-orbit-352.notion.site/Hi-there-I-am-Krishna-Kankipati-265320b3ca8d81618759cb94e03307bf), [LinkedIn](https://www.linkedin.com/in/krishnacse/), [GitHub](https://github.com/Krishna2709), the existing Wix page, and copy supplied directly by Krishna in September 2026.

The homepage case studies draw on the local `apex-7` project documentation. SpendRule is described at a public architectural level, without internal counts or customer financial data. Chronoscope is labeled an active exploration. SafeScreen's deepfake detector is framed as an uncertain secondary signal; its NPU port is not claimed as complete. ARIA's second-place award is identified only as a prize track because the specific track has not been independently confirmed. The public [PyTorch winners recap](https://pytorch.org/blog/building-the-future-of-on-device-ai-at-the-executorch-hackathon/) confirms SafeScreen's first place.
