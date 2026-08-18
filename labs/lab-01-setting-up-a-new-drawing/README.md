# Lab 1 — Setting Up a New Drawing

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 01:** Getting Started with AutoCAD

**Objective:** LO1 — read and visualize AutoCAD technical drawings; set up a drawing environment (A1, K1)

## Goal

Create a new metric drawing from the ACADISO template, choose the Drafting & Annotation workspace, set units and limits, then open a finished drawing and practise reading it with the zoom, pan and ViewCube navigation tools.

## You'll produce

A correctly configured metric drawing (units, limits, workspace) saved as DWG, plus confident navigation of an existing technical drawing.

**Commands / tools:** ACADISO template, UNITS, LIMITS, ZOOM, PAN, ViewCube

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

2. Switch the workspace to Drafting & Annotation from the status bar gear icon

   ```
   WSCURRENT → Drafting & Annotation
   ```

3. Set decimal length units with 0.00 precision and decimal degrees for angles

   ```
   UNITS → Length: Decimal, Precision 0.00
   ```

4. Frame an A3-sized working area with drawing limits, then zoom to it

   ```
   LIMITS → 0,0 → 420,297  |  ZOOM → All
   ```

5. Toggle the precision aids on the status bar: grid, snap, ortho, polar and object snap

   ```
   F7 grid · F9 snap · F8 ortho · F10 polar · F3 osnap
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

You can state the drawing's units, limits and workspace; zoom to any detail of lab01-table.dwg and back to extents; and your lab01-setup.dwg opens with the settings intact.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*