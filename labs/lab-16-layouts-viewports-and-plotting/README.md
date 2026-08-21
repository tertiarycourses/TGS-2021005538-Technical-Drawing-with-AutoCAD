# Lab 16 — Layouts, Viewports and Plotting

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO5 — produce drawings for submission to standards (A5, K5)

## Goal

Audit the supplied new-office-layout.dwg, then compose an A3 layout with a title block, locked scaled viewports and a standards-compliant PDF plot.

## You'll produce

A print-ready A3 office layout with two locked viewports, completed title information, verified lineweights and a plotted PDF.

**Commands / tools:** LAYOUT, PAGESETUP, MVIEW, viewport scale/lock, PLOT, DWG to PDF.pc3

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file
- `new-office-layout.dwg` — AutoCAD drawing file

## Step-by-step

1. Open new-office-layout.dwg, inspect its model/layout tabs and save a working copy

   ```
   OPEN new-office-layout.dwg → SAVEAS office-layout-mine.dwg
   ```

2. Rename the working layout A3-SHEET and set DWG To PDF.pc3, ISO A3 landscape, 1:1

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
