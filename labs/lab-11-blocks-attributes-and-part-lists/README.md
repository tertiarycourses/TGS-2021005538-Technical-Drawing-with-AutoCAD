# Lab 11 — Blocks, Attributes and Part Lists

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO3 — create part lists using AutoCAD (A4, K4)

## Goal

Define a reusable part-tag block with attributes (part number, description, quantity) in the title-block drawing, insert it against each component, and prepare the attribute data that will feed the part list.

## You'll produce

A BALLOON block with PART_NO / DESC / QTY attributes, inserted and filled in for each part.

**Commands / tools:** BLOCK, ATTDEF, INSERT, ATTEDIT, groups, DATAEXTRACTION (preview)

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file
- `architecture-library.dwg` — AutoCAD drawing file
- `new-office-dynamic-blocks.dwg` — AutoCAD drawing file

## Step-by-step

1. Open title-block.dwg and draw the balloon symbol (circle + leader stub)

   ```
   C → radius 5
   ```

2. Define attributes PART_NO, DESC and QTY with prompts and default values

   ```
   ATTDEF → tag/prompt/default
   ```

3. Create the block BALLOON from the circle plus its attribute definitions

   ```
   B → name BALLOON → select objects
   ```

4. Insert the balloon against each component and fill in the attribute values

   ```
   I → BALLOON → answer prompts
   ```

5. Double-click a balloon to edit its attributes; group related parts together

   ```
   ATTEDIT / EATTEDIT · GROUP
   ```

6. Preview extracting the attribute data — this becomes the part list in Lab 14

   ```
   DATAEXTRACTION
   ```

## Check your work

Each inserted balloon prompts for and displays its own part number, description and quantity, and Data Extraction lists one row per balloon with the values you entered.

---
*© 2026 Tertiary Infotech Academy Pte Ltd (UEN: 201200696W) · WSQ Technical Drawing with AutoCAD · TGS-2021005538*