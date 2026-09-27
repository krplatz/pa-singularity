# Singularity

A visual replacement for Ragnarok in **Planetary Annihilation: TITANS**, by **krplatz**.

![Singularity](ui/mods/com.pa.endgame.ragnarok-singularity/icon.png)

Singularity turns Ragnarok into a massive black hole generator, with rotating containment rings, moving gantries, a plasma buildup and collapse, and a flowing accretion disc. Includes a custom build icon and construction wireframe.

It replaces the existing Ragnarok rather than adding a separate unit. Costs, health, charge duration, planet destruction and audio match the stock game. Other players need the client mod to see its visuals. The strategic-map symbol remains stock.

## Installation

Download the [latest release](https://github.com/krplatz/pa-singularity/releases) and extract its mod folder into your PA data directory's `client_mods` folder. Enable **Singularity** in Community Mods, then fully restart PA. TITANS is required.

For a managed Community Mods installation, use the in-game catalogue once the mod is available there. Remove the manual copy from `client_mods` before switching to avoid duplicate installations. Disable the mod and restart PA to uninstall.

## Compatibility and status

**Beta, checked against build 124680.** The model, textures and effects have been viewed in-game. Construction wire thickness and broader multiplayer/mod compatibility still need verification. A local installation has also shown intermittent registration issues in the mod manager.

The mod includes Ragnarok's full unit definition to display the name **Singularity**. Other fields match stock, but the file must be refreshed after relevant game updates, especially for Galactic War. Mods that alter Ragnarok's definition or appearance may conflict; client tooltips can differ from server values. Compatibility with Nuclear Mayhem and Nuke warfare is not established.

Maintainers can use the [release checklist](https://github.com/krplatz/pa-singularity/blob/main/maintenance/RELEASE_CHECKLIST.md) and stock-file check to review all 18 replacements after game updates. The existing identifier, `com.pa.endgame.ragnarok-singularity`, is retained for update continuity; the public author is **krplatz**.

## Credits and licence

Developed with AI-assisted tooling. The build icon uses image generation with the model and stock icon as references. Legion's Holocene effects informed the particle approach; no Legion custom assets are bundled.

Original contributions are available under the [MIT licence](LICENSE). Adapted game material remains with its respective rights holders; see [third-party notices](THIRD_PARTY_NOTICES.md). This is an unofficial mod.
