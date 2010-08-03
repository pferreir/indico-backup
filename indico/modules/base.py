# -*- coding: utf-8 -*-
##
##
## This file is part of CDS Indico.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Indico; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""This file contain the definition of those classes which implement the
access to the objects in the DB related to "modules". "modules" is in the root
of the DB and holds a tree with Holders for different modules apart from categories,
conferences, and so.
The system will fetch and add objects to the collections (or holders) through these
classes that interact directly with the persistence layer and do the necessary operations
behind to ensure the persistence.
"""

from MaKaC.common.ObjectHolders import ObjectHolder
from MaKaC.errors import MaKaCError
from MaKaC.i18n import _
from persistent import Persistent


class ModuleHolder( ObjectHolder ):
    """ Specialised ObjectHolder class which provides a wrapper for collections
        based in a Catalog for indexing the objects. It allows to index some
        declared attributes of the stored objects and then perform SQL-like
        queries
    """
    idxName = "modules"
    counterName = "MODULES"
    _availableModules = None

    def __init__(self):
        ObjectHolder.__init__(self)
        # These imports are done like this in order to avoid circular imports problems.
        import indico.modules.news as news
        import indico.modules.cssTpls as cssTpls
        import indico.modules.upcoming as upcoming
        import indico.modules.scheduler as scheduler

        ModuleHolder._availableModules = {
            news.NewsModule.id               : news.NewsModule,
            cssTpls.CssTplsModule.id         : cssTpls.CssTplsModule,
            upcoming.UpcomingEventsModule.id : upcoming.UpcomingEventsModule,
            scheduler.SchedulerModule.id             : scheduler.SchedulerModule
        }

    def _newId( self ):
        id = ObjectHolder._newId( self )
        return "%s"%id

    def destroyById(self, moduleId):
        del self._getIdx()[str(moduleId)]

    def getById(self, moduleId):
        """returns an object from the index which id corresponds to the one
            which is specified.
        """

        if type(moduleId) is int:
            moduleId = str(moduleId)
        if self._getIdx().has_key(str(moduleId)):
            return self._getIdx()[str(moduleId)]
        elif self._availableModules.has_key(moduleId):
            newmod=self._availableModules[moduleId]()
            self.add(newmod)
            return newmod
        else:
            raise MaKaCError( ("Module id %s does not exist") % str(moduleId) )


class Module(Persistent):
    """
    This class represents a general module that it is stored in the database.
    A module class is a way to access the main data for a general Indico module.
    A module could be news management, plugins management, etc and anything not
    related to Indico settings (HelperMaKaCInfo) categories and conferences.
    """

    id = ""

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        return self.id

    @classmethod
    def destroyDBInstance(cls):
        return ModuleHolder().destroyById(cls.id)

    @classmethod
    def getDBInstance(cls):
        """
        Returns the module instance that is stored in the database
        """
        return ModuleHolder().getById(cls.id)
