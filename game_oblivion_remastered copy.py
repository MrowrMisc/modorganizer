import os

import mobase
from PyQt6.QtCore import QDir, QFileInfo

from ..basic_game import BasicGame


class OblivionRemasteredModDataChecker(mobase.ModDataChecker):
    """
    Accept all mods regardless of structure to prevent MO2 from complaining.
    """
    def dataLooksValid(self, filetree: mobase.IFileTree) -> mobase.ModDataChecker.CheckReturn:
        # Always return VALID to accept any mod structure
        return mobase.ModDataChecker.VALID


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
