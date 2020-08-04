from hashlib import md5, sha256
import datetime


def hash_md5(data):
    result = "md5: " + md5(data.encode()).hexdigest()
    return result


def hash_sha256(data):
    result = "sha256: " + sha256(data.encode()).hexdigest()
    return result


def hello(data):
    result = "Your message: " + data + " Time: " + str(datetime.datetime.now())
    return result


def hello_person(person, data):
    result = str(person) + " your message: " + str(data) + " Time: " + str(datetime.datetime.now())
    return result
