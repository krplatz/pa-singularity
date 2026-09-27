# Release checklist

After every PA patch, run `python tools/check_stock.py --game-root "PATH_TO_PA_TITANS"` from the source checkout. The baseline records all 18 replaced stock files and their SHA-256 hashes for build 124680. A changed hash requires review; never update the baseline just to silence a failure.

1. Compare every changed stock file with the replacement. Preserve relevant stock fixes while retaining the intended model/effects.
2. Refresh the unit JSON from installed stock, changing only display_name to Singularity. This matters especially for Galactic War, where client-loaded unit specs can become battle specs.
3. Compare audio events and attachment bones; validate PAPA formats and all effect references.
4. Verify startup, collapse, disc orientation from multiple camera angles, construction wireframe, core descent, and destruction in-game.
5. Test compatibility with other Ragnarok mods. Do not claim compatibility with conflicting unit or visual replacements without testing.
6. Update build/version/date only to the version actually checked. Run the stock check again and regenerate the baseline only after reviewing differences.
7. Package with git archive so export-ignore rules exclude source textures and maintenance tools. Check modinfo.json, both UI icons, all 14 PAPA assets, and absence of source texture PNGs in the ZIP.
8. Keep the existing identifier for update continuity. Coordinate any migration with the catalogue maintainers before changing it.
