"""Topic 1 — Getting Started with AutoCAD (A1, K1): hands-on activities."""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Setting Up a New Drawing",
        objective="LO1 — read and visualize AutoCAD technical drawings; set up a drawing environment (A1, K1)",
        desc="Create and verify a metric drawing environment, compare saved workspace and drafting-setting "
             "examples, then open a finished drawing and practise reading it with zoom, pan and ViewCube.",
        build="A correctly configured metric drawing saved as DWG, a settings audit, and confident "
              "navigation of an existing technical drawing.",
        services="ACADISO template, UNITS, LIMITS, DSETTINGS, WSCURRENT, ZOOM, PAN, ViewCube",
        dwg="lab01-table.dwg",
        steps=[
            ("Start AutoCAD and create a new drawing from the ISO metric template", "NEW → acadiso.dwt"),
            ("Open workspaces.dwg, compare the available workspaces, then switch to Drafting & Annotation", "OPEN workspaces.dwg → WSCURRENT → Drafting & Annotation"),
            ("Set decimal millimetres with 0.00 precision and decimal degrees for angles", "UNITS → Insertion scale: Millimetres → Length: Decimal, 0.00"),
            ("Frame an A3-sized working area with drawing limits, then zoom to it", "LIMITS → 0,0 → 420,297  |  ZOOM → All"),
            ("Open drafting-settings.dwg and audit grid, snap, ortho, polar and object-snap settings", "OPEN drafting-settings.dwg → DSETTINGS · F7 · F9 · F8 · F10 · F3"),
            ("Open lab01-table.dwg and navigate it: wheel-zoom, pan, zoom window and zoom extents", "OPEN lab01-table.dwg → Z → W / Z → E"),
            ("Identify the views, dimensions and title information in the drawing, then save your setup file", "SAVEAS → lab01-setup.dwg"),
        ],
        test="INSUNITS reports millimetres, limits are 420 × 297, Drafting & Annotation is current, "
             "the precision-aid audit is complete, and lab01-setup.dwg reopens with the settings intact.",
    ),
]
