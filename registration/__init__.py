# -*- coding: utf-8 -*-
"""The tgapp-registration package"""
from tg import hooks, config


def plugme(app_config, options):
    app_config['_pluggable_registration_config'] = options
    hooks.register('after_config', lambda app: register_dal_interface(config, options))
    return dict(appid='registration', global_helpers=False)


def register_dal_interface(app_config, options):
    dal_interface = options.get('dal', 'sqla')
    if dal_interface == 'sqla':
        print 'initializing registration with sqla'
        from registration.model.sqla_models import SqlaRegistration
        app_config['registration_dal'] = SqlaRegistration()

    elif dal_interface == 'ming':
        print 'initializing registration with ming'
        from registration.model.ming_models import MingRegistration
        app_config['registration_dal'] = MingRegistration

    else:
        raise ValueError('not a valid registration dal interface: %s' % dal_interface)