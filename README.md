# Krishna Kankipati — personal site

[Live portfolio](https://krishna2709.github.io/portfolio/) · [Full CV](https://krishna2709.github.io/portfolio/cv.html)

An architecture-dossier portfolio with a separate detailed work record, independent of Wix. Plain HTML and CSS; no build step or runtime dependencies. `index.html` contains four flagship system dossiers, `cv.html` holds the broader project inventory and detailed CV, and `work.html` redirects old project links to the flagship systems section.

## Preview locally

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000`.

## Publish on GitHub Pages

The site uses relative links and works at a project repository URL. GitHub Pages should deploy from the repository's default branch and root directory. The GoDaddy domain can be connected after review.

## Search visibility

The canonical site is `https://krishna2709.github.io/portfolio/`. The homepage and CV have distinct titles, descriptions, canonical URLs, and social sharing metadata. The homepage also identifies Krishna and his other public profiles with `ProfilePage` structured data. `sitemap.xml` lists the two pages intended for search results; `work.html` is only an old-link redirect.

To request Google indexing, add `https://krishna2709.github.io/portfolio/` as a **URL-prefix property** in [Google Search Console](https://search.google.com/search-console). Use Google's HTML meta tag on the homepage or place its verification file at the exact URL Search Console specifies, then complete verification. Submit `https://krishna2709.github.io/portfolio/sitemap.xml`, then inspect and request indexing for the homepage and `cv.html`. Search Console is also where Google reports crawl and indexing status. Crawling and inclusion are Google's decisions and can take time.

This is a GitHub Pages project site under `/portfolio/`; a `robots.txt` file here would not be the effective host-root robots file. The current `github.io` host returns no robots restrictions, and the pages do not send `noindex`. When the DATAOIL St. domain moves to this site, update the canonicals, sitemap, and Search Console property together.

## Content notes

The CV copy draws on Krishna's [public Notion profile](https://sharp-orbit-352.notion.site/Hi-there-I-am-Krishna-Kankipati-265320b3ca8d81618759cb94e03307bf), [LinkedIn](https://www.linkedin.com/in/krishnacse/), [GitHub](https://github.com/Krishna2709), the existing Wix page, and copy supplied directly by Krishna in September 2026. The current headshot was supplied directly by Krishna and exported for the web without embedded camera or location metadata.

The homepage case studies draw on the local `apex-7` project documentation and the separate local `108ai` code folder. The full record repeats the four flagship systems with matching status and architecture claims; Chronoscope is a research note on the homepage and an active exploration in the CV inventory. SpendRule is described at a public architectural level, without internal counts or customer financial data. Chronoscope is labeled an active exploration. SafeScreen's deepfake detector is framed as an uncertain secondary signal; its NPU port is not claimed as complete. ARIA's second-place award is identified only as a prize track because the specific track has not been independently confirmed. The public [PyTorch winners recap](https://pytorch.org/blog/building-the-future-of-on-device-ai-at-the-executorch-hackathon/) confirms SafeScreen's first place.

## Content map

| System | Homepage | Work record |
| --- | --- | --- |
| SpendRule | Full dossier; event-driven intake and evidence-backed validation | Experience plus flagship index entry |
| Casey / 108-AI | Full dossier; legal AI workflows and observability | Experience plus flagship index entry |
| SafeScreen AI | Full dossier; on-device privacy and bounded warnings | Award plus flagship index entry |
| ARIA | Full dossier; risk gates and paper trading | Award plus flagship index entry |
| Chronoscope | Evaluation field note; active exploration | Research index entry |
| Other projects | Linked from the full inventory | Broader research, interfaces, and infrastructure index |

Keep project status, award language, and technical limits aligned on both pages. ARIA's specific second-place prize track remains unnamed because the public team page does not identify it; that placement comes from Krishna. SafeScreen's application is described as on-device, while the NPU benchmarking work is not presented as a fully shipped app integration.

The SpendRule intake and observability copy is grounded in `contract-sphere/ARCHITECTURE.md`, `PIPELINE_FLOW.md`, the dropzone/archive handlers, and the tracing modules. The Casey / 108-AI copy is grounded in the contract-scoring LangGraph and Inngest workflow code, Agentic RAG flow, and copilot-agent documentation. It describes implemented architecture without claiming every prototype or agent is commercially deployed.
