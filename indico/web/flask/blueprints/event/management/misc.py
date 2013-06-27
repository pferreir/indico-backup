# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2013 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico. If not, see <http://www.gnu.org/licenses/>.

from MaKaC.webinterface.rh import conferenceModif, collaboration
from indico.web.flask.util import rh_as_view
from indico.web.flask.blueprints.event.management import event_mgmt


# Logs
event_mgmt.add_url_rule('/logs', 'confModifLog', rh_as_view(conferenceModif.RHConfModifLog))

# Collaboration
event_mgmt.add_url_rule('/collaboration/', 'confModifCollaboration', rh_as_view(collaboration.RHConfModifCSBookings),
                        methods=('GET', 'POST'))
event_mgmt.add_url_rule('/collaboration/<tab>/', 'confModifCollaboration',
                        rh_as_view(collaboration.RHConfModifCSBookings), methods=('GET', 'POST'))
event_mgmt.add_url_rule('/collaboration/managers', 'confModifCollaboration-managers',
                        rh_as_view(collaboration.RHConfModifCSProtection))