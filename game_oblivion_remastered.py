import os
from pathlib import Path

import mobase
from PyQt6.QtCore import QDir, QFileInfo

from ..basic_features import BasicGameSaveGameInfo
from ..basic_features.basic_save_game_info import BasicGameSaveGame
from ..basic_game import BasicGame


class OblivionRemasteredSaveGame(BasicGameSaveGame):
    def __init__(self, filepath: Path, player_name=None):
        super().__init__(filepath)
        self._player_name = player_name
    
    def allFiles(self):
        # Only return the save file itself, no PNG files
        return [self._filepath.name]
    
    def playerName(self):
        return self._player_name
    
    def getName(self) -> str:
        """Return a nicely formatted name for the save game."""
        filename = self._filepath.name
        
        # Handle quicksave
        if filename.lower() == "quicksave.sav":
            return "Quicksave"
        
        # Handle special files
        if filename.lower() == "save_settings.sav":
            return "Settings"
        if filename.lower() == "saves_meta.sav":
            return "Metadata"
        
        # Handle autosaves: "autosave 1 - Panasia (71EB9234-42E7-D26D-B359-F58580130EA4).sav"
        if filename.lower().startswith("autosave"):
            try:
                import re
                # Extract save number and character name
                match = re.search(r'autosave (\d+) - (.+?) \(', filename)
                if match:
                    save_num = match.group(1)
                    char_name = match.group(2)
                    return f"Auto {save_num} - {char_name}"
                else:
                    return filename.replace(".sav", "")
            except Exception:
                return filename.replace(".sav", "")
        
        # Handle manual saves: "Save 7, Playing Time 01.11.51 - Panasia - LOC_FN_AnvilHeinrichOakenHallsHouseSecondFloor, Level 1.sav"
        if filename.lower().startswith("save"):
            try:
                import re
                # Extract save number, time, character name, and location
                match = re.search(r'Save (\d+), Playing Time (.+?) - (.+?) - (.+?), Level', filename)
                if match:
                    save_num = match.group(1)
                    play_time = match.group(2)
                    char_name = match.group(3)
                    location = match.group(4)
                    
                    # Simplify location name
                    location = location.replace("LOC_FN_", "")
                    # Remove numbers from location
                    location = re.sub(r'\d+', '', location)
                    # Convert CamelCase to spaces
                    location = re.sub(r'([a-z])([A-Z])', r'\1 \2', location)
                    
                    return f"Save {save_num} - {char_name} - {location}"
                else:
                    return filename.replace(".sav", "")
            except Exception:
                return filename.replace(".sav", "")
        
        # Default case
        return filename.replace(".sav", "")


class OblivionRemasteredModDataChecker(mobase.ModDataChecker):
    """
    Accept all mods regardless of structure to prevent MO2 from complaining.
    Also restructures mods to put files in the correct directories.
    """
    def __init__(self):
        super().__init__()
        # UE5 file extensions that should go in Paks/~mods/[mod name]
        self.ue5_extensions = [".pak", ".ucas", ".utoc", ".uasset", ".uexp", ".ubulk", ".umap"]
        # Bethesda file extensions that should go in Dev/ObvData/Data
        self.bethesda_extensions = [".esp", ".bsa"]
        # INI files that should go in Dev/ObvData
        self.ini_files = ["blendsettings.ini", "oblivion.ini", "oblivion_default.ini"]
    
    def dataLooksValid(self, filetree: mobase.IFileTree) -> mobase.ModDataChecker.CheckReturn:
        # Always return FIXABLE to ensure the fix method is called
        return mobase.ModDataChecker.FIXABLE
    
    def _contains_ue5_files(self, directory: mobase.IFileTree) -> bool:
        """
        Check if a directory contains UE5 files.
        """
        if directory is None:
            return False
            
        for entry in directory:
            if entry is not None and entry.isFile():
                try:
                    file_name = entry.name().lower()
                    file_ext = os.path.splitext(file_name)[1].lower()
                    if file_ext in self.ue5_extensions:
                        return True
                except Exception:
                    pass
        return False
    
    def fix(self, filetree: mobase.IFileTree) -> mobase.IFileTree:
        """
        Restructure the mod to put files in the correct directories.
        This method is called when dataLooksValid returns FIXABLE.
        """
        # Restructure the mod
        
        # Check for UE5 files in the root
        ue5_files_in_root = []
        for entry in filetree:
            if entry is not None and entry.isFile():
                file_name = entry.name().lower()
                file_ext = os.path.splitext(file_name)[1].lower()
                if file_ext in self.ue5_extensions:
                    ue5_files_in_root.append(entry)
        
        # Check for directories in the root that contain UE5 files
        ue5_dirs_in_root = []
        for entry in filetree:
            if entry is not None and entry.isDir():
                try:
                    if self._contains_ue5_files(entry):
                        ue5_dirs_in_root.append(entry)
                except Exception:
                    pass
        
        # Check for Bethesda files in the root
        bethesda_files_in_root = []
        for entry in filetree:
            if entry is not None and entry.isFile():
                file_name = entry.name().lower()
                file_ext = os.path.splitext(file_name)[1].lower()
                if file_ext in self.bethesda_extensions:
                    bethesda_files_in_root.append(entry)
        
        # Check for INI files in the root
        ini_files_in_root = []
        for entry in filetree:
            if entry is not None and entry.isFile():
                file_name = entry.name().lower()
                if file_name in self.ini_files:
                    ini_files_in_root.append(entry)
        
        # Always restructure the mod, even if we didn't find any specific files to move
        # This ensures that the fix method is always applied
        
        # Create the necessary directories for UE5 files
        if ue5_files_in_root or ue5_dirs_in_root:
            try:
                paks_dir = filetree.addDirectory("Paks")
                mods_dir = paks_dir.addDirectory("~mods")
                
                # Move UE5 files directly to Paks/~mods/
                if ue5_files_in_root:
                    for entry in ue5_files_in_root:
                        if entry is not None:
                            mods_dir.insert(entry, mobase.IFileTree.InsertPolicy.REPLACE)
                
                # Move directories containing UE5 files to Paks/~mods/[dir name]
                for dir_entry in ue5_dirs_in_root:
                    if dir_entry is not None:
                        dir_name = dir_entry.name()
                        target_dir = mods_dir.addDirectory(dir_name)
                        
                        # Collect all files first to avoid issues with modifying the directory while iterating
                        files_to_move = []
                        for file_entry in dir_entry:
                            if file_entry is not None:
                                files_to_move.append(file_entry)
                        
                        # Now process all files
                        for file_entry in files_to_move:
                            # Insert the file directly into the target directory
                            target_dir.insert(file_entry, mobase.IFileTree.InsertPolicy.REPLACE)
            except Exception:
                pass
        
        # Create the necessary directories for Bethesda files and INI files
        if bethesda_files_in_root or ini_files_in_root:
            try:
                dev_dir = filetree.addDirectory("Dev")
                obvdata_dir = dev_dir.addDirectory("ObvData")
                
                # Move INI files to Dev/ObvData
                for entry in ini_files_in_root:
                    if entry is not None:
                        obvdata_dir.insert(entry, mobase.IFileTree.InsertPolicy.REPLACE)
                
                # Create Data directory and move Bethesda files there
                if bethesda_files_in_root:
                    data_dir = obvdata_dir.addDirectory("Data")
                    for entry in bethesda_files_in_root:
                        if entry is not None:
                            data_dir.insert(entry, mobase.IFileTree.InsertPolicy.REPLACE)
            except Exception:
                pass
        
        return filetree


class OblivionRemasteredGame(BasicGame):
    Name = "Oblivion Remastered Support Plugin"
    Author = "MO2 Community"
    Version = "1.0.0"
    
    GameName = "The Elder Scrolls IV: Oblivion Remastered"
    GameShortName = "OblivionRemastered"
    GameNexusName = "oblivionremastered"
    GameNexusId = 7587
    GameSteamId = 2623190
    # Use the UE5 shipping executable
    GameBinary = "OblivionRemastered.exe"
    GameLauncher = "OblivionRemastered.exe"
    # Use the UE5 mods directory as the data path
    GameDataPath = "OblivionRemastered/Content"
    # GameDataPath = "OblivionRemastered/Content/Paks/~mods"
    GameIniFiles = ["Oblivion.ini", "Oblivion_default.ini", "BlendSettings.ini"]
    GameDocumentsDirectory = "%GAME_PATH%/OblivionRemastered/Content/Dev/ObvData"
    GameSaveExtension = "sav"
    GameSavesDirectory = "%USERPROFILE%\\Documents\\My Games\\Oblivion Remastered\\Saved\\SaveGames"
    
    # No need for GameIniPath, we'll use GameDocumentsDirectory instead
    
    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._organizer = organizer
        self._register_feature(OblivionRemasteredModDataChecker())
        
        # Register BasicGameSaveGameInfo without looking for PNG files
        self._register_feature(BasicGameSaveGameInfo())
        
        # Add BasicLocalSavegames feature for profile-specific saves
        from ..basic_features import BasicLocalSavegames
        self._register_feature(BasicLocalSavegames(self.savesDirectory()))
        
        try:
            # Access paths to ensure they're initialized
            self.documentsDirectory().absolutePath()
            self.savesDirectory().absolutePath()
            self.gameDirectory().absolutePath()
            self.dataDirectory().absolutePath()
        except Exception:
            pass
        
        return True
    
    def _extract_player_name(self, filename: str):
        """Extract player name from save filename."""
        try:
            import re
            # For autosaves: "autosave 1 - dhfr (ID).sav"
            autosave_match = re.search(r'- (.+?) \(', filename)
            if autosave_match:
                return autosave_match.group(1).strip()
            
            # For manual saves: "Save 1, Playing Time 00.00.38 - dasd - LOC_FN_ImperialDungeon01, Level 1.sav"
            manual_save_match = re.search(r'Time .+? - (.+?) -', filename)
            if manual_save_match:
                return manual_save_match.group(1).strip()
            
            return None
        except Exception:
            return None
    
    def documentsDirectory(self):
        """Override the documents directory method to explicitly point to the correct path for INI files."""
        # This is where MO2 will look for INI files
        return QDir(os.path.join(self.gameDirectory().absolutePath(), "OblivionRemastered", "Content", "Dev", "ObvData"))
    
    def savesDirectory(self):
        """Override the saves directory method to explicitly point to the correct path."""
        try:
            docs_dir = self.documentsDirectory().absolutePath()
            saves_path = f"{docs_dir}/Saved/SaveGames"
            return QDir(saves_path)
        except Exception:
            return super().savesDirectory()
    
    # Set the correct paths for INI files
    # The GameDocumentsDirectory is where MO2 will look for the INI files
    GameDocumentsDirectory = "%GAME_PATH%/OblivionRemastered/Content/Dev/ObvData"
    
    # The GameIniFiles is a list of INI file names that MO2 will look for in the GameDocumentsDirectory
    GameIniFiles = ["Oblivion.ini", "Oblivion_default.ini", "BlendSettings.ini"]
    
    def listSaves(self, folder: QDir) -> list[mobase.ISaveGame]:
        """List save games from the provided folder directory.
        
        When profile-specific saves are enabled, folder will be the profile's save directory.
        When profile-specific saves are disabled, folder will be the game's save directory.
        """
        ext = self._mappings.savegameExtension.get()
        
        # Use the provided folder parameter, which will be the profile's save directory
        # when profile-specific saves are enabled
        folder_path = Path(folder.absolutePath())
        
        # Get current profile name - we'll simply use the profile name as the expected player name
        profile_name = self._organizer.profile().name()
        
        # Check if we're using profile-specific saves
        using_profile_saves = folder_path.name == "saves"
        
        # If we're using profile-specific saves but the folder doesn't exist or is empty,
        # we might need to copy saves from the game directory to the profile directory
        if using_profile_saves and (not folder_path.exists() or not any(folder_path.glob(f"*.{ext}"))):
            # Create the directory if it doesn't exist
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
            
            # We could copy saves from the game directory to the profile directory here,
            # but for now we'll just return an empty list
            return []
        
        # Check if the directory exists
        if not folder_path.exists():
            return []
            
        # Find all save files
        all_save_files = list(folder_path.glob(f"*.{ext}"))
        
        # Filter out system files that should be hidden
        hidden_files = ["saves_meta.sav", "save_settings.sav"]
        filtered_save_files = [f for f in all_save_files if f.name.lower() not in [h.lower() for h in hidden_files]]
        
        # Create objects for all saves and extract their player names
        all_saves = []
        for save_path in filtered_save_files:
            save_file_player = self._extract_player_name(save_path.name)
            all_saves.append(OblivionRemasteredSaveGame(save_path, save_file_player))
        
        # If no profile name is set, return all saves
        if not profile_name:
            return all_saves
        
        # Filter saves by player name matching profile name
        # This is a simplification - users need to name their characters the same as their profile
        filtered_saves = []
        for save in all_saves:
            player_name = save.playerName()
            if player_name and player_name.lower() == profile_name.lower():
                filtered_saves.append(save)
        
        # If no saves match the profile name, show all saves as a fallback
        if not filtered_saves:
            return all_saves
        
        return filtered_saves
    
    def executables(self):
        return [
            mobase.ExecutableInfo(
                "Oblivion Remastered",
                QFileInfo(self.gameDirectory().absoluteFilePath(self.binaryName()))
            ),
            mobase.ExecutableInfo(
                "Oblivion Remastered (Launcher)",
                QFileInfo(self.gameDirectory().absoluteFilePath(self.GameLauncher))
            )
        ]
    
    def initializeProfile(self, directory: QDir, settings: mobase.ProfileSetting):
        # Create the mods directories if they don't exist
        ue5_mods_path = os.path.join(
            self.gameDirectory().absolutePath(), "OblivionRemastered", "Content", "Paks", "~mods"
        )
        bethesda_mods_path = os.path.join(
            self.gameDirectory().absolutePath(), "OblivionRemastered", "Content", "Dev", "ObvData", "Data"
        )
        
        if not os.path.exists(ue5_mods_path):
            os.makedirs(ue5_mods_path, exist_ok=True)
            
        if not os.path.exists(bethesda_mods_path):
            os.makedirs(bethesda_mods_path, exist_ok=True)
        
        # Create the saves directory in the profile if it doesn't exist
        # Always create the saves directory, regardless of profile settings
        saves_path = os.path.join(directory.absolutePath(), "saves")
        if not os.path.exists(saves_path):
            os.makedirs(saves_path, exist_ok=True)
            
        super().initializeProfile(directory, settings)


def createPlugin():
    return OblivionRemasteredGame()
