# Lab 13 — Text and Text Styles

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO4 — create AutoCAD design documentation (A5, K5)

## Goal

Annotate the layered table drawing with single-line and multiline text, create and apply text styles for titles and notes, and fill in the title-block fields.

## You'll produce

An annotated drawing with consistent TITLE and NOTES text styles and a completed title block.

**Commands / tools:** TEXT, MTEXT, STYLE, annotative text, SPELL

## Files in this lab

- `lab-table-lesson2.dwg` — AutoCAD drawing file
- `title-block.dwg` — AutoCAD drawing file

## Step-by-step

1. Open your table drawing and create text styles TITLE (Arial, 5mm) and NOTES (Arial, 2.5mm)

   ```
   ST → New → font/height
   ```

2. Add the drawing title with single-line text on the A-TEXT layer

   ```
   DT → start point → height → rotation
   ```

3. Add a general-notes paragraph with multiline text in a bounding box

   ```
   T (MTEXT) → pick corners
   ```

4. Set the NOTES style current and re-style existing text via the Properties palette

   ```
   PR → Style → NOTES
   ```

5. Fill in the title-block fields: title, drawn-by, date, scale, sheet number

   ```
   double-click text → edit
   ```

6. Spell-check the drawing and save

   ```
   SPELL → SAVE
   ```

## Check your work

All annotation uses your named styles (none on Standard), the title block is complete, and changing the NOTES style font updates every note at once.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*