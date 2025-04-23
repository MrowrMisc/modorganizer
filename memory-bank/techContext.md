# Technical Context: MO2 Plugin for Oblivion Remaster

## Technologies Used

### Core Technologies

1. **Python** - For plugin development
   - Used by the basic_games framework
   - Easier to develop and maintain than C++
   - More portable and flexible
   - Preferred for this project

2. **Qt** - For UI components
   - Used by MO2 for its user interface
   - Required for any custom UI elements in the plugin
   - Version used by MO2: Qt 5/6 (depending on MO2 version)
   - Accessed through Python bindings in the basic_games framework

### MO2-Specific Technologies

1. **USVFS (User Space Virtual File System)**
   - Core technology behind MO2's mod virtualization
   - Allows mods to be installed in separate directories
   - Maps files from mod directories to the game directory at runtime
   - Will be used to map files to both traditional and UE5 mod directories

2. **basic_games Framework**
   - Python-based framework for creating game plugins
   - Provides base classes and utilities for game support
   - Simplifies integration with MO2's systems
   - Allows for custom features through registration

3. **Plugin Interfaces**
   - `BasicGame` - Base class for Python-based game plugins
   - `BasicGameSaveGameInfo` - Interface for save game handling
   - `BasicGamePluginManager` - Interface for plugin management
   - `BasicInstaller` - Base class for custom installers

4. **MO2 API**
   - Provides access to MO2's core functionality
   - Includes interfaces for mod management, profile management, etc.
   - Available to Python plugins through the basic_games framework

### Game-Specific Technologies

1. **Bethesda Plugin System**
   - .esp/.esm file format for game plugins
   - .bsa file format for asset archives
   - Load order management via Plugins.txt
   - Plugin dependencies and rules

2. **Unreal Engine 5**
   - .pak/.ucas/.utoc file formats for asset packaging
   - Alphabetical loading from the ~mods folder
   - Standard UE5 modding patterns

## Development Setup

### For Python Plugin Development

1. **Required Tools**
   - Python 3.8 or later
   - Text editor or IDE with Python support (e.g., Visual Studio Code, PyCharm)
   - Git for version control

2. **Development Environment Setup**
   - Clone the modorganizer-basic_games repository
   - Create a new game plugin file in the games directory
   - Implement the required functionality

3. **Development Workflow**
   - Create a class that inherits from BasicGame
   - Define game-specific properties as class attributes
   - Override methods for custom behavior
   - Register custom features using `_register_feature`
   - Test by placing the plugin in MO2's plugins directory

4. **Testing Environment**
   - Install Mod Organizer 2
   - Install Oblivion Remaster
   - Place the plugin in the appropriate directory
   - Test with various mod types and configurations

5. **Debugging**
   - Use MO2's logging system for debugging
   - Add debug print statements in the plugin
   - Test with simple mods before complex ones

## Technical Constraints

1. **MO2 Compatibility**
   - Must work with the current stable version of MO2
   - Should maintain compatibility with future MO2 updates
   - Should follow MO2's plugin architecture and conventions

2. **Performance Considerations**
   - Should not significantly impact MO2's performance
   - Must handle large mod collections efficiently
   - Should minimize resource usage when idle
   - May need optimization for handling dual modding systems

3. **File System Constraints**
   - Must work with MO2's virtual file system (USVFS)
   - Must handle both traditional Bethesda mod files and UE5 assets
   - Must map files to the correct directories:
     - Traditional mods to `OblivionRemastered\Content\Dev\ObvData\Data`
     - UE5 mods to `OblivionRemastered\Content\Paks\~mods`
   - Must respect file permissions and handle errors gracefully

4. **UI Constraints**
   - Any custom UI elements must follow MO2's UI design
   - Should integrate seamlessly with MO2's existing UI
   - Must provide clear indicators for mod types
   - Must be responsive and user-friendly

## Dependencies

### External Dependencies

1. **Mod Organizer 2**
   - Core application that hosts the plugin
   - Provides the plugin API and infrastructure
   - Version compatibility is critical

2. **basic_games Framework**
   - Provides the base classes and utilities for game support
   - Must be compatible with the version used

3. **Oblivion Remaster**
   - The game itself, which the plugin needs to support
   - File structure and modding approach may change with updates
   - May require adaptation to different versions

### Internal Dependencies

1. **Python Plugin Dependencies**
   - basic_games framework
   - Python standard library
   - MO2's Python API
   - PyQt for UI components (if needed)

## Tool Usage Patterns

1. **Version Control**
   - Git for source code management
   - GitHub or similar for collaboration and issue tracking
   - Semantic versioning for releases

2. **Deployment**
   - Manual installation for development and testing
   - Potential integration with MO2's plugin installer
   - Distribution through Nexus Mods or GitHub

3. **Testing**
   - Manual testing with different mod configurations
   - Testing with both traditional and UE5 mods
   - Testing with hybrid mods (containing both types)
   - Testing with different versions of Oblivion Remaster
   - Community testing for broader coverage

## Documentation Approach

1. **Code Documentation**
   - Inline comments for complex code sections
   - Function and class documentation following Python docstring conventions
   - README and other documentation files for high-level overview

2. **User Documentation**
   - Installation and setup instructions
   - Usage guidelines for end users
   - Explanation of dual modding system
   - Visual guides for different mod types
   - Troubleshooting information

3. **Maintenance Documentation**
   - Architecture overview
   - Design decisions and rationale
   - Future development plans
   - Update procedures for game patches

## File Structure and Organization

The plugin will be organized as follows:

```
game_oblivionremastered.py       # Main plugin file
oblivionremastered/              # Supporting modules
├── __init__.py
├── installer.py                 # Custom installer logic
├── plugin_manager.py            # Plugin management
├── ue5_manager.py               # UE5 asset management
└── features/                    # Custom features
    ├── __init__.py
    ├── save_game_info.py
    └── ini_manager.py
```

This structure separates concerns and makes the code more maintainable.

## Development Resources

1. **MO2 Documentation**
   - [MO2 Wiki](https://github.com/ModOrganizer2/modorganizer/wiki)
   - [basic_games Documentation](https://github.com/ModOrganizer2/modorganizer-basic_games)

2. **Reference Implementations**
   - Other game plugins in the basic_games repository
   - Existing Bethesda game plugins (Skyrim, Oblivion)

3. **Oblivion Remaster Resources**
   - Game file structure documentation
   - Nexus Mods page for Oblivion Remaster
   - Community modding guides

4. **Unreal Engine 5 Modding Resources**
   - UE5 modding documentation
   - Community resources on .pak file structure and loading
