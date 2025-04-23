# Product Context: MO2 Plugin for Oblivion Remaster

## Why This Project Exists

The Oblivion Remaster represents a significant update to a classic Bethesda game, bringing it to modern platforms with updated graphics and new modding capabilities. However, without proper mod management tools, the modding community for Oblivion Remaster would face significant challenges:

1. **Mod Conflicts**: Without a virtual file system like MO2 provides, mods would overwrite each other directly in the game directory, making it difficult to manage multiple mods.

2. **Complex Installation**: The hybrid nature of Oblivion Remaster modding (combining traditional Bethesda modding with Unreal Engine 5 elements) makes manual mod installation more complex and error-prone.

3. **Dual Modding Systems**: Oblivion Remaster supports both traditional Bethesda-style mods (.esp/.bsa) and Unreal Engine 5 mods (.pak/.ucas/.utoc), requiring users to understand and manage two different modding approaches.

4. **Load Order Management**: Proper load order is crucial for Bethesda games, and without tools like MO2, managing load order becomes difficult, especially with many mods installed.

5. **Mod Testing and Switching**: Without MO2's profile system, testing different mod configurations or switching between mod setups would require manual reinstallation of mods.

## Problems It Solves

This MO2 plugin for Oblivion Remaster aims to solve these problems by:

1. **Unified Mod Management**: Providing a single interface to manage all types of mods for Oblivion Remaster, regardless of whether they use traditional Bethesda formats or Unreal Engine 5 formats.

2. **Virtual File System**: Leveraging MO2's virtual file system to allow mods to be installed in separate directories, preventing them from overwriting each other directly.

3. **Dual Modding System Support**: Handling both traditional Bethesda mods (mapping to `OblivionRemastered\Content\Dev\ObvData\Data`) and UE5 mods (mapping to `OblivionRemastered\Content\Paks\~mods`).

4. **Profile System**: Enabling users to create different profiles with different mod configurations, making it easy to switch between mod setups or test new mods.

5. **Load Order Management**: Providing tools to manage the load order of plugins (via `Plugins.txt` for traditional mods) and UE5 mods (via alphabetical loading).

6. **Conflict Visualization**: Showing conflicts between mods and allowing users to resolve them easily.

7. **INI File Management**: Managing game configuration files on a per-profile basis, allowing users to have different game settings for different mod setups.

## How It Should Work

From a user perspective, the plugin should work seamlessly with MO2:

1. **Game Detection**: MO2 should automatically detect the Oblivion Remaster installation when the plugin is installed.

2. **Mod Installation**: Users should be able to install mods through MO2's standard installation methods (manual installation, FOMOD installers, etc.).

3. **Mod Type Detection**: The plugin should automatically detect whether a mod is a traditional Bethesda mod, a UE5 mod, or a hybrid, and handle it accordingly.

4. **Mod Management**: The plugin should provide a clear interface for enabling/disabling mods, managing load order, and resolving conflicts, with visual indicators for mod type.

5. **Profile System**: Users should be able to create and switch between different profiles with different mod configurations and game settings.

6. **Game Launch**: MO2 should be able to launch Oblivion Remaster with the selected mods and load order.

From a technical perspective, the plugin needs to:

1. **Integrate with MO2's Plugin System**: As a Python plugin using the basic_games framework for better portability and flexibility.

2. **Handle Dual Modding Systems**: Properly manage both traditional Bethesda mod files (.esp, .bsa, etc.) and Unreal Engine 5 files (.pak, .ucas, .utoc).

3. **Implement Virtual File System Mapping**: Ensure MO2's USVFS correctly maps mod files to the appropriate game directories:
   - Traditional mods to `OblivionRemastered\Content\Dev\ObvData\Data`
   - UE5 mods to `OblivionRemastered\Content\Paks\~mods`

4. **Manage Load Order**: Handle load order for both modding systems:
   - Traditional mods via the `Plugins.txt` file
   - UE5 mods via alphabetical loading (potentially with a prefix system for user control)

5. **Handle INI Files**: Manage game configuration files on a per-profile basis, including Oblivion.ini and other relevant configuration files.

## User Experience Goals

The plugin should provide a user experience that is:

1. **Intuitive**: Users familiar with MO2 for other Bethesda games should find the interface familiar and easy to use, despite the added complexity of dual modding systems.

2. **Comprehensive**: The plugin should support all common modding scenarios for Oblivion Remaster, including traditional mods, UE5 mods, and hybrids.

3. **Informative**: The plugin should provide clear information about mods, their types, conflicts, and any issues that arise, with visual indicators to distinguish between mod types.

4. **Flexible**: Users should be able to easily manage both traditional and UE5 mods, with appropriate tools for each type.

5. **Reliable**: Mod installation, management, and game launching should work consistently and reliably across both modding systems.

6. **Efficient**: The plugin should perform well, even with large mod collections, and should not significantly impact MO2's performance.

## Specific Modding Scenarios

### Traditional Bethesda Mod Installation

For traditional Bethesda mods (.esp/.bsa), the installation process typically involves:

1. Extracting mod files to `OblivionRemastered\Content\Dev\ObvData\Data`
2. Adding the .esp file to `Plugins.txt` to enable it in the game

Our plugin will handle this by:
- Detecting traditional mod files during installation
- Placing them in the correct virtual directory structure
- Managing the `Plugins.txt` file to handle load order

### Unreal Engine 5 Mod Installation

For UE5 mods (.pak/.ucas/.utoc), the installation process typically involves:

1. Placing .pak files in `OblivionRemastered\Content\Paks\~mods`
2. Ensuring alphabetical loading order for load priority

Our plugin will handle this by:
- Detecting UE5 mod files during installation
- Placing them in the correct virtual directory structure
- Potentially implementing a prefix system to allow users to control load order

### Hybrid Mod Installation

Some mods might contain both traditional and UE5 components. Our plugin will:
- Detect both types of files
- Place each in the appropriate directory structure
- Provide a unified interface for managing the mod as a whole
