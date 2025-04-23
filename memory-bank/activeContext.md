# Active Context: MO2 Plugin for Oblivion Remaster

## Current Work Focus

We are currently in the **exploration and planning phase** of developing an MO2 plugin for Oblivion Remaster. The main focus areas are:

1. **Understanding MO2's Plugin Architecture**
   - Exploring both native C++ and Python-based plugin approaches
   - Analyzing existing game plugins (Skyrim, Oblivion) as reference implementations
   - Understanding the basic_games framework for Python-based plugins

2. **Researching Oblivion Remaster's Modding Approach**
   - Identifying how the remaster combines traditional Bethesda modding with Unreal Engine elements
   - Understanding the file structure and organization of the game
   - Determining the specific requirements for mod management

3. **Evaluating Implementation Options**
   - Comparing native C++ vs. Python-based approaches
   - Identifying the pros and cons of each approach
   - Determining which approach best suits the requirements of Oblivion Remaster modding

## Recent Changes

As this project is in its initial phase, there are no implementation changes yet. However, we have:

1. **Set up a development environment**
   - Added reference code from existing game plugins (Skyrim, Oblivion)
   - Added the basic_games framework for reference
   - Added the rootbuilder plugin as an example of a Python-based utility plugin

2. **Conducted initial research**
   - Explored the structure of native game plugins
   - Explored the structure of Python-based game plugins
   - Analyzed the rootbuilder plugin as an example of a complex Python plugin

3. **Created initial documentation**
   - Established the project brief
   - Documented the product context
   - Outlined the system architecture and patterns
   - Documented the technical context

## Next Steps

The immediate next steps in the project are:

1. **Gather Detailed Information on Oblivion Remaster**
   - Analyze the game's file structure
   - Identify the modding approach used by the remaster
   - Determine how traditional Bethesda mods and Unreal Engine assets are handled

2. **Create a Prototype Plugin**
   - Develop a minimal viable plugin that can detect the game
   - Test basic integration with MO2
   - Validate the chosen approach (C++ or Python)

3. **Implement Core Functionality**
   - Game detection and basic integration
   - Mod directory structure definition
   - Basic mod installation and management

4. **Develop Specialized Features**
   - Support for traditional Bethesda plugins (.esp/.esm)
   - Support for Unreal Engine assets (.pak)
   - Custom UI elements if needed

## Active Decisions and Considerations

### Decision: Native C++ vs. Python Implementation

**Status**: Under consideration

**Options**:
1. **Native C++ Plugin**
   - Pros: Deep integration, better performance, more control
   - Cons: More complex development, harder to maintain

2. **Python Plugin (via basic_games)**
   - Pros: Easier development, faster iteration, simpler maintenance
   - Cons: Limited functionality, potential performance issues for complex operations

**Considerations**:
- The complexity of Oblivion Remaster's modding approach
- The need for custom handling of Unreal Engine assets
- Development resources and timeline
- Long-term maintenance requirements

**Current Leaning**: 
Python-based approach for initial development, with the option to migrate to a native C++ plugin if more advanced functionality is required.

### Decision: Handling Unreal Engine Assets

**Status**: Research needed

**Options**:
1. **Treat as Regular Files**
   - Pros: Simpler implementation, works with existing systems
   - Cons: May miss opportunities for specialized handling

2. **Develop Custom Handling**
   - Pros: Better integration, more features for UE assets
   - Cons: More complex development, requires deeper understanding of UE

**Considerations**:
- How UE assets are structured in Oblivion Remaster
- How mods for UE assets are typically distributed
- The level of integration needed for optimal user experience

**Current Leaning**: 
Start with treating UE assets as regular files, then develop custom handling based on research findings and user feedback.

## Important Patterns and Preferences

### Development Patterns

1. **Incremental Development**
   - Start with a minimal viable plugin
   - Add features incrementally
   - Test thoroughly at each stage

2. **Reference-Based Development**
   - Use existing plugins as references
   - Follow established patterns and conventions
   - Adapt existing solutions where possible

3. **User-Centered Design**
   - Focus on user experience
   - Make the plugin intuitive for users familiar with MO2
   - Provide clear documentation and guidance

### Code Organization Preferences

1. **Clean Separation of Concerns**
   - Separate game-specific logic from general plugin logic
   - Isolate Unreal Engine-specific handling
   - Use clear interfaces between components

2. **Consistent Naming and Structure**
   - Follow MO2's naming conventions
   - Use consistent file and class naming
   - Organize code in a logical, easy-to-navigate structure

3. **Comprehensive Documentation**
   - Document code thoroughly
   - Provide high-level architecture documentation
   - Include usage examples and guidelines

## Learnings and Project Insights

As we're in the early stages, our key learnings so far include:

1. **MO2 Plugin Architecture**
   - MO2 supports both native C++ and Python-based plugins
   - The basic_games framework provides a simpler way to add game support
   - Different plugin types (game plugins, tool plugins, installer plugins) serve different purposes

2. **Game Plugin Requirements**
   - Game plugins need to handle game detection, mod management, and plugin management
   - Different games require different approaches based on their modding systems
   - Bethesda games share common patterns that can be leveraged

3. **Hybrid Modding Challenges**
   - Games that combine different modding approaches (like Bethesda + UE) present unique challenges
   - Custom handling may be needed for different types of mod files
   - Balance between leveraging existing systems and developing custom solutions is key
