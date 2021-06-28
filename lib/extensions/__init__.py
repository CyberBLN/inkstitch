# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

from lib.extensions.troubleshoot import Troubleshoot

from .apply_pattern import ApplyPattern
from .auto_satin import AutoSatin
from .break_apart import BreakApart
from .cleanup import Cleanup
from .convert_to_satin import ConvertToSatin
from .cut_satin import CutSatin
from .duplicate_params import DuplicateParams
from .embroider_settings import EmbroiderSettings
from .flip import Flip
from .global_commands import GlobalCommands
from .import_threadlist import ImportThreadlist
from .input import Input
from .install import Install
from .layer_commands import LayerCommands
from .lettering import Lettering
from .lettering_custom_font_dir import LetteringCustomFontDir
from .lettering_generate_json import LetteringGenerateJson
from .lettering_remove_kerning import LetteringRemoveKerning
from .object_commands import ObjectCommands
from .output import Output
from .params import Params
from .print_pdf import Print
from .remove_embroidery_settings import RemoveEmbroiderySettings
from .reorder import Reorder
from .simulator import Simulator
from .stitch_plan_preview import StitchPlanPreview
from .zip import Zip

__all__ = extensions = [StitchPlanPreview,
                        Install,
                        Params,
                        Print,
                        Input,
                        Output,
                        Zip,
                        Flip,
                        ApplyPattern,
                        ObjectCommands,
                        LayerCommands,
                        GlobalCommands,
                        ConvertToSatin,
                        CutSatin,
                        AutoSatin,
                        Lettering,
                        LetteringGenerateJson,
                        LetteringRemoveKerning,
                        LetteringCustomFontDir,
                        Troubleshoot,
                        RemoveEmbroiderySettings,
                        Cleanup,
                        BreakApart,
                        ImportThreadlist,
                        Simulator,
                        Reorder,
                        DuplicateParams,
                        EmbroiderSettings]
