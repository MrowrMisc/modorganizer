# Project Brief: MO2 Plugin for Oblivion Remaster

## Project Overview
Create a Mod Organizer 2 (MO2) plugin to support the new Oblivion Remaster. The plugin will enable MO2 to manage mods for Oblivion Remaster, which has a modding approach that combines elements from traditional Oblivion (Bethesda-style .esp/.bsa files) and Unreal Engine 5 games (.pak/.ucas/.utoc files).

## Core Requirements
1. Enable MO2 to detect and manage the Oblivion Remaster installation
2. Support mod installation and management specific to Oblivion Remaster
3. Handle the dual modding systems (traditional Bethesda and UE5)
4. Provide appropriate UI elements and tools for managing Oblivion Remaster mods

## Technical Considerations
- The plugin will be developed as a Python plugin using the basic_games framework for better portability and flexibility
- The plugin needs to handle the hybrid nature of Oblivion Remaster modding, including:
  - Traditional Bethesda-style plugins (.esp/.esm files) and archives (.bsa files)
  - Unreal Engine 5 assets (.pak/.ucas/.utoc files)
  - Game configuration files (.ini files)

## Project Goals
1. Seamless integration with MO2's existing systems
2. User-friendly interface for managing Oblivion Remaster mods
3. Support for all relevant mod formats and installation methods
4. Maintainable and extensible codebase that can adapt to future updates

## Constraints
- Must work within MO2's plugin architecture
- Must be compatible with MO2's virtual file system (USVFS)
- Should follow best practices established by existing game plugins

## Success Criteria
- MO2 can detect and manage Oblivion Remaster installation
- Users can install, enable/disable, and manage both traditional and UE5 mods
- Plugin handles the dual modding systems correctly
- Plugin provides appropriate UI elements for Oblivion Remaster-specific features

## Game-Specific Information

### Nexus IDs
- Oblivion Remastered: GameNexusId `7587` and GameNexusName `oblivionremastered`
- Original Oblivion: GameNexusId `101` and GameNexusName `oblivion`

### File Structure
- Game installation path: `[Steam Library]\steamapps\common\Oblivion Remastered`
- Main directories: `Engine` (UE5 engine) and `OblivionRemastered` (game content)
- Traditional Bethesda mod files path: `OblivionRemastered\Content\Dev\ObvData\Data`
- UE5 mod files path: `OblivionRemastered\Content\Paks\~mods`
- Game configuration files: `OblivionRemastered\Content\Dev\ObvData\Oblivion.ini` and others

### Modding Approaches
1. **Traditional Bethesda Modding**:
   - Uses .esp/.esm plugin files and .bsa archives
   - Load order managed through `Plugins.txt` file
   - Compatible with some original Oblivion mods

2. **Unreal Engine 5 Modding**:
   - Uses .pak/.ucas/.utoc files
   - Loaded alphabetically from the `~mods` folder
   - Follows standard UE5 modding patterns
