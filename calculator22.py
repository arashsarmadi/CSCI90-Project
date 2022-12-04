def set_user_noncompliant():
    import os
    root = 0
    # Noncompliant: the process user is set to root.
    os.setuid(root)