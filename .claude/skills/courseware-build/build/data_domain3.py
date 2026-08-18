"""Topic 3 — Modifying Objects (A3, K3): hands-on activities."""

DOMAIN3 = [
    dict(
        num=6, topic=3,
        title="Move, Copy, Rotate and Offset",
        objective="LO2/LO3 — modify 2D drawings efficiently to build up a design (A3, K3)",
        desc="Build practice drawing EX-4 by drawing one feature and then positioning the rest with "
             "MOVE, COPY (multiple), ROTATE with reference angle and OFFSET for the parallel profiles.",
        build="The completed EX-4 drawing produced with modify commands rather than re-drawing each feature.",
        services="MOVE, COPY (Multiple/Array), ROTATE (Reference), OFFSET",
        dwg="ex4.dwg",
        img="ex4.png",
        steps=[
            ("Open the EX-4 sheet (ex4-drawing-sheet.pdf) and spot the repeated features", ""),
            ("Draw the base profile, then offset it to create the parallel inner/outer edges", "O → distance → pick side"),
            ("Draw one hole feature and copy it to every dimensioned centre", "CO → base point → second points"),
            ("Move a mis-placed feature precisely from its centre to the correct intersection", "M → base → destination"),
            ("Rotate the angled feature about its base point, using Reference to match the sheet angle", "RO → base → R → ref angle → new angle"),
            ("Check against ex4.dwg and save your version", "SAVEAS ex4-mine.dwg"),
        ],
        test="Feature spacings measure correct with DIST, offsets are at the specified distances, and "
             "the rotated feature sits at exactly the sheet's angle.",
    ),
    dict(
        num=7, topic=3,
        title="Trim, Extend, Fillet and Chamfer",
        objective="LO2/LO3 — clean up and finish drawing geometry (A3, K3)",
        desc="Complete practice drawing EX-5 by trimming overlapping construction geometry, extending "
             "short edges to their boundaries, and finishing corners with fillets and chamfers.",
        build="A clean EX-5 profile with every corner finished exactly as dimensioned on the sheet.",
        services="TRIM (Quick/Standard), EXTEND, FILLET, CHAMFER, BREAK",
        dwg="ex5.dwg",
        img="ex5.png",
        steps=[
            ("Open the EX-5 sheet (ex5-drawing-sheet.pdf) and rough out the profile with overlapping lines", ""),
            ("Trim the overshoots in Quick mode — click or drag across the pieces to remove", "TR → click segments"),
            ("Use Standard mode where you need explicit cutting edges: select boundaries, then objects", "TR → Enter (all edges) → pick"),
            ("Extend the short edges to meet their boundary lines", "EX → pick edges to extend"),
            ("Fillet the rounded corners at the sheet radius, and chamfer the bevelled ones", "F → R → 10 → pick 2 lines  ·  CHA → D → 5,5"),
            ("Compare with ex5.dwg and save", "SAVEAS ex5-mine.dwg"),
        ],
        test="No overshooting or dangling segments remain (zoom around the whole profile), and every "
             "fillet radius / chamfer distance matches the drawing sheet.",
    ),
    dict(
        num=8, topic=3,
        title="Mirror, Stretch, Scale and Arrays",
        objective="LO2/LO3 — reproduce patterned and symmetric geometry (A3, K3)",
        desc="Produce practice drawing EX-6 by drawing half of the symmetric design and mirroring it, "
             "then distributing the hole pattern with rectangular and polar arrays, and adjusting sizes "
             "with STRETCH and SCALE.",
        build="The completed EX-6 drawing with its symmetric outline and evenly arrayed hole pattern.",
        services="MIRROR, STRETCH (crossing window), SCALE (Reference), ARRAYRECT, ARRAYPOLAR",
        dwg="ex6.dwg",
        img="ex6.png",
        steps=[
            ("Open the EX-6 sheet (ex6-drawing-sheet.pdf) and find its axis of symmetry", ""),
            ("Draw one half of the outline, then mirror it across the centreline", "MI → select → axis pt1 → pt2 → N"),
            ("Array one hole into the rectangular pattern (rows, columns, spacing from the sheet)", "AR → R → rows/cols/spacing"),
            ("Distribute the bolt holes around the centre with a polar array", "AR → PO → centre → items → 360"),
            ("Stretch the slot to its dimensioned length with a crossing window, scale a feature with Reference", "S → crossing → base → distance  ·  SC → R"),
            ("Verify against ex6.dwg and save", "SAVEAS ex6-mine.dwg"),
        ],
        test="The two halves are perfectly symmetric about the centreline, array counts and spacings "
             "match the sheet, and the stretched slot measures the dimensioned length.",
    ),
]
