from random import random

def request_file_api(query):
    print(f"{query} is runing")
    if(int(random() * 100) < 50):
        request_resolve(query)
    else:
        request_reject(query)

def request_reject(query):
    print(f"your request {query} has be reject")


def request_resolve(query):
    print(f"your request {query} has be resolve")


if(__name__ == "__main__"):
    request_file_api("TEST")

