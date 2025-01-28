# Elbows.py

A Nuke script to create dots that organize the node graph, ensuring input streams are straight (B pipes, A pipes, or masks).

Select a node that has single or multiple inputs, where the inputs are straigt and run the script.

## Installation

1. **Place the Script:**
   
   Copy `elbows.py` to your Nuke scripts directory, typically found at:
   ```
   <Nuke Directory>/scripts/
   ```

2. **Update `menu.py`:**
   
   Add the following lines to your `menu.py` to integrate the script into Nuke's menu. You can name the menu item whatever you prefer.

   ```python
   # menu.py

   import nuke
   import elbows  # Ensure elbows.py is in the scripts directory

   # Add to the Custom menu
   custom_menu = nuke.menu('Nuke').addMenu('Custom')
   custom_menu.addCommand('Elbows', 'elbows.main()', 'Alt+Shift+E')
   ```

   - **Explanation:**
     - `addMenu('Custom')`: Creates a new menu named "Custom". You can change "Custom" to any name you like.
     - `addCommand('Elbows', 'elbows.main()', 'Alt+Shift+E')`: Adds a menu item named "Elbows" that triggers the `main` function in `elbows.py` with the shortcut `Alt + Shift + E`. Modify the name and shortcut as desired.

3. **Restart Nuke:**
   
   After updating `menu.py`, restart Nuke to apply the changes. You should see the new menu item under the specified menu with the assigned shortcut.

## Usage

1. Select the node you want to organize.
2. Use the menu item (`Elbows`) or press the shortcut (`Alt + Shift + E`) to run the script.
3. The script will create dots to align the input streams of the selected node.

