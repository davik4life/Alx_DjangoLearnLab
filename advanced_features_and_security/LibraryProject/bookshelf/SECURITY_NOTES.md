Security Measures Implemented

1) Secure settings:
- DEBUG=False for production safety
- SECURE_CONTENT_TYPE_NOSNIFF=True
- X_FRAME_OPTIONS="DENY"
- SECURE_BROWSER_XSS_FILTER=True
- CSRF_COOKIE_SECURE=True and SESSION_COOKIE_SECURE=True for HTTPS-only cookies

2) CSRF protection:
All POST forms include {% csrf_token %}.

3) SQL injection prevention:
- No raw SQL constructed with user input
- Input validated using Django Forms
- Queries executed via Django ORM (parameterized)

4) CSP:
Implemented Content-Security-Policy using django-csp (or custom middleware).
