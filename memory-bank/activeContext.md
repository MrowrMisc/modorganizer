# Active Context: MO2 Plugin for Oblivion Remaster

## Current Work Focus

We are currently in the **planning and initial implementation phase** of developing an MO2 plugin for Oblivion Remaster. The main focus areas are:

1. **Implementing the Python-based Plugin**
   - Using the basic_games framework for better portability and flexibility
   - Creating the core plugin structure
   - Implementing custom features for the dual modding system

2. **Handling the Dual Modding System**
   - Implementing support for traditional Bethesda mods (.esp/.bsa)
   - Implementing support for Unreal Engine 5 mods (.pak/.ucas/.utoc)
   - Creating a unified interface for managing both mod types

3. **Developing Custom Installers**
   - Creating mod type detection logic
   - Implementing proper file placement for each mod type
   - Handling hybrid mods that contain both traditional and UE5 components

## Recent Changes

We have made significant progress in understanding the requirements and planning the implementation:

1. **Analyzed Oblivion Remaster's File Structure**
   - Identified the game installation path: `[Steam Library]\steamapps\common\Oblivion Remastered`
   - Located the traditional Bethesda mod files path: `OblivionRemastered\Content\Dev\ObvData\Data`
   - Located the UE5 mod files path: `OblivionRemastered\Content\Paks\~mods`
   - Identified relevant configuration files: `OblivionRemastered\Content\Dev\ObvData\Oblivion.ini` and others

2. **Researched Modding Approaches**
   - Confirmed that traditional Bethesda mods use .esp/.bsa files and are managed via Plugins.txt
   - Confirmed that UE5 mods use .pak/.ucas/.utoc files and are loaded alphabetically from the ~mods folder
   - Identified that some mods might contain both traditional and UE5 components

3. **Decided on Implementation Approach**
   - Selected Python-based approach using the basic_games framework
   - Designed a system for handling the dual modding nature
   - Planned custom features for mod type detection and proper file placement

4. **Created Comprehensive Documentation**
   - Established the project brief with specific requirements
   - Documented the product context and user experience goals
   - Outlined the system architecture and key components
   - Documented the technical context and development setup
   - Created a detailed implementation plan

## Next Steps

The immediate next steps in the project are:

1. **Implement Core Plugin Structure**
   - Create the main `OblivionRemasteredGame` class
   - Define game-specific properties and paths
   - Set up basic game detection

2. **Develop Mod Type Detection**
   - Create logic to identify traditional vs. UE5 mods
   - Implement file extension and structure analysis
   - Handle hybrid mods that contain both types

3. **Implement Custom Installer**
   - Create the `OblivionRemasteredInstaller` class
   - Implement proper file placement for each mod type
   - Test with various mod formats

4. **Implement Plugin Management**
   - Create the `OblivionRemasteredPluginManager` class
   - Implement Plugins.txt handling for traditional mods
   - Develop load order management for both mod types

5. **Add INI File Support**
   - Configure relevant .ini files
   - Set up profile-specific .ini handling
   - Test with different game configurations

6. **Enhance User Interface**
   - Add mod type indicators
   - Implement filters for different mod types
   - Improve conflict visualization for the dual modding system

7. **Testing and Refinement**
   - Test with various mod configurations
   - Optimize performance
   - Refine user experience

## Active Decisions and Considerations

### Decision: Python Implementation via basic_games

**Status**: Decided

**Decision**: Use the Python-based basic_games framework rather than a native C++ plugin.

**Rationale**:
- **Portability**: Python plugins are more portable across different systems
- **Flexibility**: Easier to adapt to changes in the game or modding approach
- **Development Speed**: Faster to develop and iterate on
- **User Preference**: The user has expressed a preference for Python

**Implementation Plan**:
- Create a new game plugin file in the basic_games framework
- Implement custom features for the dual modding system
- Test thoroughly with different mod types

### Decision: Game Data Path and Virtual File System Mapping

**Status**: Decided

**Decision**: Set the game data path to `OblivionRemastered/Content` and implement custom handling for mapping files to the appropriate subdirectories.

**Rationale**:
- Allows handling both mod types from a single virtual root
- Provides flexibility for mods that might contain both types of files
- Simplifies the overall architecture while still supporting the dual modding nature

**Implementation Plan**:
- Set `GameDataPath` to `OblivionRemastered/Content`
- Implement custom installer logic to detect mod type and place files accordingly:
  - Traditional mods to `Dev/ObvData/Data/`
  - UE5 mods to `Paks/~mods/`

### Decision: Mod Type Detection Approach

**Status**: Under development

**Options**:
1. **File Extension Analysis**
   - Pros: Simple to implement, works for most cases
   - Cons: May not handle complex mods correctly

2. **Directory Structure Analysis**
   - Pros: More accurate for structured mods
   - Cons: More complex to implement

3. **Hybrid Approach**
   - Pros: Most accurate, handles edge cases
   - Cons: Most complex to implement

**Considerations**:
- Accuracy of detection
- Handling of hybrid mods
- User experience when detection fails

**Current Leaning**: 
Implement a hybrid approach that uses both file extension and directory structure analysis, with user confirmation for ambiguous cases.

### Decision: UE5 Load Order Management

**Status**: Under consideration

**Options**:
1. **Prefix System**
   - Pros: Allows user control over load order
   - Cons: Requires renaming files, which might be confusing

2. **Metadata-Based System**
   - Pros: Doesn't require file renaming
   - Cons: More complex to implement, might require custom UE5 loader

3. **No Custom Management**
   - Pros: Simplest to implement
   - Cons: Limited user control over load order

**Considerations**:
- How important load order is for UE5 mods
- User expectations for load order control
- Technical feasibility of each approach

**Current Leaning**: 
Start with a prefix system for controlling alphabetical loading, with clear documentation for users.

## Important Patterns and Preferences

### Development Patterns

1. **Incremental Development**
   - Start with core functionality (game detection, basic mod management)
   - Add specialized features for each mod type
   - Test thoroughly at each stage with real mods

2. **Reference-Based Development**
   - Use existing basic_games plugins as references
   - Follow established patterns from the Skyrim and Oblivion plugins
   - Adapt existing solutions where possible

3. **User-Centered Design**
   - Focus on making the dual modding system intuitive
   - Provide clear visual indicators for mod types
   - Ensure seamless integration with MO2's existing UI

### Code Organization Preferences

1. **Clean Separation of Concerns**
   - Separate core plugin logic from mod type-specific handling
   - Use dedicated classes for each major feature
   - Implement clear interfaces between components

2. **Consistent Naming and Structure**
   - Follow Python naming conventions (snake_case for functions and variables)
   - Use descriptive names that clearly indicate purpose
   - Organize code in a modular, maintainable structure

3. **Comprehensive Documentation**
   - Document code with clear docstrings
   - Provide high-level architecture documentation
   - Include examples for complex functionality

## Learnings and Project Insights

Our key learnings so far include:

1. **Oblivion Remaster's Dual Modding Nature**
   - The game supports both traditional Bethesda mods and UE5 mods
   - Traditional mods are placed in `OblivionRemastered\Content\Dev\ObvData\Data`
   - UE5 mods are placed in `OblivionRemastered\Content\Paks\~mods`
   - Load order is managed differently for each type

2. **UE5 Modding Patterns**
   - UE5 mods are loaded alphabetically from the ~mods folder
   - This is a standard pattern across UE5 games
   - Subfolders within these directories are also loaded alphabetically

3. **MO2 Plugin Architecture**
   - The basic_games framework provides a flexible way to add game support
   - Custom features can be registered to extend functionality
   - The framework supports INI file management on a per-profile basis

4. **Implementation Challenges**
   - Handling two different modding systems requires careful design
   - Mod type detection needs to be accurate to ensure proper file placement
   - User interface needs to clearly distinguish between mod types
   - Load order management needs different approaches for each mod type
