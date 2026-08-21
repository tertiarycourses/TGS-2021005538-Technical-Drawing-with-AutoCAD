# Lab 12 — External References and PDF Import

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO4 — assemble drawings from shared reference content (A4, K4)

## Goal

Repair and verify the relative Landscaping_REV1 Xref in the supplied office-layout host, then attach a title block and a PDF underlay and import vector geometry.

## You'll produce

A host drawing whose landscaping Xref resolves from the lab folder, with an additional live title-block Xref and an imported PDF geometry sample.

**Commands / tools:** XREF/ATTACH, External References palette, PDFATTACH, PDFIMPORT

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file
- `ex1-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `new-office-layout-with-xref.dwg` — AutoCAD drawing file
- `Landscaping_REV1.dwg` — AutoCAD drawing file

## Step-by-step

1. Keep new-office-layout-with-xref.dwg and Landscaping_REV1.dwg together, then open the host

   ```
   OPEN new-office-layout-with-xref.dwg
   ```

2. Open External References and confirm Landscaping_REV1 is Found using a relative path

   ```
   XR → Landscaping_REV1 → Saved Path: .\Landscaping_REV1.dwg
   ```

3. If unresolved, select a new path in the current lab folder, reload, and retain a relative path

   ```
   XR → Change Path → Select New Path → Reload
   ```

4. Attach title-block.dwg as an additional Xref at 0,0, scale 1

   ```
   XATTACH → title-block.dwg
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

Both Xrefs show Loaded, Landscaping_REV1 uses a relative path and survives reopening the folder elsewhere, while PDFIMPORT produces editable AutoCAD objects from the underlay.
