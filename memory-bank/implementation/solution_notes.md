# Oblivion Remastered Plugin Solution Notes

## Current Implementation

We have implemented a basic MO2 plugin for Oblivion Remastered using the BasicGames framework. The plugin provides support for the game's dual modding system, handling both traditional Bethesda mods (.esp/.bsa) and Unreal Engine 5 mods (.pak/.ucas/.utoc).

### Core Components

1. **OblivionRemasteredGame Class**
   - Inherits from BasicGame
   - Defines game-specific properties and paths
   - Implements game detection and basic integration with MO2

2. **OblivionRemasteredSaveGame Class**
   - Handles save game information
   - Extracts player name and other metadata from save files
   - Provides formatted save game names for display in MO2

3. **OblivionRemasteredModDataChecker Class**
   - Validates and fixes mod structure
   - Detects mod type (traditional, UE5, or hybrid)
   - Ensures files are placed in the correct directories

### Key Features

1. **Dual Modding System Support**
   - Traditional Bethesda mods (.esp/.bsa) are placed in `OblivionRemastered/Content/Dev/ObvData/Data`
   - UE5 mods (.pak/.ucas/.utoc) are placed in `OblivionRemastered/Content/Paks/~mods`
   - Hybrid mods are split into their respective directories

2. **Save Game Handling**
   - Detects and displays save games
   - Extracts player name and other metadata
   - Supports profile-specific saves

3. **INI File Management**
   - Handles game INI files
   - Supports profile-specific INI settings
   - Manages multiple INI files in different locations

4. **Mod Type Detection**
   - Analyzes file extensions and directory structure
   - Determines whether a mod is traditional, UE5, or hybrid
   - Ensures proper file placement

## Implementation Details

### Game Detection and Setup

```python
class OblivionRemasteredGame(BasicGame):
    Name = "Oblivion Remastered Support Plugin"
    Author = "Mrowr Purr"
    Version = "1.0.0"
    
    GameName = "The Elder Scrolls IV: Oblivion Remastered"
    GameShortName = "OblivionRemastered"
    GameNexusName = "oblivionremastered"
    GameNexusId = 7587
    GameSteamId = 2623190
    GameBinary = "OblivionRemastered.exe"
    GameLauncher = "OblivionRemastered.exe"
    GameDataPath = "OblivionRemastered/Content"
    GameIniFiles = ["Oblivion.ini", "Oblivion_default.ini", "BlendSettings.ini"]
    GameDocumentsDirectory = "%GAME_PATH%/OblivionRemastered/Content/Dev/ObvData"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%USERPROFILE%\\Documents\\My Games\\Oblivion Remastered\\Saved\\SaveGames"
```

### Mod Data Checking

The `OblivionRemasteredModDataChecker` class is responsible for validating and fixing mod structure. It detects the mod type based on file extensions and directory structure, then ensures files are placed in the correct directories.

```python
class OblivionRemasteredModDataChecker(mobase.ModDataChecker):
    def __init__(self):
        super().__init__()
        # UE5 file extensions
        self.ue5_extensions = [".pak", ".ucas", ".utoc", ".uasset", ".uexp", ".ubulk", ".umap"]
        # Bethesda file extensions
        self.bethesda_extensions = [".esp", ".bsa"]
        # INI files
        self.ini_files = ["blendsettings.ini", "oblivion.ini", "oblivion_default.ini"]
    
    def dataLooksValid(self, filetree):
        # Always return FIXABLE to ensure the fix method is called
        return mobase.ModDataChecker.FIXABLE
    
    def fix(self, filetree):
        # Restructure the mod based on file types
        # UE5 files go to Paks/~mods/
        # Bethesda files go to Dev/ObvData/Data/
        # INI files go to Dev/ObvData/
        # ... implementation details ...
        return fixed_filetree
```

### Save Game Handling

The `OblivionRemasteredSaveGame` class handles save game information, extracting player name and other metadata from save files.

```python
class OblivionRemasteredSaveGame(BasicGameSaveGame):
    def __init__(self, filepath, player_name=None):
        super().__init__(filepath)
        self._player_name = player_name
    
    def allFiles(self):
        # Only return the save file itself, no PNG files
        return [self._filepath.name]
    
    def playerName(self):
        return self._player_name
    
    def getName(self):
        # Format the save game name for display
        # ... implementation details ...
        return formatted_name
```

### Plugin Management

The plugin includes methods for reading and writing the Plugins.txt file, which is used to manage traditional Bethesda mods.

```python
def readPluginsList(self):
    # Read the Plugins.txt file
    plugins_path = os.path.join(
        self.gameDirectory().absolutePath(),
        "OblivionRemastered", "Content", "Dev", "ObvData", "Data", "Plugins.txt"
    )
    # ... implementation details ...
    return plugins

def writePluginsList(self, plugins):
    # Write the Plugins.txt file
    plugins_path = os.path.join(
        self.gameDirectory().absolutePath(),
        "OblivionRemastered", "Content", "Dev", "ObvData", "Data", "Plugins.txt"
    )
    # ... implementation details ...
```

### Mod State Change Detection

The plugin attempts to detect when mods are enabled or disabled using the `onModStateChanged` callback.

```python
def init(self, organizer):
    super().init(organizer)
    self._organizer = organizer
    
    # Register features
    self._register_feature(OblivionRemasteredModDataChecker())
    self._register_feature(BasicGameSaveGameInfo())
    self._register_feature(BasicLocalSavegames(self.savesDirectory()))
    
    # Register callback for mod state changes
    try:
        self._organizer.modList().onModStateChanged(self._onModStateChanged)
    except Exception as e:
        # Handle error
    
    return True

def _onModStateChanged(self, mod_states):
    # Handle mod state changes
    # Update Plugins.txt
    # ... implementation details ...
```

## Current Limitations and Issues

1. **Plugins.txt Not Being Updated**
   - The Plugins.txt file is not being automatically updated when mods are enabled or disabled
   - This means users must manually update the Plugins.txt file or use a workaround

2. **Mod State Change Detection Not Working**
   - The `onModStateChanged` callback is not being triggered or is not working as expected
   - This prevents automatic updates of the Plugins.txt file

3. **Logging Challenges**
   - Standard print statements are not being captured by MO2's logging system
   - Custom logging to a file is being used as a workaround

4. **UE5 Load Order Management**
   - UE5 mods are loaded alphabetically, which limits control
   - No custom load order management has been implemented yet

5. **Hybrid Mod Handling**
   - Mods containing both traditional and UE5 components may not be handled optimally
   - Further testing and refinement is needed

## Next Steps

1. **Fix Plugins.txt Update Issue**
   - Investigate why the Plugins.txt file is not being updated
   - Implement a workaround if necessary

2. **Improve Mod State Change Detection**
   - Investigate why the `onModStateChanged` callback is not working
   - Explore alternative approaches for detecting mod state changes

3. **Enhance Logging**
   - Improve logging to better diagnose issues
   - Explore integration with MO2's logging system

4. **Implement UE5 Load Order Management**
   - Develop a system for controlling UE5 mod load order
   - Consider a prefix system or metadata-based approach

5. **Refine Hybrid Mod Handling**
   - Improve detection and handling of hybrid mods
   - Test with various mod configurations

6. **Add User Interface Enhancements**
   - Add mod type indicators
   - Implement filters for different mod types
   - Enhance conflict visualization for the dual modding system

7. **Comprehensive Testing**
   - Test with various mod configurations
   - Test with different combinations of traditional and UE5 mods
   - Optimize performance
   - Refine user experience
