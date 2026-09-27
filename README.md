# Singularity

Replaces Ragnarok's appearance with Singularity, a massive black hole generator with rotating containment rings and dramatic effects. Keeps the original gameplay, balance, and audio.

For **Planetary Annihilation: TITANS**, by **krplatz**. Version 0.9.6 — beta.

![Singularity](ui/mods/com.pa.endgame.ragnarok-singularity/icon.png)

## Features

- Dense containment structure with nested animated gyroscopes and opening gantries.
- Plasma compression followed by black-hole formation around 24 seconds after activation.
- Warped accretion mesh, inward particles and a controlled core descent.
- Blue PA-style build icon with Titan marker; displayed unit name **Singularity**.
- Stock costs, health, weapon, charge duration, planet destruction and audio cues. No audio files are bundled.

This replaces the existing Ragnarok visually; it does not add a separate buildable unit. The stock charge is 176 seconds, not the shortened comparison-video timing. Other players need this client mod to see its visuals.

## 0.9.6 packaging and review follow-up

Adds the metadata signature placeholder and TITANS-only flag. Source texture PNGs remain in Git but are omitted from installation archives. Adds a stock-file baseline and maintenance check for all 18 replacements. Disc facing and mesh depth corrections were already delivered in 0.9.4.

## Compatibility and maintenance

The full Ragnarok unit definition is included to display the name **Singularity**. Its other fields match build 124680. This copy can retain older gameplay values after a PA update, including in Galactic War, and can conflict with mods that change Ragnarok's definition. With conflicting server mods, client tooltips may not match server values. Nuclear Mayhem (WIP) and Nuke warfare were identified by the review as shipping the same unit path; compatibility is not established. Other Ragnarok appearance mods can also conflict.

For maintainers: see [the release checklist](maintenance/RELEASE_CHECKLIST.md) and run `python tools/check_stock.py --game-root "PATH_TO_PA_TITANS"` after game updates. These maintenance files are retained in the source repository, not the install archive.

The legacy identifier `com.pa.endgame.ragnarok-singularity` is retained for existing installation/update continuity. **endgame is a legacy project namespace, not the public author credit.** The author and public mod name remain **krplatz** and **Singularity**. Any identifier migration must be coordinated with catalogue maintainers.

## 0.9.5 construction wireframe

Bakes the construction distance mask into diffuse alpha, replacing the constant alpha that made the early build look like a filled hologram. Repackages 9,016 planar surface islands into a dedicated atlas, resampling existing colours and material masks. Mesh positions, normals, skinning, indices, effects and animations remain unchanged. Asset validation passes; wire thickness and appearance still need in-game confirmation on a newly constructed unit.

## 0.9.4 effect pass

Reworks startup into a continuous plasma gathering, heating and compression sequence through the 24-second collapse. Both sprite dimensions are specified explicitly. Pins the accretion mesh to EmitterZ, adds a moving hot filament layer, and increases inward particle activity. This pass still needs in-game visual verification; the 0.9.3 unit texture correction has been confirmed in-game.

## 0.9.3 texture correction

Fixes an unintended second vertical UV flip during model conversion. In 0.9.2, metal surfaces sampled unused black atlas tiles and some surfaces sampled the orange reactor tile. Only texture coordinates changed; geometry, animation and gameplay are unchanged. All vertices now sample populated atlas tiles. The corrected unit textures were subsequently confirmed in-game.

## Status

The model, corrected textures, and latest effect pass have been viewed in-game by the author. Construction wire thickness and broader compatibility still need in-game verification. One test installation loses its local filesystem-mod registration when leaving Community Mods. Publication through the managed download route is being evaluated; it is not a confirmed fix.

All 14 PAPA assets pass the game's format reader and asset references resolve. The unit JSON differs from stock only in its display name. Audio events match stock. These checks do not establish visual correctness or multiplayer compatibility.

## Installation

Submitted to Community Mods for review. Catalogue availability and update timing depend on the Community Mods service.

For manual testing, download this repository and place its contents in a folder named `com.pa.endgame.ragnarok-singularity` under your PA data directory's `client_mods` folder. `modinfo.json` must be directly inside that folder. Enable **Singularity** in Community Mods and fully restart the game to clear cached art. Disable conflicting Ragnarok appearance mods. The strategic-map symbol remains stock.

To remove, disable Singularity and restart. When switching to a managed Community Mods download, move the manual copy out of `client_mods` first to avoid duplicate identifiers.

## Credits

Mod author: **krplatz**. Custom model, animations, textures, effects and icon work were developed with AI-assisted tooling; the blue build icon uses image generation with the model and stock icon as references. The installed Legion Holocene effects informed the layered particle approach; no Legion assets are bundled.

Adapted stock unit/effect data and game references belong to their respective Planetary Annihilation rights holders. Planetary Annihilation: TITANS is required. This project is not an official game release.

## Licence

Original contributions are available under the [MIT licence](LICENSE). See [third-party notices](THIRD_PARTY_NOTICES.md) for excluded game material and licence scope.
