# -*- coding: utf-8 -*-
import sys
import tg
from tg.i18n import lazy_ugettext as l_
from tgext.ajaxforms import ajaxloaded
from tgext.pluggable import plug_url

if tg.config.get('prefer_toscawidgets2', False):
    from tw2.forms import TableForm, TextField, PasswordField
    from tw2.core import Required
    from validators import UniqueEmailValidator, UniqueUserValidator
    from formencode import validators

    class RegistrationForm(TableForm):
        user_name = TextField(label=l_(u'User Name'), validator=UniqueUserValidator(not_empty=True))
        email_address = TextField(label=l_(u'Email'), validator=UniqueEmailValidator(not_empty=True))
        password = PasswordField(label=l_(u'Password'), validator=Required)
        password_confirm = PasswordField(label=l_(u'Confirm Password'), validator=Required)
        validator = validators.FieldsMatch('password', 'password_confirm')

else:
    from tw.api import WidgetsList
    from tw.forms import TableForm, TextField, PasswordField
    from tw.forms import validators
    from validators import UniqueEmailValidator, UniqueUserValidator

    class RegistrationForm(TableForm):
        class fields(WidgetsList):
            user_name = TextField(label_text=l_('User Name'), validator=UniqueUserValidator(not_empty=True))
            email_address = TextField(label_text=l_('Email'), validator=UniqueEmailValidator(not_empty=True))
            password = PasswordField(label_text=l_('Password'), validator=validators.UnicodeString(not_empty=True))
            password_confirm = PasswordField(label_text=l_('Confirm Password'),
                validator=validators.UnicodeString(not_empty=True))

        validator = validators.Schema(chained_validators = [validators.FieldsMatch('password', 'password_confirm')])