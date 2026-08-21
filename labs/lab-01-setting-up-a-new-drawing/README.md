# Lab 1 — Setting Up a New Drawing

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 01:** Getting Started with AutoCAD

**Objective:** LO1 — read and visualize AutoCAD technical drawings; set up a drawing environment (A1, K1)

## Goal

Create and verify a metric drawing environment, compare saved workspace and drafting-setting examples, then open a finished drawing and practise reading it with zoom, pan and ViewCube.

## You'll produce

A correctly configured metric drawing saved as DWG, a settings audit, and confident navigation of an existing technical drawing.

**Commands / tools:** ACADISO template, UNITS, LIMITS, DSETTINGS, WSCURRENT, ZOOM, PAN, ViewCube

## Files in this lab

- `lab01-table.dwg` — AutoCAD drawing file
- `reading-practice.dwg` — AutoCAD drawing file
- `workspaces.dwg` — AutoCAD drawing file
- `drafting-settings.dwg` — AutoCAD drawing file

## Step-by-step

1. Start AutoCAD and create a new drawing from the ISO metric template

   ```
   NEW → acadiso.dwt
   ```

2. Open workspaces.dwg, compare the available workspaces, then switch to Drafting & Annotation

   ```
   OPEN workspaces.dwg → WSCURRENT → Drafting & Annotation
   ```

3. Set decimal millimetres with 0.00 precision and decimal degrees for angles

   ```
   UNITS → Insertion scale: Millimetres → Length: Decimal, 0.00
   ```

4. Frame an A3-sized working area with drawing limits, then zoom to it

   ```
   LIMITS → 0,0 → 420,297  |  ZOOM → All
   ```

5. Open drafting-settings.dwg and audit grid, snap, ortho, polar and object-snap settings

   ```
   OPEN drafting-settings.dwg → DSETTINGS · F7 · F9 · F8 · F10 · F3
   ```

6. Open lab01-table.dwg and navigate it: wheel-zoom, pan, zoom window and zoom extents

   ```
   OPEN lab01-table.dwg → Z → W / Z → E
   ```

7. Identify the views, dimensions and title information in the drawing, then save your setup file

   ```
   SAVEAS → lab01-setup.dwg
   ```

## Check your work

INSUNITS reports millimetres, limits are 420 × 297, Drafting & Annotation is current, the precision-aid audit is complete, and lab01-setup.dwg reopens with the settings intact.
