# The Violence

A tactical autobattler RPG in Godot 4. You run the police department of **Port Carrick**, a rust-belt city on the edge of
collapse: manage budget, hiring and firing, then plan operations that play out hands-off. Civilian harm and excessive force
cost you allies before a contested election ends the forty-week campaign.

*Status as of 2026-10-27.* This repository holds **two tracks that were developed in separate sessions and have not been
harmonised**. They are documented separately below, and where they disagree the disagreement is recorded, not smoothed over.

| Track | What it is | Where | Latest state |
| --- | --- | --- | --- |
| **The game** | The Godot project: simulation, campaign, UI, cutscenes, 34 runnable headless test harnesses | repository root | 1.3 candidate (roguelike story mode) with the crayon visual overhaul applied to gameplay and menus; `Version.VALUE` still reads 1.2.1 |
| **Port Carrick** | The city as a generated, validated data model plus its map viewer | [`port-carrick/`](port-carrick/) | City model v0.4, 74/74 rules, regenerates byte for byte |

To play or test the game, see [`docs/GAME_README.md`](docs/GAME_README.md) (install Godot 4.4+, import `project.godot`;
`tools/run_tests.sh --quick` runs the gates).

---

## Track 1 — the game

### Roadmap position

**Done**
- **The 1.3 run layer** (`scripts/campaign/rogue.gd`): every story is a seeded forty-week ironman run with inheritance
  doctrines, procurement contracts, training programs, offers (14), events (20), a run score on election night and a legacy
  file that unlocks more doctrines. Design: [`docs/ROGUELIKE_PLAN.md`](docs/ROGUELIKE_PLAN.md).
- **Endless Battle removed** (`scripts/city/`, `city_main.gd`, `scenes/city.tscn` and their tests are gone).
- **Crayon visual overhaul, gameplay and menus** ([`docs/VISUAL_OVERHAUL.md`](docs/VISUAL_OVERHAUL.md)): the page, doors,
  63 props and vehicles, figures with carries and eight death sprites per look, physical blood, charcoal fog, boiling
  sprites baked to `assets/crayon/`, the title page and UI, and a "Line boil" setting. Everything is drawn in code
  (`scripts/view/crayon*.gd`), not recoloured. Prototype stills and clips: [`docs/overhaul/`](docs/overhaul/).
- **Two playtest rounds** of the 1.3 candidate: [`docs/PLAYTEST_2026-10-27.md`](docs/PLAYTEST_2026-10-27.md).
- **Merged current model** of the game: [`docs/CURRENT_MODEL.md`](docs/CURRENT_MODEL.md) (the 1.21 tree wins where it
  disagreed with earlier notes).

**In progress / open**
- **The ten release recommendations from the playtest**, none finished except one interim mitigation:
  1. *Trauma cliff* — officers carrying trauma above about 12 misjudge rally crowds (nineteen civilians killed at trauma 14
     versus none at 10 in the same test). "Suggest a plan" now keeps them off crowd duty; the flaw in `world.gd`
     (`misjudge_p` / `add_stress`) is **not fixed**. Gate: `event_probe.gd --trauma=14 --n=8` ≤ 1 civilian hit.
  2. Make the roster a live constraint (a "next week" strip, emergency lateral hires): every run ends with 5–7 of 20 officers fit.
  3. Fix the money curve (accounts go negative early, then pass $200,000 by election night).
  4. Give lost allies a way back.
  5. Use the empty left two-thirds of the management screens (draw the city).
  6. Stop the guided first operation buying $4,700 of kit on its own.
  7. Make the harnesses fail honestly (`_check.gd` exit codes, runner-scaled timeouts; `orders_test` times out at its 600 s budget under load).
  8. Balance the run layer with numbers: `rogue_balance_test.gd`, 20 seeds, four policies.
  9. Finish content: 10 of the 14 cutscene shorts are never played; music beds.
  10. Ship: rebuild the exe, test on Windows 10/11, add `LICENSE` and `THIRD_PARTY_NOTICES`, sort out signing, then bump to 1.3.0 with `tools/sync_version.py`.
- **Visual overhaul, remaining:** cutscenes are not re-rendered in the crayon look (phase 6, deliberately left until last);
  the per-phase gates in the plan (`tests/rig_gallery.gd` re-render, all maps under 4 ms/frame) have no recorded result;
  the plan still carries an "open question" about a cut-off note that the later work has already moved past.
- **Release readiness** ([`RELEASE_READINESS.md`](RELEASE_READINESS.md), dated 2026-10-24): the only Windows binary has never
  been run on Windows hardware and is unsigned (SmartScreen will warn); CI exists but is not active (see Known gaps).

**Next steps, in suggested order**
1. Fix the trauma cliff in the simulation (rec 1) — it produced the worst playtest outcome.
2. Make the harnesses honest (rec 7) before trusting any further gate.
3. Add the balance harness (rec 8), then fix the money curve (rec 3) against its numbers.
4. Roster strip and ally reconciliation (recs 2 and 4); first-operation spending (rec 6); use the screen (rec 5).
5. Finish content and music (rec 9), re-render the cutscenes in the crayon look.
6. Build, test on Windows, license, sign and bump to 1.3.0 (rec 10); publish the exe as a GitHub Release asset.

---

## Track 2 — Port Carrick, the city model

Full detail in [`port-carrick/README.md`](port-carrick/README.md).

**Done (v0.4):** locked topography and proposed geology; growth by era; four unequal harbour basins in the wide river
reaches; every historical crossing with the 1958 viaduct last; floodwall and pumps; utilities; dual-bank services with
bridge-closure scenarios; causal abandonment; Chicago-style addresses; a crayon-styled viewer. 12,666 buildings,
population exactly 100,000 now and 150,000 at the 1962 peak.

**Next:** the author's edit pass; bind the game to `city.json` (nothing loads it yet); pin the new levels to real addresses;
decide whether bridge closure becomes a campaign mechanic.

Design docs: [`port-carrick/docs/MAP_SPEC.md`](port-carrick/docs/MAP_SPEC.md),
[`port-carrick/docs/CANON_AND_CRITIQUE.md`](port-carrick/docs/CANON_AND_CRITIQUE.md).

---

## Contradictions kept as they are

The two tracks (and the notes within them) were not reconciled. These are the known disagreements:

- **Accent colour.** The original art direction, the game README and the project description say *single crimson accent*;
  `docs/VISUAL_OVERHAUL.md` explicitly supersedes it (red stays for blood and the VOTE crosses, other colours join).
  The game README still documents the F2 "red ink / monochrome" toggle.
- **Map count and version.** `docs/design/LEVEL_DESIGN_CONSTRAINTS.md` describes **1.5 with sixteen maps (00–15)**; the code
  here has **twelve (`m00`–`m11`)**, the game README and the overhaul plan say twelve, and `Version.VALUE` is **1.2.1**. See Known gaps.
- **Street names.** The 1.5 level list names Tannery Street, River Road, County Road 9, Civic Avenue, Ridge Road and Main
  Street. Of these none exists in `city.json` (it has *Tannery Boulevard*; *Furnace Street* does exist). Level design and
  the city model have not been reconciled.
- **Harbour location.** `port-carrick/docs/CANON_AND_CRITIQUE.md` still lists "four basins at the narrows"; the Map Spec v0.4
  moved them to the wide reaches and says it supersedes that line. The Canon doc carries a banner saying so.
- **Docs in two places.** The claude.ai Project "the violence" holds earlier copies of `CURRENT_MODEL`, `ROGUELIKE_PLAN`,
  `VISUAL_OVERHAUL` and `PLAYTEST_2026-10-27`. The copies in this repository are the working-tree versions.

## Known gaps

- **The 1.5 command layer is not in this snapshot.** Squads placed in accessible zones, the ranking officer as Squad 1,
  succession of command, squad reports and the "Mother" brain, `tests/command_test.gd`, `scripts/campaign/deploy.gd`,
  `tests/strike.gd` and maps 12–15 were built in a separate working session and never reached the folder this repository
  was made from. Only their design survives (`docs/design/LEVEL_DESIGN_CONSTRAINTS.md`). If a copy exists elsewhere it
  should be merged in.
- **The Windows exe is not in git.** `release/TheViolence.exe` (about 147 MB, shipped locally as seven parts) exceeds
  GitHub's 100 MB limit; the project's own `.gitignore` already routes it to a GitHub Release. Rebuild with
  `tools/build_windows_exe.sh`. Only `release/README.md` is tracked.
- **CI is not active.** `tools/ci/ci.yml` must be moved to `.github/workflows/ci.yml` (the account that originally pushed
  it could not create workflow files).
- **Version metadata** (`scripts/version.gd`, `project.godot`, `export_presets.cfg`) still says 1.2.1 although the tree
  is the 1.3 candidate.
- **Not pushed from the source folder:** `Crime-Thriller-main` (a separate prose-writing project, unrelated to the game).

## Repository layout

```
README.md                 this file
CHANGELOG.md              release history (newest first; "Unreleased" = the 1.3 candidate)
RELEASE.md                what is inside the exe and how it was built
RELEASE_READINESS.md      the 2026-10-24 assessment of what stands between the game and a release
project.godot, scenes/, scripts/, shaders/, fonts/, assets/     the Godot project
tests/                    36 files, 34 runnable headless harnesses (run with tools/run_tests.sh)
tools/                    test runner, version sync, exe build, crayon baking, CI definition
cinematics/               Remotion project that renders the cutscenes
Play.bat, play.sh, "Build TheViolence.exe.bat", release/        launchers and the (untracked) exe folder
docs/                     CURRENT_MODEL, ROGUELIKE_PLAN, PLAYTEST_2026-10-27, VISUAL_OVERHAUL, GAME_README
docs/design/              level design constraints (1.5)
docs/overhaul/            crayon prototype stills and clips
docs/archive/             the superseded v1.2.1 playtest report
port-carrick/             the city model (generator, validator, viewer, data, docs)
```

## Housekeeping done on 2026-10-27

Removed as superseded or duplicate: the older `TheViolence-v1.2.1-main` copy (every file in it was either identical to,
or older than, the 1.21 tree, apart from the Endless City files removed on purpose); 37 prose-writing files from the
separate Crime-Thriller project that had been copied into the game's root (36 had byte-identical twins there, and `style_lint.py` was a path-adjusted copy of the one in `Crime-Thriller-main/tools`);
`crayon_overhaul_src.zip` (an archive of 1,326 files already in the tree, all identical); a stray `download` file; a
duplicate root-level `city.json`; and three superseded generator snapshots. `PLAYTEST_REPORT.md` (the v1.2.1 report)
moved to `docs/archive/`; the old README moved to `docs/GAME_README.md`.
