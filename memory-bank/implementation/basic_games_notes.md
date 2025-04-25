# BasicGames Framework Notes

## Overview

The BasicGames framework is a Python-based system for creating game plugins for Mod Organizer 2 (MO2). It provides a simplified way to add support for new games without having to write a full C++ plugin. The framework is particularly useful for games that follow standard modding patterns and don't require deep integration with MO2's core.

## Core Components

### BasicGame Class

The `BasicGame` class is the foundation of the framework. It implements the `IPluginGame` interface and provides default implementations for many methods. Game plugins typically inherit from this class and override specific methods as needed.

```python
class MyGamePlugin(BasicGame):
    Name = "My Game Plugin"
    Author = "Author Name"
    Version = "1.0.0"
    
    GameName = "My Game"
    GameShortName = "mygame"
    GameBinary = "MyGame.exe"
    GameDataPath = "Data"
    # ... other game-specific properties
```

### Key Properties

- **Name**: The name of the plugin
- **Author**: The author of the plugin
- **Version**: The version of the plugin
- **GameName**: The full name of the game
- **GameShortName**: A short identifier for the game
- **GameNexusName**: The name used on Nexus Mods
- **GameNexusId**: The game ID on Nexus Mods
- **GameSteamId**: The game ID on Steam
- **GameBinary**: The main executable file
- **GameDataPath**: The path to the game's data directory
- **GameDocumentsDirectory**: The path to the game's documents directory
- **GameSavesDirectory**: The path to the game's saves directory
- **GameIniFiles**: List of INI files used by the game

### Important Methods

- **init(organizer)**: Called when the plugin is initialized
- **initializeProfile(directory, settings)**: Called when a profile is created or reset
- **executables()**: Returns a list of executables for the game
- **listSaves(folder)**: Lists save games in the specified folder
- **savesDirectory()**: Returns the directory containing save games
- **dataDirectory()**: Returns the directory containing game data

## Features System

The BasicGames framework uses a feature system to extend functionality. Features are registered with the game plugin and provide additional capabilities.

### Common Features

1. **BasicGameSaveGameInfo**
   - Provides save game handling
   - Extracts information from save files
   - Displays save game information in MO2

2. **BasicLocalSavegames**
   - Enables profile-specific save games
   - Manages save game directories for each profile

3. **ModDataChecker**
   - Validates mod structure
   - Can fix mod structure issues
   - Ensures mods are installed correctly

### Registering Features

Features are registered in the `init` method of the game plugin:

```python
def init(self, organizer):
    super().init(organizer)
    self._organizer = organizer
    self._register_feature(MyCustomFeature())
    return True
```

## File System Handling

### Virtual File System Mapping

The BasicGames framework maps files from mods to their virtual locations in the game directory. This is controlled by the `GameDataPath` property and custom file mapping logic.

### Mod Data Checking

The `ModDataChecker` feature allows plugins to validate and fix mod structure. This is particularly useful for games with specific mod organization requirements.

```python
class MyGameModDataChecker(ModDataChecker):
    def dataLooksValid(self, filetree):
        # Check if the mod structure is valid
        return ModDataChecker.FIXABLE
    
    def fix(self, filetree):
        # Fix the mod structure
        return fixed_filetree
```

## Callback System

The BasicGames framework provides access to MO2's callback system through the `IOrganizer` interface. This allows plugins to respond to events like mod state changes.

### Key Callbacks

1. **onModStateChanged**
   - Called when mods are enabled or disabled
   - Provides a map of mod names to their states
   - Used for updating plugin lists and other state-dependent features

2. **onProfileChanged**
   - Called when the active profile changes
   - Used for updating profile-specific features

### Implementation Example

```python
def init(self, organizer):
    super().init(organizer)
    self._organizer = organizer
    self._organizer.modList().onModStateChanged(self._onModStateChanged)
    return True

def _onModStateChanged(self, mod_states):
    # Handle mod state changes
    for mod_name, state in mod_states.items():
        is_active = state & mobase.ModState.ACTIVE
        # Do something with this information
```

## INI File Management

The BasicGames framework provides support for managing game INI files. This includes profile-specific INI files and INI tweaks.

### Key Properties

- **GameIniFiles**: List of INI files used by the game
- **GameDocumentsDirectory**: The path to the game's documents directory (where INI files are typically stored)

### Profile-Specific INI Files

When a profile is created or reset, the `initializeProfile` method is called. This method can copy INI files from the game directory to the profile directory, allowing for profile-specific INI settings.

```python
def initializeProfile(self, directory, settings):
    if settings & mobase.ProfileSetting.CONFIGURATION:
        # Copy INI files to the profile directory
        for ini_file in self.GameIniFiles:
            source_path = os.path.join(self.gameDirectory().absolutePath(), ini_file)
            target_path = os.path.join(directory.absolutePath(), ini_file)
            shutil.copyfile(source_path, target_path)
    super().initializeProfile(directory, settings)
```

## Limitations and Challenges

### Limited Access to MO2 Core

The BasicGames framework provides a simplified interface to MO2's core functionality. This can be limiting for games that require deep integration or custom features.

### Performance Overhead

Python plugins may have a performance overhead compared to native C++ plugins. This is usually not significant for most games, but can be a consideration for performance-critical features.

### Callback Reliability

The callback system in MO2 is designed for C++ plugins. Python plugins can use it, but there may be issues with callback reliability, especially for complex callbacks or those that need to modify MO2's state.

### Debugging Challenges

Debugging Python plugins can be challenging, as MO2's debugging tools are primarily designed for C++ plugins. Custom logging and error handling are often necessary for effective debugging.

## Best Practices

1. **Follow Existing Patterns**
   - Study existing game plugins for patterns and best practices
   - Reuse code where appropriate
   - Maintain consistency with MO2's design philosophy

2. **Robust Error Handling**
   - Use try/except blocks to catch exceptions
   - Log errors with meaningful messages
   - Fail gracefully when errors occur

3. **Comprehensive Testing**
   - Test with various mod configurations
   - Test with different game versions
   - Test with different MO2 versions

4. **Clear Documentation**
   - Document code with clear docstrings
   - Provide high-level architecture documentation
   - Include examples for complex functionality
