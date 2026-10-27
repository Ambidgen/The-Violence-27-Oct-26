# Port Carrick, PA — the city model

The definitive map of the game's city, **generated rather than drawn**: one deterministic Python pipeline writes
`city.json`; an independent validator re-checks it from the JSON alone; a single-file viewer draws it. Everything
level-design touches downstream (streets, addresses, landmarks, situation sites, wards) is meant to read from
`city.json` and never contradict it.

This track is **separate from the Godot game** in the repository root: it has its own version (city model **v0.4**),
its own docs and its own roadmap, and nothing in the game reads it yet.

## Run it

```sh
pip install -r requirements.txt          # numpy, scipy, shapely>=2, scikit-image
python3 make_city.py city.json           # ~1 minute; seed 1995; exits non-zero if any validator rule fails
python3 build_viewer.py city.json        # writes port-carrick-map.html (open in a browser)
python3 mutate.py && python3 mutate2.py  # 36 mutation tests: each injected contradiction must be caught
```

Verified 2026-10-27: the pipeline regenerates the committed `city.json` **byte for byte**, 74/74 validator rules pass,
and all 36 mutation tests (10 original + 26 for the v4 rules) are caught.

## Files

| File | Role |
| --- | --- |
| `make_city.py` | Entry point: streets → landmarks → lots/buildings → finalize → export → validate |
| `pc_geo.py` | Single owner of every geometric fact: frame, river, terrain, harbour basins, bridge, floodwall, crossings |
| `pc_streets.py` | Programmatic road system derived from `pc_geo` (no hand-placed road coordinates): organic Ferry Street kernel, accretive grids, rail |
| `pc_net.py` | Travel-time model over the noded street network, shared by generator and validator (service response times, bridge-closure scenarios) |
| `pc_landmarks.py`, `pc_build.py`, `pc_finalize.py` | Landmarks, lots and buildings, history/abandonment/flood exposure, exact population calibration |
| `pc_addr.py`, `pc_export.py` | Chicago-style address geocoder; sites, address matrix, contours and the `city.json` document |
| `sites_src.json` | The 25 hand-authored situation sites (name, ward, type, archetype, visibility, notes) read by `pc_export.py` |
| `validate_city.py`, `validate_layers.py` | Independent rule checker: GE, RD, BD, AD, PD, ST + the v4 layers HS history, FL flood, UT utilities, SV services |
| `mutate.py`, `mutate2.py` | Mutation tests for the validator |
| `viewer_template.html`, `build_viewer.py` | Crayon-styled map viewer; the JSON is inlined into one HTML file |
| `city.json` | The model (1.9 MB): 275 streets, 12,666 buildings, 80 landmarks, 25 situation sites, 6 wards |
| `docs/MAP_SPEC.md` | The spec (v0.4) |
| `docs/CANON_AND_CRITIQUE.md` | Locked topography, proposed geology, the infrastructure critique v0.4 implements |

## Where it stands

**Done (v0.4):** locked topography (river funnel, 215 m datum, 222 m flood line, Slag, Kilbride knoll, south bluff);
growth by era (Ferry Street 1794 → peak 150,000 in 1962 → 100,000 now); four unequal harbour basins relocated to the wide
reaches; ferry, swing/lift, rail lift and the 1958 viaduct as the last crossing; floodwall, gates and 12 pump stations;
utilities with validated fall lines; dual-bank services with three bridge-closure scenarios; causal abandonment for five
ghost districts. All nine items of the Canon critique's change list are implemented.

**Next (not started):**
1. The author's edit pass: the model was built to be edited by hand and then locked as the definitive map.
2. Bind the game to it: nothing in the Godot project loads `city.json` yet. Candidates are situations, ward trust and
   the 25 sites.
3. Place levels on the map. The 1.5 level list (see `../docs/design/LEVEL_DESIGN_CONSTRAINTS.md`) names four new maps in
   Tannery Flats, Ironworks, Riverside and Cinder Hollow; each should be pinned to an address in `city.json`.
4. Decide whether the bridge-closure scenarios become a campaign mechanic (the critique called it "a gameplay gift").

## Invented assumptions (veto freely)

Geology and flow direction, port founding years, pump and plant positions, unbuilt far bays. Street and landmark names
beyond the original project docs are placeholders.

## Filing notes (2026-10-27)

- `pc_export.py` used to read the situation sites from a hard-coded scratch path in an earlier working session, so the
  pipeline could not run anywhere else. The sites are now bundled as `sites_src.json` (extracted from the committed
  `city.json`) and the path is relative. Regenerated output is byte-identical to the previous `city.json`.
- Three superseded snapshots (`pc_geo_v4a.py`, `pc_streets_v4a.py`, `pc_landmarks_v4a.py`, which put the harbour basins
  at the narrows) and a duplicate root-level `city.json` were removed.
