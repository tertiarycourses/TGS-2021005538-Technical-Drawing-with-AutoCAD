# Lab 12 — External References and PDF Import

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO4 — assemble drawings from shared reference content (A4, K4)

## Goal

Attach the title-block drawing as an external reference under the table drawing, observe how xref updates flow through, then attach a PDF as an underlay and import PDF geometry.

## You'll produce

A host drawing with a live xref title block and a PDF underlay ready for tracing.

**Commands / tools:** XREF/ATTACH, External References palette, PDFATTACH, PDFIMPORT

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file
- `ex1-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `new-office-layout-with-xref.dwg` — AutoCAD drawing file

## Step-by-step

1. Open your layered table drawing from Lab 9 as the host drawing

   ```
   OPEN table-layers.dwg
   ```

2. Attach title-block.dwg as an Xref at 0,0, scale 1

   ```
   XATTACH → title-block.dwg
   ```

3. Open the External References palette and note the xref's status and path

   ```
   XR (External References)
   ```

4. Edit the title block in its own file, save, and reload the xref in the host

   ```
   XR → right-click → Reload
   ```

5. Attach the supplied drawing-sheet PDF as an underlay and snap to its geometry

   ```
   PDFATTACH → ex1-drawing-sheet.pdf
   ```

6. Import the PDF's vector geometry into the drawing and inspect the created objects

   ```
   PDFIMPORT → select underlay area
   ```

## Check your work

Changing the title block file and reloading updates the host without copying geometry, and PDFIMPORT produces editable AutoCAD objects from the underlay.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*