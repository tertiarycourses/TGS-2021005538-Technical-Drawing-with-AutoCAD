# DWG Reference Review - v13

## Outcome

The 36 DWG files under `reference/autocad dwg/` are technically usable as AutoCAD references:

- all 36 parse successfully as AutoCAD 2013-format (`AC1027`) drawings;
- 22 declare millimetres and 14 declare inches;
- one pair is byte-identical (`GND Floor Plan.dwg` and `OLD_GND Floor Plan.dwg`);
- `Units-METRIC.dwg` declares inches (`INSUNITS=1`) despite its filename, so it must not be used as a metric template without correction;
- the supplied conclusion slide identifies the collection as LinkedIn Learning material by Shaun Bryant.

## Publication decision

The repository's `.gitignore` states that `reference/` contains source material that is not ours to republish. The new DWGs therefore remain local reference material and are not copied into GitHub, Google Drive learner labs or LMS-TMS.

## Courseware use

The drawings were used to validate the intended progression across units, navigation, geometry, modifying objects, layers, reusable content, Xrefs, annotation, viewports and collaboration. The public lab update uses the already redistributable practice assets in `labs/_assets/`:

| Lab | Active practice asset | Use in v13 |
|---|---|---|
| 1 | `workspaces.dwg`, `drafting-settings.dwg` | Workspace and precision-setting audit |
| 8 | `sawblade.dwg` | Polar-array property audit |
| 9 | `office-plan-ground-floor.dwg` | Five-layer standards audit |
| 10 | `new-office-design.dwg` | Grips, select-similar, isolate and hide |
| 11 | `architecture-library.dwg`, `new-office-dynamic-blocks.dwg` | DesignCenter and dynamic-block practice |
| 12 | `new-office-layout-with-xref.dwg`, `Landscaping_REV1.dwg` | Relative-Xref repair and portability check |
| 15 | `landscaping-rev1.dwg`, `landscaping-rev2.dwg` | DWG Compare and revision-cloud review |
| 16 | `new-office-layout.dwg` | Layout, viewport and plotting audit |

## Lab 12 dependency check

LibreDWG inspection confirms that `new-office-layout-with-xref.dwg` expects the relative path `.\\Landscaping_REV1.dwg`. v13 includes that exact filename in the same lab folder so the Xref can resolve when the folder is moved as a unit.
