# Lab 16 — Layouts, Viewports and Plotting

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO5 — produce drawings for submission to standards (A5, K5)

## Goal

Compose an A3 layout: attach the title block, create scaled viewports (1:20 and a detail), lock them, and plot the sheet to PDF — the standard submission output.

## You'll produce

A print-ready A3 layout with title block, two locked scaled viewports and a plotted PDF.

**Commands / tools:** LAYOUT, PAGESETUP, MVIEW, viewport scale/lock, PLOT, DWG to PDF.pc3

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file

## Step-by-step

1. Open your annotated drawing, switch to a Layout tab and rename it A3-SHEET

   ```
   right-click tab → Rename
   ```

2. Set the page: DWG To PDF.pc3, ISO A3 (420×297), landscape, 1:1 plot scale

   ```
   PAGESETUP → Modify
   ```

3. Insert the title block on the layout at 0,0 in paper space

   ```
   I → title-block
   ```

4. Create a main viewport and set its scale to 1:20 exactly, then lock it

   ```
   MV → drag → select → scale 1:20 → lock
   ```

5. Add a second, smaller viewport for a detail at a larger scale

   ```
   MV → drag → scale 1:5
   ```

6. Plot the layout to PDF and check line weights in the output

   ```
   PLOT → DWG To PDF.pc3 → OK
   ```

## Check your work

Both viewports report their exact scales in the status bar and cannot be zoomed when locked, and the plotted PDF shows the complete titled sheet at A3.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*