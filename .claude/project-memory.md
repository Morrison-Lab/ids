# Project memory

Facts about working on this project that a new session would otherwise have to ask Ezra again.

## Textbook PDFs

- The textbook PDFs the course draws on (MacKay's *Information Theory, Inference, and Learning Algorithms*, Cover and Thomas, Yeung) live in the lab's `mlr` repo, in `books/`.
- Cloud sessions can't download ITILA from inference.org.uk (the proxy returns 403), so read the copy in `mlr` instead.
  In a Claude project thread linked to Ezra's computer, it is at `~/Documents/GitHub/mlr/books/` on device cf463-02; stage it with the device folder tools.
- Copy books from `mlr` into the project Library (`/mnt/project-files/books/`) as needed, and check there before staging a book again.
  ITILA was copied there on 2026-11-09.
- The ITILA PDF's page numbers match the printed book (exercise 8.11 is on p. 142), and `pdftotext -layout` extracts it cleanly.
