# -*-coding: utf-8-*-

import logging

from pyramid.view import view_config, view_defaults

from travelcrm.views import BaseView
from travelcrm.lib.utils.common_utils import translate as _

from ..forms.persons_import import PersonsImportForm


log = logging.getLogger(__name__)


@view_defaults(
    context='..resources.persons_import.PersonsImportResource',
)
class PersonsImportView(BaseView):

    @view_config(
        name='action',
        request_method='GET',
        renderer='travelcrm_persons_import:templates/index.mako',
        permission='import',
    )
    def action(self):
        return {
            'title': self._get_title(),
        }

    @view_config(
        name='action',
        request_method='POST',
        renderer='json',
        permission='import'
    )
    def _action(self):
        form = PersonsImportForm(self.request)
        if form.validate():
            form.submit()
            return {
                'success_message': _(u'Task will start soon'),
                'response': None
            }
        else:
            return {
                'error_message': _(u'Please, check errors'),
                'errors': form.errors
            }
