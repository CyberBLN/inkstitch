# Authors: see git history
#
# Copyright (c) 2010 Authors
# Licensed under the GNU GPL version 3.0 or later.  See the file LICENSE for details.

import inkex

from ..elements.utils import is_satin_column
from ..i18n import _
from ..svg import get_correction_transform
from .base import InkstitchExtension


class CutSatin(InkstitchExtension):
    def effect(self):
        if not self.get_elements():
            return

        if not self.svg.selected:
            inkex.errormsg(_("Please select one or more satin columns to cut."))
            return

        for satin in self.elements:
            if is_satin_column(satin):
                command = satin.get_command("satin_cut_point")

                if command is None:
                    # L10N will have the satin's id prepended, like this:
                    # path12345: error: this satin column does not ...
                    satin.fatal(_('this satin column does not have a "satin column cut point" command attached to it. '
                                  'Please use the "Attach commands" extension and attach the "Satin Column cut point" command first.'))

                split_point = command.target_point
                command_group = command.use.getparent()
                if command_group is not None and command_group.get('id').startswith('command_group'):
                    command_group.getparent().remove(command_group)
                else:
                    command.use.getparent().remove(command.use)
                    command.connector.getparent().remove(command.connector)

                new_satins = satin.split(split_point)
                transform = get_correction_transform(satin.node)
                parent = satin.node.getparent()
                index = parent.index(satin.node)
                parent.remove(satin.node)
                for new_satin in new_satins:
                    new_satin.node.set('transform', transform)
                    parent.insert(index, new_satin.node)
                    index += 1
