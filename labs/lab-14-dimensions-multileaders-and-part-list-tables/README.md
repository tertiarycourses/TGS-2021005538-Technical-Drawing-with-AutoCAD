# Lab 14 — Dimensions, Multileaders and Part-List Tables

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 05:** Design Documentation

**Objective:** LO3/LO4 — dimension drawings and produce part lists (A5, K5)

## Goal

Fully dimension practice drawing EX-8 with a metric dimension style — linear, aligned, radial, diameter, angular, continue and baseline — add multileader callouts, and create the part-list table from the Lab 11 balloon attributes.

## You'll produce

A fully dimensioned EX-8 sheet with leader notes and a parts table (part no · description · qty).

**Commands / tools:** DIMSTYLE, DIM, DIMLINEAR/ALIGNED/RADIUS/DIAMETER/ANGULAR, DIMCONTINUE, DIMBASELINE, MLEADER, TABLE, DATAEXTRACTION

## Files in this lab

- `ex8.dwg` — AutoCAD drawing file
- `ex8-drawing-sheet.pdf` — drawing sheet / reference (PDF)
- `ex8.png` — reference image

## Step-by-step

1. Open ex8.dwg and create dimension style MECH-25 (ISO, 2.5mm text, closed-filled arrows)

   ```
   D (DIMSTYLE) → New → fit/text
   ```

2. Place linear and aligned dimensions on the main edges

   ```
   DLI · DAL
   ```

3. Dimension the circles and arcs with diameter, radius and angular dimensions

   ```
   DDI · DRA · DAN
   ```

4. Chain related dimensions with Continue, and datum-reference them with Baseline

   ```
   DCO · DBA
   ```

5. Add multileader callouts for the hole notes and edge finishes

   ```
   MLD → arrow point → landing → note
   ```

6. Insert a table for the part list and populate it from the Lab 11 attribute extraction

   ```
   TB (TABLE) · DATAEXTRACTION
   ```

7. Add a revision cloud around one detail to flag it for checking, then save

   ```
   REVCLOUD → drag around detail
   ```

## Check your work

Every dimension on the EX-8 sheet is reproduced with the MECH-25 style (no overridden text), leaders land neatly, and the table rows match the balloons one-for-one.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*