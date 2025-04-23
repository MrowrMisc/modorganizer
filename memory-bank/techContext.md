# Technical Context: MO2 Plugin for Oblivion Remaster

## Technologies Used

### Core Technologies

1. **C++** - For native plugin development
   - Used by MO2's core and most game plugins
   - Required for deep integration with MO2's systems
   - Provides optimal performance for complex operations

2. **Python** - For basic_games plugin development
   - Used by the basic_games framework
   - Easier to develop and maintain than C++
   - Suitable for simpler game plugins

3. **Qt** - For UI components
   - Used by MO2 for its user interface
   - Required for any custom UI elements in the plugin
   - Version used by MO2: Qt 5/6 (depending on MO2 version)

4. **CMake** - For build system
   - Used to build MO2 and its native plugins
   - Manages dependencies and build configuration

### MO2-Specific Technologies

1. **USVFS (User Space Virtual File System)**
   - Core technology behind MO2's mod virtualization
   - Allows mods to be installed in separate directories
   - Maps files from mod directories to the game directory at runtime

2. **Plugin Interfaces**
   - `IPluginGame` - Base interface for game plugins
   - `GameGamebryo` - Base class for Bethesda game plugins
   - `BasicGame` - Base class for Python-based game plugins

3. **MO2 API**
   - Provides access to MO2's core functionality
   - Includes interfaces for mod management, profile management, etc.
   - Available to both C++ and Python plugins

### Game-Specific Technologies

1. **Bethesda Plugin System**
   - .esp/.esm file format
   - Load order management
   - Plugin dependencies and rules

2. **Unreal Engine 5**
   - .pak file format for asset packaging
   - Asset management and loading
   - Mod integration with UE5 systems

## Development Setup

### For Native C++ Plugin Development

1. **Required Tools**
   - Visual Studio 2019 or later (for Windows)
   - CMake 3.16 or later
   - Qt 5/6 development tools
   - Git for version control

2. **Build Environment**
   - MO2 uses a build system called "mob" for managing dependencies
   - Alternative: Manual setup of dependencies and build environment

3. **Development Workflow**
   - Clone the modorganizer-game_gamebryo repository as a base
   - Create a new repository for the Oblivion Remaster plugin
   - Implement the required interfaces and functionality
   - Build and test with MO2

### For Python Plugin Development

1. **Required Tools**
   - Python 3.8 or later
   - Text editor or IDE with Python support
   - Git for version control

2. **Development Environment**
   - Clone the modorganizer-basic_games repository
   - Create a new game plugin file in the games directory
   - Implement the required functionality

3. **Development Workflow**
   - Implement a class that inherits from BasicGame
   - Define game-specific properties and behavior
   - Test by placing the plugin in MO2's plugins directory

## Technical Constraints

1. **MO2 Compatibility**
   - Must work with the current stable version of MO2
   - Should maintain compatibility with future MO2 updates
   - Should follow MO2's plugin architecture and conventions

2. **Performance Considerations**
   - Should not significantly impact MO2's performance
   - Must handle large mod collections efficiently
   - Should minimize resource usage when idle

3. **File System Constraints**
   - Must work with MO2's virtual file system (USVFS)
   - Must handle both traditional Bethesda mod files and UE assets
   - Must respect file permissions and handle errors gracefully

4. **UI Constraints**
   - Any custom UI elements must follow MO2's UI design
   - Should integrate seamlessly with MO2's existing UI
   - Must be responsive and user-friendly

## Dependencies

### External Dependencies

1. **Mod Organizer 2**
   - Core application that hosts the plugin
   - Provides the plugin API and infrastructure
   - Version compatibility is critical

2. **Oblivion Remaster**
   - The game itself, which the plugin needs to support
   - File structure and modding approach may change with updates
   - May require adaptation to different versions

### Internal Dependencies

1. **For Native C++ Plugin**
   - GameGamebryo base class
   - MO2 core libraries
   - Qt libraries for UI components

2. **For Python Plugin**
   - basic_games framework
   - Python standard library
   - MO2's Python API

## Tool Usage Patterns

1. **Version Control**
   - Git for source code management
   - GitHub or similar for collaboration and issue tracking
   - Semantic versioning for releases

2. **Build and Deployment**
   - CMake for building native plugins
   - Manual installation or installer for distribution
   - Testing in different MO2 environments

3. **Testing**
   - Manual testing with different mod configurations
   - Testing with different versions of Oblivion Remaster
   - Community testing for broader coverage

## Documentation Approach

1. **Code Documentation**
   - Inline comments for complex code sections
   - Function and class documentation following MO2's conventions
   - README and other documentation files for high-level overview

2. **User Documentation**
   - Installation and setup instructions
   - Usage guidelines for end users
   - Troubleshooting information

3. **Maintenance Documentation**
   - Architecture overview
   - Design decisions and rationale
   - Future development plans
