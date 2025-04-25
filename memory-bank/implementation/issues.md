# Oblivion Remastered Plugin Issues

## Critical Issues

### 1. Plugins.txt Not Being Updated

**Description:**
The Plugins.txt file is not being automatically updated when mods are enabled or disabled in MO2. This file is critical for traditional Bethesda mods (.esp files) to be recognized by the game.

**Current Status:**
- ❌ Plugins.txt is not being updated when mods are enabled/disabled
- ❌ No manual update button or mechanism is currently implemented

**Investigation:**
- Attempted to use the `onModStateChanged` callback to detect mod state changes
- Implemented a method to update the Plugins.txt file
- The callback appears to be registered successfully but is not being triggered

**Potential Solutions:**
1. **Fix the callback issue:**
   - Investigate why the callback is not being triggered
   - Check if there are compatibility issues with the current MO2 version
   - Try different callback registration approaches

2. **Implement a manual update button:**
   - Add a button to the MO2 interface to manually update the Plugins.txt file
   - This would be a workaround until the automatic update is fixed

3. **Use a different detection mechanism:**
   - Explore alternative ways to detect mod state changes
   - Consider polling the mod list periodically

### 2. Mod State Change Detection Not Working

**Description:**
The `onModStateChanged` callback is not being triggered or is not working as expected. This prevents automatic updates of the Plugins.txt file and other state-dependent features.

**Current Status:**
- ❌ The callback is registered but not being triggered
- ❌ No logging output is seen when mods are enabled/disabled
- ✅ Custom logging to a file has been implemented as a diagnostic measure

**Investigation:**
- Implemented custom logging to a file to track callback registration and execution
- The log shows that the callback is registered successfully
- No log entries are created when mods are enabled/disabled
- Attempted to use print statements, but they are not being captured by MO2's logging system

**Potential Solutions:**
1. **Investigate callback registration:**
   - Check if the callback is being registered correctly
   - Verify that the callback signature matches what MO2 expects
   - Try different registration approaches

2. **Explore alternative callbacks:**
   - Check if there are other callbacks that might be triggered when mods are enabled/disabled
   - Look for undocumented or alternative ways to detect mod state changes

3. **Implement a polling mechanism:**
   - Periodically check the mod list state
   - Compare with previous state to detect changes
   - Update Plugins.txt when changes are detected

### 3. Logging Challenges

**Description:**
Standard print statements are not being captured by MO2's logging system, making it difficult to debug issues. Custom logging to a file is being used as a workaround.

**Current Status:**
- ❌ Print statements are not visible in MO2's log
- ✅ Custom logging to a file has been implemented
- ❌ The custom log file is not integrated with MO2's logging system

**Investigation:**
- Tried using standard print statements
- Implemented custom logging to a file in the MO2 directory
- The custom log file is being created and written to
- No integration with MO2's logging system has been achieved

**Potential Solutions:**
1. **Explore MO2's logging API:**
   - Check if there's a way to directly use MO2's logging system from Python
   - Look for examples in other plugins

2. **Enhance custom logging:**
   - Improve the custom logging system
   - Add timestamps, log levels, and other features
   - Make the log file more accessible to users

3. **Use a Python logging library:**
   - Configure a Python logging library to write to a file
   - Add more structured logging with different log levels

## Secondary Issues

### 4. UE5 Load Order Management

**Description:**
UE5 mods are loaded alphabetically from the ~mods folder, which limits control over load order. No custom load order management has been implemented yet.

**Current Status:**
- ❌ No custom load order management for UE5 mods
- ❌ UE5 mods are loaded alphabetically, which may not be optimal

**Investigation:**
- Researched UE5 mod loading behavior
- Confirmed that mods are loaded alphabetically from the ~mods folder
- No built-in mechanism for controlling load order beyond alphabetical sorting

**Potential Solutions:**
1. **Implement a prefix system:**
   - Add numeric prefixes to mod folders to control load order
   - This would require renaming files, which might be confusing for users

2. **Develop a metadata-based system:**
   - Create a metadata file that specifies load order
   - Implement a custom loader that reads this file
   - This would be more complex but wouldn't require file renaming

3. **Provide clear documentation:**
   - Explain the alphabetical loading behavior to users
   - Suggest naming conventions for controlling load order

### 5. Hybrid Mod Handling

**Description:**
Mods containing both traditional and UE5 components may not be handled optimally. The current implementation splits files into their respective directories, but this may not be ideal for all mods.

**Current Status:**
- ✅ Basic hybrid mod handling is implemented
- ❌ No special handling for mods that require files to stay together
- ❌ No user interface indication of hybrid mods

**Investigation:**
- Implemented basic hybrid mod handling
- Files are split based on their extensions
- No special handling for mods that require files to stay together

**Potential Solutions:**
1. **Improve hybrid mod detection:**
   - Develop more sophisticated detection of hybrid mods
   - Consider mod structure and file relationships

2. **Add user interface indicators:**
   - Show which mods are hybrid in the MO2 interface
   - Provide information about how files are being handled

3. **Implement special handling for certain mod types:**
   - Identify patterns in hybrid mods
   - Develop special handling for common patterns

## Technical Debt

### 6. Error Handling

**Description:**
The current error handling is basic and may not catch all edge cases. More robust error handling is needed to prevent crashes and provide better user feedback.

**Current Status:**
- ✅ Basic try/except blocks are implemented
- ❌ No detailed error reporting
- ❌ No user-friendly error messages

**Investigation:**
- Implemented basic try/except blocks
- Errors are caught but not always reported in a user-friendly way
- Some errors may still cause crashes

**Potential Solutions:**
1. **Enhance error handling:**
   - Add more specific exception handling
   - Provide detailed error messages
   - Log errors with context information

2. **Implement user-friendly error messages:**
   - Convert technical errors to user-friendly messages
   - Provide guidance on how to resolve common issues

3. **Add error recovery mechanisms:**
   - Implement ways to recover from errors
   - Provide fallback options when operations fail

### 7. Code Organization

**Description:**
The current code organization is functional but could be improved for better maintainability and readability.

**Current Status:**
- ✅ Basic code organization is in place
- ❌ Some methods are too long or complex
- ❌ Limited documentation

**Investigation:**
- Reviewed code organization
- Identified areas where methods could be split or refactored
- Documentation is limited to basic docstrings

**Potential Solutions:**
1. **Refactor long methods:**
   - Split long methods into smaller, focused methods
   - Improve method naming for clarity

2. **Enhance documentation:**
   - Add more detailed docstrings
   - Include examples and explanations
   - Document edge cases and assumptions

3. **Implement consistent coding style:**
   - Follow Python best practices
   - Use consistent naming conventions
   - Add type hints where appropriate

## Next Steps

Based on the issues identified, the following next steps are recommended:

1. **Fix Plugins.txt Update Issue (High Priority)**
   - Investigate why the `onModStateChanged` callback is not working
   - Implement a workaround if necessary
   - Test with various mod configurations

2. **Improve Logging (High Priority)**
   - Enhance the custom logging system
   - Explore integration with MO2's logging system
   - Add more detailed logging for debugging

3. **Implement UE5 Load Order Management (Medium Priority)**
   - Develop a system for controlling UE5 mod load order
   - Test with various UE5 mods
   - Document the approach for users

4. **Refine Hybrid Mod Handling (Medium Priority)**
   - Improve detection and handling of hybrid mods
   - Add user interface indicators for hybrid mods
   - Test with various hybrid mod configurations

5. **Enhance Error Handling (Medium Priority)**
   - Add more robust error handling
   - Implement user-friendly error messages
   - Test edge cases and error scenarios

6. **Refactor Code (Lower Priority)**
   - Improve code organization
   - Enhance documentation
   - Follow Python best practices

7. **Comprehensive Testing (Ongoing)**
   - Test with various mod configurations
   - Test with different combinations of traditional and UE5 mods
   - Test error handling and recovery
