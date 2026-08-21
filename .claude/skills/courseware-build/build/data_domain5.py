"""Topic 5 — Design Documentation (A5, K5): hands-on activities."""

DOMAIN5 = [
    dict(
        num=13, topic=5,
        title="Text and Text Styles",
        objective="LO4 — create AutoCAD design documentation (A5, K5)",
        desc="Annotate the layered table drawing with single-line and multiline text, create and apply "
             "text styles for titles and notes, and fill in the title-block fields.",
        build="An annotated drawing with consistent TITLE and NOTES text styles and a completed title block.",
        services="TEXT, MTEXT, STYLE, annotative text, SPELL",
        dwg="lab-table-lesson2.dwg",
        steps=[
            ("Open your table drawing and create text styles TITLE (Arial, 5mm) and NOTES (Arial, 2.5mm)", "ST → New → font/height"),
            ("Add the drawing title with single-line text on the A-TEXT layer", "DT → start point → height → rotation"),
            ("Add a general-notes paragraph with multiline text in a bounding box", "T (MTEXT) → pick corners"),
            ("Set the NOTES style current and re-style existing text via the Properties palette", "PR → Style → NOTES"),
            ("Fill in the title-block fields: title, drawn-by, date, scale, sheet number", "double-click text → edit"),
            ("Spell-check the drawing and save", "SPELL → SAVE"),
        ],
        test="All annotation uses your named styles (none on Standard), the title block is complete, "
             "and changing the NOTES style font updates every note at once.",
    ),
    dict(
        num=14, topic=5,
        title="Dimensions, Multileaders and Part-List Tables",
        objective="LO3/LO4 — dimension drawings and produce part lists (A5, K5)",
        desc="Fully dimension practice drawing EX-8 with a metric dimension style — linear, aligned, "
             "radial, diameter, angular, continue and baseline — add multileader callouts, and create "
             "the part-list table from the Lab 11 balloon attributes.",
        build="A fully dimensioned EX-8 sheet with leader notes and a parts table (part no · description · qty).",
        services="DIMSTYLE, DIM, DLI/DAL/DRA/DDI/DAN, DCO/DBA, MLEADER, TABLE, DATAEXTRACTION",
        dwg="ex8.dwg",
        img="ex8.png",
        steps=[
            ("Open ex8.dwg and create dimension style MECH-25 (ISO, 2.5mm text, closed-filled arrows)", "D (DIMSTYLE) → New → fit/text"),
            ("Place linear and aligned dimensions on the main edges", "DLI · DAL"),
            ("Dimension the circles and arcs with diameter, radius and angular dimensions", "DDI · DRA · DAN"),
            ("Chain related dimensions with Continue, and datum-reference them with Baseline", "DCO · DBA"),
            ("Add multileader callouts for the hole notes and edge finishes", "MLD → arrow point → landing → note"),
            ("Insert a table for the part list and populate it from the Lab 11 attribute extraction", "TB (TABLE) · DATAEXTRACTION"),
            ("Add a revision cloud around one detail to flag it for checking, then save", "REVCLOUD → drag around detail"),
        ],
        test="Every dimension on the EX-8 sheet is reproduced with the MECH-25 style (no overridden "
             "text), leaders land neatly, and the table rows match the balloons one-for-one.",
    ),
    dict(
        num=15, topic=5,
        title="Hatching and Detail Finishing",
        objective="LO5 — produce design specification using AutoCAD (A5, K5)",
        desc="Apply section hatching with controlled boundaries and islands, then compare two supplied "
             "landscaping revisions and mark the changed area with a revision cloud and note.",
        build="A correctly hatched section view plus a documented landscaping revision showing the "
              "changed geometry, revision cloud and concise change note.",
        services="HATCH, gradient fills, boundary/island detection, HATCHEDIT, DWG Compare, REVCLOUD, MLEADER",
        dwg="ex3.dwg",
        steps=[
            ("Open a drawing with closed profiles (reuse ex3-mine.dwg) and identify the cut areas", ""),
            ("Hatch the main section area with ANSI31 at a scale that reads clearly", "H → Pattern ANSI31 → pick point"),
            ("Set different angles for adjacent parts so the section reads unambiguously", "H → Angle 90 → pick point"),
            ("Control islands: hatch around text and holes using island detection", "H → Settings → Island detection"),
            ("Apply a two-colour gradient fill to the elevation face for presentation", "GRADIENT → colours → pick area"),
            ("Edit an existing hatch's pattern and scale, then save", "HATCHEDIT → new scale"),
            ("Compare landscaping-rev1.dwg with landscaping-rev2.dwg and isolate the changed geometry", "COMPARE → landscaping-rev2.dwg"),
            ("Cloud the change and add a concise multileader note before saving the review copy", "REVCLOUD → MLEADER → SAVEAS landscaping-review.dwg"),
        ],
        test="Hatches do not bleed, adjacent parts use distinct angles, islands remain clear, and the "
             "landscaping review identifies every revision with one cloud and one readable note.",
    ),
    dict(
        num=16, topic=5,
        title="Layouts, Viewports and Plotting",
        objective="LO5 — produce drawings for submission to standards (A5, K5)",
        desc="Audit the supplied new-office-layout.dwg, then compose an A3 layout with a title block, "
             "locked scaled viewports and a standards-compliant PDF plot.",
        build="A print-ready A3 office layout with two locked viewports, completed title information, "
              "verified lineweights and a plotted PDF.",
        services="LAYOUT, PAGESETUP, MVIEW, viewport scale/lock, PLOT, DWG to PDF.pc3",
        dwg="title-block.dwg",
        steps=[
            ("Open new-office-layout.dwg, inspect its model/layout tabs and save a working copy", "OPEN new-office-layout.dwg → SAVEAS office-layout-mine.dwg"),
            ("Rename the working layout A3-SHEET and set DWG To PDF.pc3, ISO A3 landscape, 1:1", "PAGESETUP → Modify"),
            ("Insert the title block on the layout at 0,0 in paper space", "I → title-block"),
            ("Create a main viewport and set its scale to 1:20 exactly, then lock it", "MV → drag → select → scale 1:20 → lock"),
            ("Add a second, smaller viewport for a detail at a larger scale", "MV → drag → scale 1:5"),
            ("Plot the layout to PDF and check line weights in the output", "PLOT → DWG To PDF.pc3 → OK"),
        ],
        test="Both viewports report their exact scales in the status bar and cannot be zoomed when "
             "locked, and the plotted PDF shows the complete titled sheet at A3.",
    ),
]
