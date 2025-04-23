Nexus IDs:

- Oblivion Remastered is GameNexusId `7587` and GameNexusName `oblivionremastered`
- Oblivion (original) is GameNexusId `101` and GameNexusName `oblivion`

# Thoughts for: MO2 Plugin for Oblivion Remaster

Ok, so I'll let you know how the Oblivion Remaster works.

## Original Oblivion game

So, in the original Oblivion, here's where the game is:
- D:\SteamLibrary\steamapps\common\Oblivion

Note: I have mine in SteamLibrary, but it's usually C:\Program Files (x86)\Steam\steamapps\common\Oblivion

Ok, and so the Data folder is a very special folder, and for me it's at:
- D:\SteamLibrary\steamapps\common\Oblivion\Data

And for most people it'll be located at:
- C:\Program Files (x86)\Steam\steamapps\common\Oblivion\Data

Ok, so that's the Oblivion folder, for the "OG" original Oblivion.

It has files in it like this:

```
Music/
Shaders/
Textures/
Video/
Credits.txt
DLCBattlehornCastle.bsa
DLCBattlehornCastle.esp
DLCFrostcrag.bsa
DLCFrostcrag.esp
DLCHorseArmor.bsa
DLCHorseArmor.esp
DLCList.txt
DLCMehrunesRazor.esp
DLCOrrery.bsa
DLCOrrery.esp
DLCShiveringIsles - Meshes.bsa
DLCShiveringIsles - Sounds.bsa
DLCShiveringIsles - Textures.bsa
DLCShiveringIsles - Voices.bsa
DLCShiveringIsles.esp
DLCSpellTomes.esp
DLCThievesDen.bsa
DLCThievesDen.esp
DLCVileLair.bsa
DLCVileLair.esp
Knights.bsa
Knights.esp
Oblivion - Invalidation.bsa
Oblivion - Meshes.bsa
Oblivion - Misc.bsa
Oblivion - Sounds.bsa
Oblivion - Textures - Compressed.bsa
Oblivion - Voices1.bsa
Oblivion - Voices2.bsa
Oblivion.esm
```

So that's my Oblivion game of the year edition with all the DLC etc.

Ok, cool, right?

And note my root Steam folder for games is at D:\SteamLibrary\steamapps\common
and remember that it's usually at C:\Program Files (x86)\Steam\steamapps\common

## Oblivion Remastered game

When installed from Steam, Oblivion Remaster lives here on my PC:

- D:\SteamLibrary\steamapps\common\Oblivion Remastered

Now, it's a Unreal Engine 5 game and I can tell that there are 2x main projects because
this is what the top level folder looks like:

This shows ALL the contents of the 2x subfoldrs:
- Engine
- OblivionRemastered

I think this is standard for all UE5 games maybe and the Engine is just the UE5 engine
and everything we really care about is in the OblivionRemastered folder.

Here's ALL the files under the "D:\SteamLibrary\steamapps\common\Oblivion Remastered" folder:

```
 Oblivion Remastered ◉
> tree.com /a /f
Folder PATH listing for volume Data
Volume serial number is 0A6B-6BDD
D:.
|   OblivionRemastered.exe
|
+---Engine
|   +---Binaries
|   |   +---ThirdParty
|   |   |   +---CEF3
|   |   |   |   \---Win64
|   |   |   |       |   chrome_elf.dll
|   |   |   |       |   d3dcompiler_47.dll
|   |   |   |       |   icudtl.dat
|   |   |   |       |   libcef.dll
|   |   |   |       |   libEGL.dll
|   |   |   |       |   libGLESv2.dll
|   |   |   |       |   snapshot_blob.bin
|   |   |   |       |   v8_context_snapshot.bin
|   |   |   |       |
|   |   |   |       \---Resources
|   |   |   |           |   chrome_100_percent.pak
|   |   |   |           |   chrome_200_percent.pak
|   |   |   |           |   icudtl.dat
|   |   |   |           |   resources.pak
|   |   |   |           |
|   |   |   |           +---locales
|   |   |   |           |       am.pak
|   |   |   |           |       ar.pak
|   |   |   |           |       bg.pak
|   |   |   |           |       bn.pak
|   |   |   |           |       ca.pak
|   |   |   |           |       cs.pak
|   |   |   |           |       da.pak
|   |   |   |           |       de.pak
|   |   |   |           |       el.pak
|   |   |   |           |       en-GB.pak
|   |   |   |           |       en-US.pak
|   |   |   |           |       es-419.pak
|   |   |   |           |       es.pak
|   |   |   |           |       et.pak
|   |   |   |           |       fa.pak
|   |   |   |           |       fi.pak
|   |   |   |           |       fil.pak
|   |   |   |           |       fr.pak
|   |   |   |           |       gu.pak
|   |   |   |           |       he.pak
|   |   |   |           |       hi.pak
|   |   |   |           |       hr.pak
|   |   |   |           |       hu.pak
|   |   |   |           |       id.pak
|   |   |   |           |       it.pak
|   |   |   |           |       ja.pak
|   |   |   |           |       kn.pak
|   |   |   |           |       ko.pak
|   |   |   |           |       lt.pak
|   |   |   |           |       lv.pak
|   |   |   |           |       ml.pak
|   |   |   |           |       mr.pak
|   |   |   |           |       ms.pak
|   |   |   |           |       nb.pak
|   |   |   |           |       nl.pak
|   |   |   |           |       pl.pak
|   |   |   |           |       pt-BR.pak
|   |   |   |           |       pt-PT.pak
|   |   |   |           |       ro.pak
|   |   |   |           |       ru.pak
|   |   |   |           |       sk.pak
|   |   |   |           |       sl.pak
|   |   |   |           |       sr.pak
|   |   |   |           |       sv.pak
|   |   |   |           |       sw.pak
|   |   |   |           |       ta.pak
|   |   |   |           |       te.pak
|   |   |   |           |       th.pak
|   |   |   |           |       tr.pak
|   |   |   |           |       uk.pak
|   |   |   |           |       vi.pak
|   |   |   |           |       zh-CN.pak
|   |   |   |           |       zh-TW.pak
|   |   |   |           |
|   |   |   |           \---swiftshader
|   |   |   |                   libEGL.dll
|   |   |   |                   libGLESv2.dll
|   |   |   |
|   |   |   +---DbgHelp
|   |   |   |       dbghelp.dll
|   |   |   |
|   |   |   +---MsQuic
|   |   |   |   \---v220
|   |   |   |       \---win64
|   |   |   |               msquic.dll
|   |   |   |
|   |   |   +---NVIDIA
|   |   |   |   \---NVaftermath
|   |   |   |       \---Win64
|   |   |   |               GFSDK_Aftermath_Lib.x64.dll
|   |   |   |
|   |   |   +---Ogg
|   |   |   |   \---Win64
|   |   |   |       \---VS2015
|   |   |   |               libogg_64.dll
|   |   |   |
|   |   |   +---Steamworks
|   |   |   |   \---Steamv153
|   |   |   |       \---Win64
|   |   |   |               steam_api64.dll
|   |   |   |
|   |   |   +---Vorbis
|   |   |   |   \---Win64
|   |   |   |       \---VS2015
|   |   |   |               libvorbisfile_64.dll
|   |   |   |               libvorbis_64.dll
|   |   |   |
|   |   |   \---Windows
|   |   |       \---XAudio2_9
|   |   |           \---x64
|   |   |                   xaudio2_9redist.dll
|   |   |
|   |   \---Win64
|   |           CrashReportClient.exe
|   |           EOSSDK-Win64-Shipping.dll
|   |           EpicWebHelper.exe
|   |           tbb.dll
|   |           tbb.pdb
|   |           tbbmalloc.dll
|   |           tbbmalloc.pdb
|   |
|   +---Content
|   |   +---Slate
|   |   |   \---Cursor
|   |   |           invisible.cur
|   |   |
|   |   \---SlateDebug
|   |       \---Fonts
|   |               LastResort.tps
|   |               LastResort.ttf
|   |
|   +---Extras
|   |   \---Redist
|   |       \---en-us
|   |               UEPrereqSetup_x64.exe
|   |
|   +---Plugins
|   |   \---Marketplace
|   |       +---nvidia
|   |       |   \---DLSS
|   |       |       +---DLSS
|   |       |       |   \---Binaries
|   |       |       |       \---ThirdParty
|   |       |       |           \---Win64
|   |       |       |                   nvngx_dlss.dll
|   |       |       |
|   |       |       \---Streamline
|   |       |           \---Binaries
|   |       |               \---ThirdParty
|   |       |                   \---Win64
|   |       |                           nvngx_deepdvc.dll
|   |       |                           nvngx_dlssg.dll
|   |       |                           sl.common.dll
|   |       |                           sl.deepdvc.dll
|   |       |                           sl.dlss_g.dll
|   |       |                           sl.interposer.dll
|   |       |                           sl.pcl.dll
|   |       |                           sl.reflex.dll
|   |       |
|   |       \---XeSS
|   |           \---Binaries
|   |               \---ThirdParty
|   |                   \---Win64
|   |                           libxess.dll
|   |
|   \---Programs
|       \---CrashReportClient
|           \---Content
|               \---Paks
|                       CrashReportClient.pak
|
\---OblivionRemastered
    +---Binaries
    |   \---Win64
    |       |   amd_fidelityfx_dx12.dll
    |       |   OblivionRemastered-Win64-Shipping.exe
    |       |   OpenImageDenoise.dll
    |       |   tbb.dll
    |       |   tbb.pdb
    |       |   tbb12.dll
    |       |   tbbmalloc.dll
    |       |   tbbmalloc.pdb
    |       |
    |       \---D3D12
    |               D3D12Core.dll
    |
    +---Content
    |   +---Dev
    |   |   +---DebugUI
    |   |   |       DebugMenu.txt
    |   |   |
    |   |   +---LevelSelectDoors
    |   |   |   \---Config
    |   |   |           LevelSelectDoors.txt
    |   |   |
    |   |   +---ObvData
    |   |   |   |   BlendSettings.ini
    |   |   |   |   Oblivion.ini
    |   |   |   |   Oblivion_default.ini
    |   |   |   |
    |   |   |   \---Data
    |   |   |       |   AltarDeluxe.bsa
    |   |   |       |   AltarDeluxe.esp
    |   |   |       |   AltarESPMain.bsa
    |   |   |       |   AltarESPMain.esp
    |   |   |       |   AltarGymNavigation.esp
    |   |   |       |   Barrels.esp
    |   |   |       |   Credits.txt
    |   |   |       |   DLCBattlehornCastle.bsa
    |   |   |       |   DLCBattlehornCastle.esp
    |   |   |       |   DLCFrostcrag.bsa
    |   |   |       |   DLCFrostcrag.esp
    |   |   |       |   DLCHorseArmor.bsa
    |   |   |       |   DLCHorseArmor.esp
    |   |   |       |   DLCList.txt
    |   |   |       |   DLCMehrunesRazor.esp
    |   |   |       |   DLCOrrery.bsa
    |   |   |       |   DLCOrrery.esp
    |   |   |       |   DLCShiveringIsles - Meshes.bsa
    |   |   |       |   DLCShiveringIsles - Sounds.bsa
    |   |   |       |   DLCShiveringIsles - Textures.bsa
    |   |   |       |   DLCShiveringIsles - Voices.bsa
    |   |   |       |   DLCShiveringIsles.esp
    |   |   |       |   DLCSpellTomes.esp
    |   |   |       |   DLCThievesDen.bsa
    |   |   |       |   DLCThievesDen.esp
    |   |   |       |   DLCVileLair.bsa
    |   |   |       |   DLCVileLair.esp
    |   |   |       |   GymNavigationDisable.bat
    |   |   |       |   GymNavigationEnable.bat
    |   |   |       |   Knights.bsa
    |   |   |       |   Knights.esp
    |   |   |       |   Oblivion - Meshes.bsa
    |   |   |       |   Oblivion - Misc.bsa
    |   |   |       |   Oblivion - Sounds.bsa
    |   |   |       |   Oblivion - Textures - Compressed.bsa
    |   |   |       |   Oblivion - Voices1.bsa
    |   |   |       |   Oblivion - Voices2.bsa
    |   |   |       |   Oblivion.esm
    |   |   |       |   OverPoweredArrows.esp
    |   |   |       |   Plugins.txt
    |   |   |       |   SuperSpells.esp
    |   |   |       |   TamrielLeveledRegion.esp
    |   |   |       |
    |   |   |       +---LSData
    |   |   |       |       DtC6dal.dat
    |   |   |       |       DtC6dl.dat
    |   |   |       |       Wt16M9bs.dat
    |   |   |       |       Wt16M9fs.dat
    |   |   |       |       Wt8S9bs.dat
    |   |   |       |       Wt8S9fs.dat
    |   |   |       |
    |   |   |       +---Menus
    |   |   |       |   |   birthsign_menu.xml
    |   |   |       |   |   book_menu.xml
    |   |   |       |   |   breath_meter_menu.xml
    |   |   |       |   |   container_menu.xml
    |   |   |       |   |   levelup_menu.xml
    |   |   |       |   |   loading_bar_ingame_menu.xml
    |   |   |       |   |   loading_ingame_menu.xml
    |   |   |       |   |   loading_menu.xml
    |   |   |       |   |   lockpick_menu.xml
    |   |   |       |   |   menu_labels.txt
    |   |   |       |   |   message_menu.xml
    |   |   |       |   |   negotiate_menu.xml
    |   |   |       |   |   quantity_menu.xml
    |   |   |       |   |   recharge_menu.xml
    |   |   |       |   |   repair_menu.xml
    |   |   |       |   |   sleep_wait_menu.xml
    |   |   |       |   |   strings.xml
    |   |   |       |   |   training_menu.xml
    |   |   |       |   |
    |   |   |       |   +---CharGen
    |   |   |       |   |       attributes_menu.xml
    |   |   |       |   |       class_menu.xml
    |   |   |       |   |       race_sex_menu.xml
    |   |   |       |   |       skills_menu.xml
    |   |   |       |   |       specilization_menu.xml
    |   |   |       |   |
    |   |   |       |   +---Dialog
    |   |   |       |   |       Alchemy.xml
    |   |   |       |   |       dialog_menu.xml
    |   |   |       |   |       Enchantment.xml
    |   |   |       |   |       enchantmentsetting_menu.xml
    |   |   |       |   |       persuasion_menu.xml
    |   |   |       |   |       SigilStone.xml
    |   |   |       |   |       Spellmaking.xml
    |   |   |       |   |       spell_purchase.xml
    |   |   |       |   |       TextEditMenu.xml
    |   |   |       |   |
    |   |   |       |   +---Generic
    |   |   |       |   |       quest_added.xml
    |   |   |       |   |       skill_perk.xml
    |   |   |       |   |
    |   |   |       |   +---Main
    |   |   |       |   |       hud_info_menu.xml
    |   |   |       |   |       hud_main_menu.xml
    |   |   |       |   |       hud_reticle.xml
    |   |   |       |   |       hud_subtitle_menu.xml
    |   |   |       |   |       inventory_menu.xml
    |   |   |       |   |       magic_menu.xml
    |   |   |       |   |       magic_popup_menu.xml
    |   |   |       |   |       map_menu.xml
    |   |   |       |   |       player_model.xml
    |   |   |       |   |       quickkeys_menu.xml
    |   |   |       |   |       safe_zone.xml
    |   |   |       |   |       stats_menu.xml
    |   |   |       |   |
    |   |   |       |   +---Options
    |   |   |       |   |       audio_menu.xml
    |   |   |       |   |       controls_menu.xml
    |   |   |       |   |       credits_menu.xml
    |   |   |       |   |       downloads_menu.xml
    |   |   |       |   |       gameplay_menu.xml
    |   |   |       |   |       load_menu.xml
    |   |   |       |   |       main_menu.xml
    |   |   |       |   |       options_menu.xml
    |   |   |       |   |       pause_menu.xml
    |   |   |       |   |       save_menu.xml
    |   |   |       |   |       video_display_menu.xml
    |   |   |       |   |       video_menu.xml
    |   |   |       |   |       xcontrols_menu.xml
    |   |   |       |   |
    |   |   |       |   \---Prefabs
    |   |   |       |           button_floating.xml
    |   |   |       |           button_floating_2.xml
    |   |   |       |           button_floating_3.xml
    |   |   |       |           button_long.xml
    |   |   |       |           button_no_background.xml
    |   |   |       |           button_short.xml
    |   |   |       |           button_xtralong.xml
    |   |   |       |           fill_bar.xml
    |   |   |       |           focus_box.xml
    |   |   |       |           generic_background.xml
    |   |   |       |           horizontal_scroll.xml
    |   |   |       |           horiz_floating_scroll.xml
    |   |   |       |           item_listing.xml
    |   |   |       |           page_tab.xml
    |   |   |       |           scroll_line.xml
    |   |   |       |           skill_item.xml
    |   |   |       |           tile_button.xml
    |   |   |       |           tile_button_over.xml
    |   |   |       |           vertical_scroll.xml
    |   |   |       |           vert_floating_scroll.xml
    |   |   |       |           xbox_floating_hint.xml
    |   |   |       |
    |   |   |       +---Music
    |   |   |       |   +---Battle
    |   |   |       |   |       battle_01.mp3
    |   |   |       |   |       battle_02.mp3
    |   |   |       |   |       battle_03.mp3
    |   |   |       |   |       battle_04.mp3
    |   |   |       |   |       battle_05.mp3
    |   |   |       |   |       battle_06.mp3
    |   |   |       |   |       battle_07.mp3
    |   |   |       |   |       battle_08.mp3
    |   |   |       |   |
    |   |   |       |   +---Dungeon
    |   |   |       |   |       Dungeon_01_v2.mp3
    |   |   |       |   |       dungeon_02.mp3
    |   |   |       |   |       dungeon_03.mp3
    |   |   |       |   |       dungeon_04.mp3
    |   |   |       |   |       dungeon_05.mp3
    |   |   |       |   |
    |   |   |       |   +---Explore
    |   |   |       |   |       atmosphere_01.mp3
    |   |   |       |   |       atmosphere_03.mp3
    |   |   |       |   |       atmosphere_04.mp3
    |   |   |       |   |       atmosphere_06.mp3
    |   |   |       |   |       atmosphere_07.mp3
    |   |   |       |   |       atmosphere_08.mp3
    |   |   |       |   |       atmosphere_09.mp3
    |   |   |       |   |
    |   |   |       |   +---Public
    |   |   |       |   |       town_01.mp3
    |   |   |       |   |       town_02.mp3
    |   |   |       |   |       town_03.mp3
    |   |   |       |   |       town_04.mp3
    |   |   |       |   |       town_05.mp3
    |   |   |       |   |
    |   |   |       |   \---Special
    |   |   |       |           death.mp3
    |   |   |       |           success.mp3
    |   |   |       |           tes4title.mp3
    |   |   |       |
    |   |   |       +---Shaders
    |   |   |       |       shaderpackage001.sdp
    |   |   |       |       shaderpackage002.sdp
    |   |   |       |       shaderpackage003.sdp
    |   |   |       |       shaderpackage004.sdp
    |   |   |       |       shaderpackage005.sdp
    |   |   |       |       shaderpackage006.sdp
    |   |   |       |       shaderpackage007.sdp
    |   |   |       |       shaderpackage008.sdp
    |   |   |       |       shaderpackage009.sdp
    |   |   |       |       shaderpackage010.sdp
    |   |   |       |       shaderpackage011.sdp
    |   |   |       |       shaderpackage012.sdp
    |   |   |       |       shaderpackage013.sdp
    |   |   |       |       shaderpackage014.sdp
    |   |   |       |       shaderpackage015.sdp
    |   |   |       |       shaderpackage016.sdp
    |   |   |       |       shaderpackage017.sdp
    |   |   |       |       shaderpackage018.sdp
    |   |   |       |       shaderpackage019.sdp
    |   |   |       |
    |   |   |       \---Textures
    |   |   |           \---Effects
    |   |   |                   TerrainNoise.dds
    |   |   |
    |   |   \---ObvData - Original
    |   |       |   BlendSettings.ini
    |   |       |   Oblivion.ini
    |   |       |   Oblivion_default.ini
    |   |       |
    |   |       \---Data
    |   |           |   AltarDeluxe.bsa
    |   |           |   AltarDeluxe.esp
    |   |           |   AltarESPMain.bsa
    |   |           |   AltarESPMain.esp
    |   |           |   AltarGymNavigation.esp
    |   |           |   Credits.txt
    |   |           |   DLCBattlehornCastle.bsa
    |   |           |   DLCBattlehornCastle.esp
    |   |           |   DLCFrostcrag.bsa
    |   |           |   DLCFrostcrag.esp
    |   |           |   DLCHorseArmor.bsa
    |   |           |   DLCHorseArmor.esp
    |   |           |   DLCList.txt
    |   |           |   DLCMehrunesRazor.esp
    |   |           |   DLCOrrery.bsa
    |   |           |   DLCOrrery.esp
    |   |           |   DLCShiveringIsles - Meshes.bsa
    |   |           |   DLCShiveringIsles - Sounds.bsa
    |   |           |   DLCShiveringIsles - Textures.bsa
    |   |           |   DLCShiveringIsles - Voices.bsa
    |   |           |   DLCShiveringIsles.esp
    |   |           |   DLCSpellTomes.esp
    |   |           |   DLCThievesDen.bsa
    |   |           |   DLCThievesDen.esp
    |   |           |   DLCVileLair.bsa
    |   |           |   DLCVileLair.esp
    |   |           |   GymNavigationDisable.bat
    |   |           |   GymNavigationEnable.bat
    |   |           |   Knights.bsa
    |   |           |   Knights.esp
    |   |           |   Oblivion - Meshes.bsa
    |   |           |   Oblivion - Misc.bsa
    |   |           |   Oblivion - Sounds.bsa
    |   |           |   Oblivion - Textures - Compressed.bsa
    |   |           |   Oblivion - Voices1.bsa
    |   |           |   Oblivion - Voices2.bsa
    |   |           |   Oblivion.esm
    |   |           |   Plugins.txt
    |   |           |   TamrielLeveledRegion.esp
    |   |           |
    |   |           +---LSData
    |   |           |       DtC6dal.dat
    |   |           |       DtC6dl.dat
    |   |           |       Wt16M9bs.dat
    |   |           |       Wt16M9fs.dat
    |   |           |       Wt8S9bs.dat
    |   |           |       Wt8S9fs.dat
    |   |           |
    |   |           +---Menus
    |   |           |   |   birthsign_menu.xml
    |   |           |   |   book_menu.xml
    |   |           |   |   breath_meter_menu.xml
    |   |           |   |   container_menu.xml
    |   |           |   |   levelup_menu.xml
    |   |           |   |   loading_bar_ingame_menu.xml
    |   |           |   |   loading_ingame_menu.xml
    |   |           |   |   loading_menu.xml
    |   |           |   |   lockpick_menu.xml
    |   |           |   |   menu_labels.txt
    |   |           |   |   message_menu.xml
    |   |           |   |   negotiate_menu.xml
    |   |           |   |   quantity_menu.xml
    |   |           |   |   recharge_menu.xml
    |   |           |   |   repair_menu.xml
    |   |           |   |   sleep_wait_menu.xml
    |   |           |   |   strings.xml
    |   |           |   |   training_menu.xml
    |   |           |   |
    |   |           |   +---CharGen
    |   |           |   |       attributes_menu.xml
    |   |           |   |       class_menu.xml
    |   |           |   |       race_sex_menu.xml
    |   |           |   |       skills_menu.xml
    |   |           |   |       specilization_menu.xml
    |   |           |   |
    |   |           |   +---Dialog
    |   |           |   |       Alchemy.xml
    |   |           |   |       dialog_menu.xml
    |   |           |   |       Enchantment.xml
    |   |           |   |       enchantmentsetting_menu.xml
    |   |           |   |       persuasion_menu.xml
    |   |           |   |       SigilStone.xml
    |   |           |   |       Spellmaking.xml
    |   |           |   |       spell_purchase.xml
    |   |           |   |       TextEditMenu.xml
    |   |           |   |
    |   |           |   +---Generic
    |   |           |   |       quest_added.xml
    |   |           |   |       skill_perk.xml
    |   |           |   |
    |   |           |   +---Main
    |   |           |   |       hud_info_menu.xml
    |   |           |   |       hud_main_menu.xml
    |   |           |   |       hud_reticle.xml
    |   |           |   |       hud_subtitle_menu.xml
    |   |           |   |       inventory_menu.xml
    |   |           |   |       magic_menu.xml
    |   |           |   |       magic_popup_menu.xml
    |   |           |   |       map_menu.xml
    |   |           |   |       player_model.xml
    |   |           |   |       quickkeys_menu.xml
    |   |           |   |       safe_zone.xml
    |   |           |   |       stats_menu.xml
    |   |           |   |
    |   |           |   +---Options
    |   |           |   |       audio_menu.xml
    |   |           |   |       controls_menu.xml
    |   |           |   |       credits_menu.xml
    |   |           |   |       downloads_menu.xml
    |   |           |   |       gameplay_menu.xml
    |   |           |   |       load_menu.xml
    |   |           |   |       main_menu.xml
    |   |           |   |       options_menu.xml
    |   |           |   |       pause_menu.xml
    |   |           |   |       save_menu.xml
    |   |           |   |       video_display_menu.xml
    |   |           |   |       video_menu.xml
    |   |           |   |       xcontrols_menu.xml
    |   |           |   |
    |   |           |   \---Prefabs
    |   |           |           button_floating.xml
    |   |           |           button_floating_2.xml
    |   |           |           button_floating_3.xml
    |   |           |           button_long.xml
    |   |           |           button_no_background.xml
    |   |           |           button_short.xml
    |   |           |           button_xtralong.xml
    |   |           |           fill_bar.xml
    |   |           |           focus_box.xml
    |   |           |           generic_background.xml
    |   |           |           horizontal_scroll.xml
    |   |           |           horiz_floating_scroll.xml
    |   |           |           item_listing.xml
    |   |           |           page_tab.xml
    |   |           |           scroll_line.xml
    |   |           |           skill_item.xml
    |   |           |           tile_button.xml
    |   |           |           tile_button_over.xml
    |   |           |           vertical_scroll.xml
    |   |           |           vert_floating_scroll.xml
    |   |           |           xbox_floating_hint.xml
    |   |           |
    |   |           +---Music
    |   |           |   +---Battle
    |   |           |   |       battle_01.mp3
    |   |           |   |       battle_02.mp3
    |   |           |   |       battle_03.mp3
    |   |           |   |       battle_04.mp3
    |   |           |   |       battle_05.mp3
    |   |           |   |       battle_06.mp3
    |   |           |   |       battle_07.mp3
    |   |           |   |       battle_08.mp3
    |   |           |   |
    |   |           |   +---Dungeon
    |   |           |   |       Dungeon_01_v2.mp3
    |   |           |   |       dungeon_02.mp3
    |   |           |   |       dungeon_03.mp3
    |   |           |   |       dungeon_04.mp3
    |   |           |   |       dungeon_05.mp3
    |   |           |   |
    |   |           |   +---Explore
    |   |           |   |       atmosphere_01.mp3
    |   |           |   |       atmosphere_03.mp3
    |   |           |   |       atmosphere_04.mp3
    |   |           |   |       atmosphere_06.mp3
    |   |           |   |       atmosphere_07.mp3
    |   |           |   |       atmosphere_08.mp3
    |   |           |   |       atmosphere_09.mp3
    |   |           |   |
    |   |           |   +---Public
    |   |           |   |       town_01.mp3
    |   |           |   |       town_02.mp3
    |   |           |   |       town_03.mp3
    |   |           |   |       town_04.mp3
    |   |           |   |       town_05.mp3
    |   |           |   |
    |   |           |   \---Special
    |   |           |           death.mp3
    |   |           |           success.mp3
    |   |           |           tes4title.mp3
    |   |           |
    |   |           +---Shaders
    |   |           |       shaderpackage001.sdp
    |   |           |       shaderpackage002.sdp
    |   |           |       shaderpackage003.sdp
    |   |           |       shaderpackage004.sdp
    |   |           |       shaderpackage005.sdp
    |   |           |       shaderpackage006.sdp
    |   |           |       shaderpackage007.sdp
    |   |           |       shaderpackage008.sdp
    |   |           |       shaderpackage009.sdp
    |   |           |       shaderpackage010.sdp
    |   |           |       shaderpackage011.sdp
    |   |           |       shaderpackage012.sdp
    |   |           |       shaderpackage013.sdp
    |   |           |       shaderpackage014.sdp
    |   |           |       shaderpackage015.sdp
    |   |           |       shaderpackage016.sdp
    |   |           |       shaderpackage017.sdp
    |   |           |       shaderpackage018.sdp
    |   |           |       shaderpackage019.sdp
    |   |           |
    |   |           \---Textures
    |   |               \---Effects
    |   |                       TerrainNoise.dds
    |   |
    |   +---Legal
    |   |   \---BGS
    |   |           Notice.txt
    |   |
    |   +---Movies
    |   |   |   ShaderLoadingScreen.mp4
    |   |   |
    |   |   \---Modern
    |   |       |   Altar_Menu_BGS_Logo_16x9.bk2
    |   |       |   Altar_Menu_Virtuos_Logo_16x9.bk2
    |   |       |   Ignite_21_9_H264.bk2
    |   |       |   Intro_21_9.bk2
    |   |       |   Loop_21_9_H264.bk2
    |   |       |   Outro_21_9.bk2
    |   |       |
    |   |       \---HelpMenu
    |   |               HelpMenu_Blocking.bk2
    |   |               HelpMenu_Clairvoyance.bk2
    |   |               HelpMenu_Crime.bk2
    |   |               HelpMenu_Crosshair.bk2
    |   |               HelpMenu_Dodging.bk2
    |   |               HelpMenu_Fatigue.bk2
    |   |               HelpMenu_Horses.bk2
    |   |               HelpMenu_Jail.bk2
    |   |               HelpMenu_LevelingUp.bk2
    |   |               HelpMenu_Lockpicking.bk2
    |   |               HelpMenu_MeleeAttacks.bk2
    |   |               HelpMenu_Movement.bk2
    |   |               HelpMenu_Persuasion.bk2
    |   |               HelpMenu_Pickpocket.bk2
    |   |               HelpMenu_RangedAttacks.bk2
    |   |               HelpMenu_ShieldBash.bk2
    |   |               HelpMenu_SoulTrap.bk2
    |   |               HelpMenu_Swimming.bk2
    |   |
    |   \---Paks
    |           global.ucas
    |           global.utoc
    |           OblivionRemastered-Windows.pak
    |           OblivionRemastered-Windows.ucas
    |           OblivionRemastered-Windows.utoc
    |
    \---Plugins
        \---Wwise
            \---ThirdParty
                \---x64_vc170
                    \---Release
                        \---bin
                                Ak3DAudioBedMixer.dll
                                AkAudioInput.dll
                                AkCompressor.dll
                                AkDelay.dll
                                AkExpander.dll
                                AkFlanger.dll
                                AkGain.dll
                                AkGuitarDistortion.dll
                                AkHarmonizer.dll
                                AkImpacter.dll
                                AkMatrixReverb.dll
                                AkMotion.dll
                                AkParametricEQ.dll
                                AkPeakLimiter.dll
                                AkPitchShifter.dll
                                AkRecorder.dll
                                AkReflect.dll
                                AkRoomVerb.dll
                                AkSilenceGenerator.dll
                                AkSineTone.dll
                                AkSoundEngineDLL.dll
                                AkStereoDelay.dll
                                AkSynthOne.dll
                                AkTimeStretch.dll
                                AkToneGen.dll
                                AkTremolo.dll
                                iZotope.dll
                                MasteringSuite.dll
```

I think we can learn a LOT from this.

But, when it comes to modding ... there are really 2x main things that I see...

### Modding using classic Oblivion files and techniques

See how the .esp and .bsa files are there?

Modders have checked the MD5 hashes of these files and they are the same as the original Oblivion files.

It's likely based on what we understand about the game (which I've played!)
that the data files area read, all the way down to the meshes and stuff,
and that's what the Unreal Engine 5 engine uses to load up the game.

Likely with lots of complex Unreal Engine 5 stuff for ... well, lots! To make it work well.

Here's where Oblivion.ini lives:

D:\SteamLibrary\steamapps\common\Oblivion Remastered\OblivionRemastered\Content\Dev\ObvData\Oblivion.ini

So! Here's the "Data" folder for the "Oblivion Remastered" game:

- D:\SteamLibrary\steamapps\common\Oblivion Remastered\OblivionRemastered\Content\Dev\ObvData\Data

The data folder has this stuff:

```
LSData/
Menus/
Music/
Shaders/
Textures/
AltarDeluxe.bsa
AltarDeluxe.esp
AltarESPMain.bsa
AltarESPMain.esp
AltarGymNavigation.esp
Barrels.esp
Credits.txt
DLCBattlehornCastle.bsa
DLCBattlehornCastle.esp
DLCFrostcrag.bsa
DLCFrostcrag.esp
DLCHorseArmor.bsa
DLCHorseArmor.esp
DLCList.txt
DLCMehrunesRazor.esp
DLCOrrery.bsa
DLCOrrery.esp
DLCShiveringIsles - Meshes.bsa
DLCShiveringIsles - Sounds.bsa
DLCShiveringIsles - Textures.bsa
DLCShiveringIsles - Voices.bsa
DLCShiveringIsles.esp
DLCSpellTomes.esp
DLCThievesDen.bsa
DLCThievesDen.esp
DLCVileLair.bsa
DLCVileLair.esp
GymNavigationDisable.bat
GymNavigationEnable.bat
Knights.bsa
Knights.esp
Oblivion - Meshes.bsa
Oblivion - Misc.bsa
Oblivion - Sounds.bsa
Oblivion - Textures - Compressed.bsa
Oblivion - Voices1.bsa
Oblivion - Voices2.bsa
Oblivion.esm
OverPoweredArrows.esp
Plugins.txt
SuperSpells.esp
TamrielLeveledRegion.esp
```

So!

I have two ideas ...

#### One: Modding the game with the official "Oblivion Remastered" game game_id from Nexus

There are mods shared on the Oblivion Remastered Nexus page.

The game is really new so there isn't yet necessarily a decided upon structure for mod files.

The most common thing in MO2 is to have the files in the .zip/.7z/.rar mod file
be mounted via usvfs into the "Data" folder of the game

And we have a Data folder, so that's possible.

And installation instructions for those mods look something like this:

```
- Download the main file
- Extract the main file archive into "The Elder Scrolls IV- Oblivion Remastered\Content\OblivionRemastered\Content\Dev\ObvData\Data"
- Open "Plugins.txt" file located in "The Elder Scrolls IV- Oblivion Remastered\Content\OblivionRemastered\Content\Dev\ObvData\Data"
- Add "Difficulty Slider Fixed.esp" to the bottom of the text file
```

Because that Data\ folder also has a plugins.txt file which is just a list of .esp files to load in order.

BUT ... that only handles mods which tweak the Oblivion original Data and add .esp and .bsa and so on

LOTS of the mods that come out for The Oblivion Remaster will be Unreal Engine 5 based mods and will be
files of types such as .pak .ucas .utoc and so on

Installation instructions for these might look like:

```
Unzip three 000_SmallerCompass_P (differ up to version) files from archive to this game folder: Oblivion Remastered\OblivionRemastered\Content\Paks\~mods.
```

I guess there's a `~mods` folder in the Paks folder? Is this UE5 standard?

#### Two: Modding the game with the original "Oblivion" game game_id from Nexus

Lots of original Oblivion mods should work out-of-the-box with the Oblivion Remaster.

And it could be cool to run MO2 and trick it into seeing Oblivion Remaster as the original Oblivion game.

This could be useful. But... let's call it an edge case for now...

It would be read, but let's focus on the main 2x focus areas: supporting the Remaster with mods that could really replace ANY files from the D:\SteamLibrary\steamapps\common\Oblivion Remastered\OblivionRemastered folder like in D:\SteamLibrary\steamapps\common\Oblivion Remastered\OblivionRemastered\Content ... Content is kinda the "Data" of UE5 mods I guess!

I'm thinking the usvfs mounted folder should be that Content folder!

And .esp mods would next their files in the .zip/.7z/.rar files like so:

- Dev\ObvData\Data\MyCool.esp
- Dev\ObvData\Data\MyCool.bsa

And Pak mods would put their files in the .zip/.7z/.rar files like so:

- Paks\~mods\MyCool.pak
- Paks\~mods\MyCool.ucas
- Paks\~mods\MyCool.utoc


### Modding using Unreal Engine 5 files and techniques

I actually added my notes on this above lol.
