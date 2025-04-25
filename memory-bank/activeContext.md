# Active Context: MO2 Plugin for Oblivion Remaster

## Current Work Focus

We are currently in the **initial implementation phase with critical issues** of developing an MO2 plugin for Oblivion Remaster. The main focus areas are:

1. **Fixing Critical Issues**
   - Resolving the Plugins.txt update issue
   - Fixing mod state change detection
   - Improving logging and debugging capabilities

2. **Enhancing the Dual Modding System**
   - Refining support for traditional Bethesda mods (.esp/.bsa)
   - Optimizing support for Unreal Engine 5 mods (.pak/.ucas/.utoc)
   - Improving handling of hybrid mods

3. **Implementing Load Order Management**
   - Developing reliable Plugins.txt management for traditional mods
   - Creating a system for UE5 mod load order control
   - Ensuring proper mod conflict resolution

## Recent Changes

We have made significant progress in implementing the plugin:

1. **Implemented Core Plugin Structure**
   - Created the main `OblivionRemasteredGame` class
   - Defined game-specific properties and paths
   - Set up basic game detection and integration with MO2
   - Implemented save game handling and INI file management

2. **Developed Mod Type Detection and Handling**
   - Created the `OblivionRemasteredModDataChecker` class
   - Implemented file extension and structure analysis
   - Set up proper file placement for each mod type
   - Added basic handling for hybrid mods

3. **Implemented Custom Logging**
   - Created a custom logging system to a file
   - Added detailed logging for callback registration and execution
   - Implemented error handling for critical operations

4. **Attempted Callback Implementation**
   - Tried to implement the `onModStateChanged` callback
   - Created methods for updating Plugins.txt
   - Encountered issues with callback triggering

5. **Documented Implementation Details and Issues**
   - Created detailed documentation of the implementation
   - Documented critical issues and potential solutions
   - Established next steps and priorities

## Next Steps

The immediate next steps in the project are:

1. **Fix Plugins.txt Update Issue**
   - Investigate why the Plugins.txt file is not being updated
   - Explore alternative approaches for detecting mod state changes
   - Implement a reliable solution for updating Plugins.txt

2. **Improve Mod State Change Detection**
   - Investigate why the `onModStateChanged` callback is not working
   - Try different callback registration approaches
   - Consider implementing a polling mechanism as a fallback

3. **Enhance Logging System**
   - Improve the custom logging system
   - Explore integration with MO2's logging system
   - Add more detailed logging for debugging

4. **Implement UE5 Load Order Management**
   - Develop a system for controlling UE5 mod load order
   - Consider a prefix system or metadata-based approach
   - Test with various UE5 mods

5. **Refine Hybrid Mod Handling**
   - Improve detection and handling of hybrid mods
   - Add special handling for mods that require files to stay together
   - Test with various hybrid mod configurations

6. **Enhance Error Handling**
   - Add more robust error handling
   - Implement user-friendly error messages
   - Add error recovery mechanisms

7. **Comprehensive Testing**
   - Test with various mod configurations
   - Test with different combinations of traditional and UE5 mods
   - Test error handling and recovery

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
