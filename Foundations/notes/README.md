# PDF Handwriting to Markdown Converter

A hybrid tool that uses Docker and Claude Code's vision capabilities to convert handwritten notes from PDFs into markdown for Obsidian.

## Prerequisites

- Docker Desktop installed
- Claude Code (you're already using it!)

## How It Works

1. **Extract**: Docker container extracts PDF pages as high-resolution images
2. **Analyze**: You ask Claude Code to read and analyze each image
3. **Convert**: Claude generates clean markdown from the handwriting
4. **Save**: Output saved to your Obsidian vault

## Quick Start

### 1. Build the Docker Image

From this directory, build the container:

```bash
docker-compose build
```

### 2. Extract PDF Pages

Place your PDF in this directory (or use an absolute path), then run:

```bash
# Extract pages from a PDF
docker-compose run --rm pdf-extractor python pdf_to_markdown.py your_notes.pdf
```

This creates a folder like `your_notes_pages/` with PNG images of each page.

### 3. Ask Claude to Analyze

In Claude Code, tell me:

```
Analyze the handwritten notes in /Users/jsturgi/Documents/Work/repositories/pdf to markdown/your_notes_pages/
and convert them to markdown. Save to ~/Documents/ObsidianVault/Notes/your_notes.md
```

I'll:
- Read each page image using vision
- Extract and interpret the handwriting
- Preserve structure (headings, lists, bullet points)
- Generate clean markdown
- Save to your Obsidian vault

## Detailed Usage

### Basic Extraction

```bash
# PDF in current directory
docker-compose run --rm pdf-extractor python pdf_to_markdown.py lecture_notes.pdf

# PDF from another location (use absolute path or relative to mounted volume)
docker-compose run --rm pdf-extractor python pdf_to_markdown.py /workspace/Downloads/notes.pdf
```

### Custom Output Directory

```bash
docker-compose run --rm pdf-extractor python pdf_to_markdown.py notes.pdf custom_output_folder
```

### Processing Workflow Example

```bash
# 1. Extract pages
docker-compose run --rm pdf-extractor python pdf_to_markdown.py meeting_notes.pdf

# 2. In Claude Code, say:
"Convert the handwritten notes in /Users/jsturgi/Documents/Work/repositories/pdf to markdown/meeting_notes_pages/
to markdown and save to ~/Documents/ObsidianVault/Work/meeting_notes.md"
```

## What Claude Can Do

When analyzing handwritten notes, I can:

- **Extract text** with high accuracy
- **Preserve structure**: headings, bullet points, numbered lists
- **Interpret formatting**: underlines, emphasis, crossed-out text
- **Handle mixed content**: text, diagrams, equations
- **Describe diagrams**: If a diagram can't be converted to text, I'll describe it
- **Clean up**: Remove artifacts, standardize formatting for Obsidian

## Tips for Best Results

- **Scan quality**: Higher DPI = better recognition (script uses 300 DPI)
- **Clear handwriting**: Works best with legible writing
- **Good lighting**: Ensure scans have good contrast
- **Multiple pages**: I can process entire notebooks, just give me the folder
- **Feedback**: If results aren't great, you can ask me to re-analyze specific pages differently

## Advanced: Batch Processing

To process multiple PDFs:

```bash
# Extract all PDFs
for pdf in *.pdf; do
  docker-compose run --rm pdf-extractor python pdf_to_markdown.py "$pdf"
done

# Then ask Claude to process all the extracted folders
```

## File Structure

```
repositories/pdf to markdown/
├── Dockerfile              # Container definition
├── docker-compose.yml      # Easy Docker commands
├── pdf_to_markdown.py      # Extraction script
├── extract.sh             # Wrapper script for easy extraction
├── .gitignore             # Git ignore file
├── README.md              # This file
├── your_notes.pdf         # Your PDF (example)
└── your_notes_pages/      # Extracted images (auto-created)
    ├── page_001.png
    ├── page_002.png
    └── ...
```

## Troubleshooting

**Docker build fails:**
- Ensure Docker Desktop is running
- Try: `docker-compose build --no-cache`

**Can't find PDF:**
- Use absolute paths or place PDF in this project directory
- Check volume mounting in docker-compose.yml

**Claude can't read images:**
- Verify images were created in the output folder
- Use absolute paths when telling Claude the folder location
- Make sure images are .png format

**Low accuracy:**
- Try rescanning at higher resolution
- Ensure good contrast in original scan
- Ask me to focus on specific sections

## Notes

- No API key needed - uses Claude Code's built-in vision
- All processing is private - images stay on your machine
- Container is lightweight and includes only necessary dependencies
- Works with any PDF containing handwritten content
