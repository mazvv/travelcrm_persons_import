# -*-coding: utf-8 -*-

import colander

from travelcrm.forms import BaseForm, File
from travelcrm.lib.utils.common_utils import translate as _
from travelcrm.lib.utils.common_utils import get_storage_dir
from travelcrm.lib.utils.security_utils import get_auth_employee
from travelcrm.lib.bl.storages import is_allowed_file_size

from ..lib.scheduler.persons_import import schedule_persons_import


@colander.deferred
def extensions_validator(node, kw):
    request = kw.get('request')
    def validator(node, value):
        if not is_allowed_file_size(value.file):
            raise colander.Invalid(
                node,
                _(u'File is too big')
            )
        if not request.storage.file_allowed(value, extensions=('csv')):
            raise colander.Invalid(
                node, 
                _(u'This files types is not allowed'))
        value.file.seek(0)
    return colander.All(validator,)


@colander.deferred
def passport_validator(node, kw):
    request = kw.get('request')

    def validator(node, value):
        passport_num = request.params.get('passport_num')
        passport_country = request.params.get('passport_country')
        if value == 0 and any([
            passport_num != '0',
            passport_country != '0',
        ]):
            raise colander.Invalid(
                node,
                _(u'Set num of column'),
            )

    return colander.All(validator,)


@colander.deferred
def foreign_passport_validator(node, kw):
    request = kw.get('request')

    def validator(node, value):
        foreign_passport_end_date = request.params.get(
            'foreign_passport_end_date'
        )
        foreign_passport_num = request.params.get('foreign_passport_num')
        foreign_passport_country = request.params.get(
            'foreign_passport_country'
        )
        if value == 0 and any([
            foreign_passport_end_date != '0',
            foreign_passport_num != '0',
            foreign_passport_country != '0'
        ]):
            raise colander.Invalid(
                node,
                _(u'Set num of column'),
            )

    return colander.All(validator,)


class _PassportImportSchema(colander.Schema):
    passport_country = colander.SchemaNode(
        colander.Integer(),
        validator=passport_validator
    )
    passport_num = colander.SchemaNode(
        colander.Integer(),
        validator=passport_validator
    )
    passport_description = colander.SchemaNode(
        colander.Integer(),
    )


class _ForeignPassportImportSchema(colander.Schema):
    foreign_passport_country = colander.SchemaNode(
        colander.Integer(),
        validator=foreign_passport_validator
    )
    foreign_passport_num = colander.SchemaNode(
        colander.Integer(),
        validator=foreign_passport_validator
    )
    foreign_passport_end_date = colander.SchemaNode(
        colander.Integer(),
        validator=foreign_passport_validator
    )
    foreign_passport_description = colander.SchemaNode(
        colander.Integer(),
    )
    

class _PersonsImportSchema(
    _PassportImportSchema, _ForeignPassportImportSchema
):
    file = colander.SchemaNode(
        File(),
        validator=extensions_validator
    )
    first_name = colander.SchemaNode(
        colander.Integer(),
        validator=colander.All(
            colander.Range(min=1, min_err=_(u'Set num of column'))
        ),
    )
    second_name = colander.SchemaNode(
        colander.Integer(),
    )
    last_name = colander.SchemaNode(
        colander.Integer(),
        validator=colander.All(
            colander.Range(min=1, min_err=_(u'Set num of column'))
        ),
    )
    phones = colander.SchemaNode(
        colander.Integer(),
    )
    emails = colander.SchemaNode(
        colander.Integer(),
    )


class PersonsImportForm(BaseForm):
    _schema = _PersonsImportSchema

    def submit(self):
        upload_path = self.request.storage.save(
            self._controls.get('file'),
            folder=get_storage_dir(),
            extensions=('csv'),
            randomize=True
        )
        data = dict([
            (key, val) for key, val in self._controls.items()
            if key != 'file' and val
        ])
        data['upload_path'] = (
            self.request.storage.base_path + '/' + upload_path
        )
        auth_employee = get_auth_employee(self.request)
        schedule_persons_import(auth_employee.id, **data)
        return
