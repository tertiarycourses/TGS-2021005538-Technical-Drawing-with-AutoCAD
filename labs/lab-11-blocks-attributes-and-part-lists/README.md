# Lab 11 — Blocks, Attributes and Part Lists

**Course:** WSQ Technical Drawing with AutoCAD (TGS-2021005538) · **Topic 04:** Organizing Objects

**Objective:** LO3 — create part lists using AutoCAD (A4, K4)

## Goal

Inspect a reusable block library and a drawing containing dynamic blocks, then define a part-tag block with attributes and prepare its data for the part list.

## You'll produce

A BALLOON block with PART_NO / DESC / QTY attributes, plus evidence that one library block and one dynamic-block state can be inserted and edited correctly.

**Commands / tools:** BLOCK, WBLOCK, DesignCenter, ATTDEF, INSERT, ATTEDIT, dynamic-block grips, DATAEXTRACTION

## Files in this lab

- `title-block.dwg` — AutoCAD drawing file
- `architecture-library.dwg` — AutoCAD drawing file
- `new-office-dynamic-blocks.dwg` — AutoCAD drawing file

## Step-by-step

1. Open architecture-library.dwg in DesignCenter and insert one reusable symbol into a new drawing

   ```
   ADCENTER → Folders → architecture-library.dwg → Blocks → Insert
   ```

2. Open new-office-dynamic-blocks.dwg and change one dynamic block's grip or visibility state

   ```
   OPEN new-office-dynamic-blocks.dwg → select dynamic block → grip / Properties
   ```

3. Open title-block.dwg and draw the balloon symbol (circle + leader stub)

   ```
   C → radius 5
   ```

4. Define attributes PART_NO, DESC and QTY with prompts and default values

   ```
   ATTDEF → tag/prompt/default
   ```

5. Create the block BALLOON from the circle plus its attribute definitions

   ```
   B → name BALLOON → select objects
   ```

6. Insert the balloon against each component and fill in the attribute values

   ```
   I → BALLOON → answer prompts
   ```

7. Edit one balloon attribute, then preview the data extraction used by the Lab 14 part list

   ```
   ATTEDIT / EATTEDIT → DATAEXTRACTION
   ```

## Check your work

The library block inserts at the correct scale, the dynamic state changes without exploding, and Data Extraction lists one row per BALLOON with the values you entered.
