# C++ Notes for MO2 Plugin Development

## MO2 C++ Architecture

MO2 is primarily written in C++ with a plugin system that allows for both C++ and Python plugins. Understanding the C++ architecture is important even when developing Python plugins, as the Python plugins interact with the C++ core through bindings.

### Key Components

1. **IPluginGame Interface**
   - Core interface for game plugins
   - Defines methods for game detection, file management, and game-specific features
   - Implemented by both C++ and Python game plugins

2. **IOrganizer Interface**
   - Provides access to MO2's core functionality
   - Allows plugins to interact with mod list, profile management, etc.
   - Available to plugins through the `init` method

3. **ModList Class**
   - Manages the list of mods in MO2
   - Provides methods for querying mod state and metadata
   - Includes the `onModStateChanged` signal for detecting mod state changes

4. **Virtual File System (VFS)**
   - Core component that handles file virtualization
   - Maps mod files to their virtual locations
   - Critical for proper mod management

## C++ vs Python Plugin Development

### C++ Plugins

**Advantages:**
- Direct access to MO2's internal APIs
- Potentially better performance
- Deeper integration with MO2's core

**Disadvantages:**
- More complex development process
- Requires C++ knowledge and build environment
- Less portable across different systems

### Python Plugins (via basic_games)

**Advantages:**
- Simpler development process
- Faster iteration
- More portable
- Easier to maintain

**Disadvantages:**
- Limited access to some internal MO2 features
- Potential performance overhead
- Some features may be harder to implement

## Callback System in MO2

MO2 uses a signal/slot system (based on Qt) for callbacks. This is important for features like detecting when mods are enabled or disabled.

### Key Signals

1. **onModStateChanged**
   - Emitted when mods are enabled or disabled
   - Provides a map of mod names to their states
   - Used for updating plugin lists and other state-dependent features

2. **onProfileChanged**
   - Emitted when the active profile changes
   - Used for updating profile-specific features

3. **onPluginSettingChanged**
   - Emitted when plugin settings are changed
   - Used for updating plugin behavior based on settings

### Implementation Challenges

- Signal connections must be properly managed to avoid memory leaks
- Callbacks should be lightweight to avoid UI freezes
- Error handling is critical to prevent crashes

## Logging in MO2

MO2 has a sophisticated logging system that allows plugins to log messages at different levels.

### Logging Methods

1. **Direct Logging**
   - Using `log::log` function from MO2's logging system
   - Supports different log levels (debug, info, warning, error)
   - Messages appear in MO2's log window and log files

2. **IOrganizer Logging**
   - Some versions of MO2 provide logging through the IOrganizer interface
   - Not consistently available across all versions

3. **Custom Logging**
   - Creating custom log files for plugin-specific logging
   - Useful for detailed debugging information

### Log Levels

- **Debug**: Detailed information for debugging
- **Info**: General information about normal operation
- **Warning**: Potential issues that don't prevent operation
- **Error**: Serious issues that may prevent proper operation

## Memory Management Considerations

- MO2 uses a mix of raw pointers, smart pointers, and Qt's parent-child ownership model
- Python plugins benefit from Python's garbage collection
- Be careful with callbacks that might outlive their targets
- Consider the lifecycle of objects when designing plugin features
