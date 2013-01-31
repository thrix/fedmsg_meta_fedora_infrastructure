# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
from fedmsg.meta.base import BaseProcessor


class KojiProcessor(BaseProcessor):
    __name__ = "koji"
    __description__ = "the Fedora build system"
    __link__ = "https://koji.fedoraproject.org/koji"
    __docs__ = "https://fedoraproject.org/wiki/Using_the_Koji_build_system"
    __obj__ = "Koji Builds"
    __icon__ = "http://fedoraproject.org/w/uploads/2/20/" + \
        "Artwork_DesignService_koji-icon-48.png"

    def handle_msg(self, msg, **config):
        return '.buildsys.' in msg['topic']

    def subtitle(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            tmpl = self._('{name}-{version}-{release} tagged {tag}')
            return tmpl.format(**msg['msg'])
        else:
            raise NotImplementedError()

    def link(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            raise NotImplementedError("We need build ids in the messages...")
        else:
            raise NotImplementedError()

    def usernames(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            raise NotImplementedError("We need owner usernames in the messages...")
        else:
            raise NotImplementedError()

    def packages(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set([msg['msg']['name']])
        else:
            raise NotImplementedError()

    def objects(self, msg, **config):
        if 'buildsys.tag' in msg['topic']:
            return set(['/'.join([
                'builds',
                msg['msg']['name'],
                msg['msg']['version'],
                msg['msg']['release'],
            ])])
        else:
            raise NotImplementedError()
