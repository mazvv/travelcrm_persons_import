# -*-coding:utf-8-*-

import logging
import csv
from datetime import datetime
import transaction

import pytz

from travelcrm.models import DBSession
from travelcrm.lib.utils.common_utils import translate as _
from travelcrm.lib.utils.scheduler_utils import gen_task_id, scopped_task
from travelcrm.lib.bl.employees import get_employee_structure
from travelcrm.lib.scheduler import scheduler

from travelcrm.models.employee import Employee
from travelcrm.models.contact import Contact
from travelcrm.models.passport import Passport
from travelcrm.models.person import Person
from travelcrm.models.resource import Resource
from travelcrm.models.country import Country
from travelcrm.models.notification import Notification
from travelcrm.resources.persons import PersonsResource
from travelcrm.resources.contacts import ContactsResource
from travelcrm.resources.passports import PassportsResource
from travelcrm.resources.notifications import NotificationsResource


log = logging.getLogger(__name__)


@scopped_task
def _persons_import(employee_id, delimiter, quotechar, **kwargs):
    csv_path = kwargs.pop('upload_path')
    employee = Employee.get(employee_id)
    owner_structure = get_employee_structure(employee)
    log.info('Start persons import')
    with open(csv_path, 'rb') as csvfile:
        reader = csv.reader(
            csvfile, delimiter=delimiter, quotechar=quotechar
        )
        for row in reader:
            person = Person(
                resource=Resource(PersonsResource, owner_structure)
            )
            if kwargs.get('first_name'):
                person.first_name = row[kwargs.get('first_name') - 1]
            if kwargs.get('second_name'):
                person.second_name = row[kwargs.get('second_name') - 1]
            if kwargs.get('last_name'):
                person.last_name = row[kwargs.get('last_name') - 1]
            
            if kwargs.get('phones'):
                phones = row[kwargs.get('phones') - 1]
                for phone in phones.split():
                    person.contacts.append(
                        Contact(
                            resource=Resource(
                                ContactsResource, owner_structure
                            ),
                            contact_type='phone',
                            status='active',
                            contact=phone
                        )
                    )

            if kwargs.get('emails'):
                emails = row[kwargs.get('emails') - 1]
                for email in emails.split():
                    person.contacts.append(
                        Contact(
                            resource=Resource(
                                ContactsResource, owner_structure
                            ),
                            contact_type='email',
                            status='active',
                            contact=email
                        )
                    )

            if kwargs.get('passport_country') and kwargs.get('passport_num'):
                country = Country.by_iso_code(
                    row[kwargs.get('passport_country') - 1]
                )
                passport = Passport(
                    resource=Resource(
                        PassportsResource, owner_structure
                    ),
                    passport_type='citizen',
                    country=country,
                    num=row[kwargs.get('passport_num') - 1]
                )
                person.passports.append(passport)
            
            if (
                kwargs.get('foreign_passport_country')
                and kwargs.get('foreign_passport_num')
                and kwargs.get('foreign_passport_end_date')
            ):
                country = Country.by_iso_code(
                    row[kwargs.get('foreign_passport_country') - 1]
                )
                passport = Passport(
                    resource=Resource(
                        PassportsResource, owner_structure
                    ),
                    passport_type='foreign',
                    country=country,
                    num=row[kwargs.get('foreign_passport_num') - 1],
                    end_date=datetime.strptime(
                        row[kwargs.get('foreign_passport_end_date') - 1],
                        '%Y-%m-%d'
                    )
                )
                person.passports.append(passport)
            with transaction.manager:
                DBSession.add(person)

    with transaction.manager:
        notification = Notification(
            title=_(u'Persons import status'),
            descr=_(u'Persons import was completed'),
            resource=Resource(NotificationsResource, owner_structure)
        )
        employee.notifications.append(notification)


def schedule_persons_import(
    employee_id, delimiter=';', quotechar='"', **kwargs
):
    scheduler.add_job(
        _persons_import,
        trigger='date',
        id=gen_task_id(),
        replace_existing=True,
        run_date=datetime.now(pytz.utc),
        args=[employee_id, delimiter, quotechar],
        kwargs=kwargs,
    )
