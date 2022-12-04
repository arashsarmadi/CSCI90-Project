def integer_overflow_noncompliant():
    # Noncompliant: Number larger than limit of the datatype is stored.
    arr = np.array([[100000000]], dtype=np.int8)


def create_session_noncompliant():
    import boto3
    # Noncompliant: uses hardcoded secret access key.
    sample_key = "AjWnyxxxxx45xxxxZxxxX7ZQxxxxYxxx1xYxxxxx"
    boto3.session.Session(aws_secret_access_key=sample_key)