import logging

from django_auth_policy.checks import enforce_password_change


logger = logging.getLogger(__name__)


def update_session(session, user):
    """ Check for temporary or expired passwords and store in session
    Our middleware should enforce a password change in next request
    """
    enforce, is_exp, is_temp = enforce_password_change(user)

    # Log password enforcement
    if enforce:
        if is_temp and not session.get('password_is_temporary'):
            logger.info(u'User %s must change temporary password', user)

        if is_exp and not session.get('password_is_expired'):
            logger.info(u'User %s must change expired password', user)

        if (not is_temp and not is_exp and
            not session.get('password_change_enforce')):
            logger.info(u'User %s must change password', user)

    session['password_change_enforce'] = enforce
    session['password_is_expired'] = is_exp
    session['password_is_temporary'] = is_temp

