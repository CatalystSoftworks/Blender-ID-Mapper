import bpy

from .types import ID_Map, ID_Group, ID_UL_IDGroupsList
from .op_assign import ID_AssignGroup, ID_AssignActiveGroup
from .op_create import ID_CreateGroup
from .op_remove import ID_RemoveGroup
from .op_select import ID_SelectByActiveGroup
from .op_add_id_material import ID_AddIDMapMaterial
from .ui import DATA_PT_idmap_groups, VIEW3D_MT_idmap_menu
from .utils import check_selection_mode

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


bl_info = {
    "name": "ID Mapper",
    "author": "Nicholas Glenn",
    "description": "Utility for setting vertex colors for the purpose baking ID maps.",
    "version": (1, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "wiki_url": "https://github.com/CatalystSoftworks/ID-Mapper-for-Blender",
    "support": "COMMUNITY",
    "warning": "",
    "category": "Generic"
}


classes = (
    ID_Group,
    ID_Map,
    ID_UL_IDGroupsList,
    ID_AssignGroup,
    ID_AssignActiveGroup,
    ID_CreateGroup,
    ID_RemoveGroup,
    ID_SelectByActiveGroup,
    ID_AddIDMapMaterial,
    DATA_PT_idmap_groups,
    VIEW3D_MT_idmap_menu,
)


def object_mode_context_menu(self, context):
    layout = self.layout


def edit_faces_menu(self, context):
    layout = self.layout
    layout.menu(VIEW3D_MT_idmap_menu.__name__)


def edit_faces_context_menu(self, context):
    layout = self.layout

    if check_selection_mode(False, False, True):
        layout.menu(VIEW3D_MT_idmap_menu.__name__)


def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Mesh.id_map = bpy.props.PointerProperty(
        name="ID Map", type=ID_Map)

    bpy.types.VIEW3D_MT_object_context_menu.append(object_mode_context_menu)
    bpy.types.VIEW3D_MT_edit_mesh_faces.append(
        edit_faces_menu)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(
        edit_faces_context_menu)
    # icons.register()
    # keymap.register(get_prefs())


def unregister():
    # keymap.unregister()
    # icons.unregister()
    bpy.types.VIEW3D_MT_object_context_menu.remove(
        object_mode_context_menu)
    bpy.types.VIEW3D_MT_edit_mesh_faces.remove(edit_faces_menu)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(edit_faces_context_menu)

    del bpy.types.Mesh.id_map

    for c in classes[::-1]:
        bpy.utils.unregister_class(c)
