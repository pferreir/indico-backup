# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2014 European Organization for Nuclear Research (CERN).
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
## along with Indico; if not, see <http://www.gnu.org/licenses/>.

from wtforms.fields.core import IntegerField
from wtforms.validators import InputRequired, NumberRange

from indico.modules.rb.forms.base import IndicoForm
from indico.modules.rb.forms.fields import EmailListField, PrincipalField
from indico.util.i18n import _


class SettingsForm(IndicoForm):
    admin_principals = PrincipalField(_(u'Administrators'), groups=True)
    authorized_principals = PrincipalField(_(u'Authorized users/groups'), groups=True)
    assistance_emails = EmailListField(_(u'Assistance email addresses (one per line)'))
    notification_hour = IntegerField(_(u'Hour at which occurrence notifications should be sent'),
                                     [InputRequired(), NumberRange(0, 23)], default=6)
    notification_before_days = IntegerField(_(u'Send occurrence notifications X days before the occurrence'),
                                            [InputRequired()], default=0)
    vc_support_emails = EmailListField(_(u'Videoconference support email addresses (one per line)'))
