# ID Map Tool for Blender 2.8+

> :construction_worker: This add-on is a work in progress, however, its core functionality is working and can be used to quickly assigning vertex colors for baking ID maps.

This addon provides a small set of utilties for quickly assigning vertex colors to selected faces for the purpose of baking ID maps using programs like Substance Painter, Houdini, or even Blender.

## Installation

Download this repository and open up Blender, then navigate to your user preferences. Select the "Addons" tab and then click "Install Addon from File". When the file selection dialog pops up, select the `.zip` you downloaded.

## Planned Features

- [x] Create ID map groups per object
- [x] Assign created ID map groups to selected faces
- [x] Removed created ID map groups
    - [ ] Remove vertex color data when removing ID map groups
- [ ] Select/Deselect faces using ID map groups
- [ ] (Almost done) Assign a material for displaying the current ID map colors outside of vertex color mode
- [ ] 1-click quick-bake ID maps inside of Blender