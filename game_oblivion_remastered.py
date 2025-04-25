import os

import mobase
from PyQt6.QtCore import QDir, QFileInfo

from ..basic_game import BasicGame


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
                except Exception as e:
                    print(f"Error checking file {entry.name() if entry else 'unknown'}: {str(e)}")
        return False
    
    def fix(self, filetree: mobase.IFileTree) -> mobase.IFileTree:
        """
        Restructure the mod to put files in the correct directories.
        This method is called when dataLooksValid returns FIXABLE.
        """
        # Print a debug message to confirm the fix method is being called
        print(f"OblivionRemasteredModDataChecker.fix: Restructuring mod {filetree.name()}")
        
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
                except Exception as e:
                    print(f"Error checking directory {entry.name() if entry else 'unknown'}: {str(e)}")
        
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
            except Exception as e:
                print(f"Error processing UE5 files: {str(e)}")
        
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
            except Exception as e:
                print(f"Error processing Bethesda files: {str(e)}")
        
        return filetree


class OblivionRemasteredGame(BasicGame):
    Name = "Oblivion Remastered Support Plugin"
    Author = "MO2 Community"
    Version = "1.0.0"
    
    GameName = "The Elder Scrolls IV: Oblivion Remastered"
    GameShortName = "oblivionremastered"
    GameNexusName = "oblivionremastered"
    GameNexusId = 7587
    GameSteamId = 2623190
    # Use the UE5 shipping executable
    GameBinary = "OblivionRemastered/Binaries/Win64/OblivionRemastered-Win64-Shipping.exe"
    GameLauncher = "OblivionRemastered.exe"
    # Use the UE5 mods directory as the data path
    GameDataPath = "OblivionRemastered/Content"
    # GameDataPath = "OblivionRemastered/Content/Paks/~mods"
    GameIniFiles = ["Oblivion.ini", "Oblivion_default.ini", "BlendSettings.ini"]
    GameDocumentsDirectory = "%GAME_PATH%/OblivionRemastered/Content/Dev/ObvData"
    GameSaveExtension = "sav"
    
    def init(self, organizer: mobase.IOrganizer):
        super().init(organizer)
        self._register_feature(OblivionRemasteredModDataChecker())
        return True
    
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
    
    def savesDirectory(self):
        return os.path.join(
            os.environ["USERPROFILE"], 
            "Documents", "My Games", "Oblivion Remastered", "Saved", "SaveGames"
        )
    
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
            
        super().initializeProfile(directory, settings)


def createPlugin():
    return OblivionRemasteredGame()
