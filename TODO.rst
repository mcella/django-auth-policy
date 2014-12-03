IDEAS / TODO'S
==============

Release 1.0
-----------

* Move to using an INI file, which may either be specified in a environment
  variable or in Django settings.

* Implement a login_required_exempt decorator which works together with the
  login required middleware.
  (which sets an attribute on the specified view)

* LoginRequiredMiddleware could catch 404's and return login page to avoid
  exposing which URLs are available on a site (because it returns 404
  or login screens depending of existence of URL resource)

* Allow regex expressions for LoginRequiredMiddleware

* Add unit tests for logout after password change

* Expand docs

    * Add example for Login form

    * Add example on how to implement Djangos password reset views

    * Add example on how to send temporary passwords by email

* Add tests for UserChange tracking

* Store authentication backend name in attempt, i.e.::

	user = authenticate(username=u, password=p)
	if user is not None:
		attempt.backend = user.backend

* pre_auth_checks: Change this function and underlying policies to accept a
  `credentials` dictionary and a HTTP `headers` dictionary.

  If this can't be done keeping backwards compatibility then move this to 2.0

* Add command to remove db records older than a specified time (specified in
  settings file or overrule on command line).

* Submit complete request headers dict to pre_auth_checks instead of only
  `remove_addr` and `host`?

Release 1.1
-----------

* Only login from whitelisted IP addresses/ranges.
  Or provide example which limits admin/superuser login
  to certain IP addresses by sending the REMOTE_ADDR to authentication backend.

* Optionally prevent usage of passwords (plains) from a list of common passwords
  
  Supply a publicly available list with django_auth_policy?

  Filter this list based on the other policy rules.

  Optionally also allow lists of forbidden hashed passwords,
  for possibly sensitive passwords. This list should not be too long.

* Add more signals as hooks for additional functionality???

* Optionally use different source of random data for temporary password
  generation (see Python cryptography.io library)

* Allow projects to use customized temporary password generator

* Allow temporary passwords to expire, and fall back to old password?

* Optionally check password complexity at login and enforce new password
  for weak passwords

* Optionally measure entropy of passwords
  
  Possible indicators:

  - len(set(password))

  - len(set(password.lower()))

  - len(re.sub(r'(.)(\1)+', r'\1', password)) # Remove consecutive characters

  Research: any good enough algorithms available?

* Add password strength ideas from OWASP:
  https://www.owasp.org/index.php/Authentication_Cheat_Sheet#Implement_Proper_Password_Strength_Controls

  - 3 out of 4 complexity rules
  - not more than 2 identical characters in a row (ie. 111 not allowed)

* Add authentication ideas from Mozilla:
  https://wiki.mozilla.org/WebAppSec/Secure_Coding_Guidelines#Authentication

* Advice users to use a password hasher for bcrypt/scrypt/PDKDF2 which stores
  nonce/salt seperately (not in the database) but still accessible by all web
  processes. Also pepper the hash with a site wide 'password pepper' string
  (similar to Django's SECRET_KEY)?

* Use sensitive_variables and sensitive_post_parameters to hide passwords from
  Django error reports

* Add password strength checker which uses unicodedata.category
  http://www.unicode.org/reports/tr44/tr44-4.html#General_Category_Values

* Optionally forbid/alarm/logout users when certain headers change (USER_AGENT,
  REMOTE_ADDR, X_FORWARDED_FOR). Also log this. Optionally fix session to 
  REMOTE_ADDR, USER_AGENT and X_FORWARDED_FOR header?

* Optionally keep a limited history of passwords (hashed) to prevent password
  reuse, password model field has been added.

Release 2.0
-----------

* Move forms into documentation examples and tests?
  Create a function that can be called within an form clean method.
  This stimulates projects to implement Django Auth Policy correctly in project
  specific forms.

* Store all HTTP headers JSON encoded with login attempt, in addition to
  current fields

* Remove Django dependency from main code and add special module/package for
  Django integration. Add examples for Flask / WTForms???
