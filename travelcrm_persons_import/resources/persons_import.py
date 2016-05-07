# -*-coding: utf-8 -*-

from zope.interface import implementer

from travelcrm.interfaces import (
    IResourceType,
)
from travelcrm.resources import (
    ResourceTypeBase,
)
from travelcrm.lib.utils.common_utils import translate as _


@implementer(IResourceType)
class PersonsImportResource(ResourceTypeBase):

    __name__ = 'persons_import'


    @property
    def allowed_permisions(self):
        return [
            ('import', _(u'import')),
        ]
