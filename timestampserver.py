import thriftpy
from thriftpy.rpc import make_server
import datetime
import os
import sys


timestamp_thrift = thriftpy.load("timestamp_service/timestamp_service.thrift", module_name="timestamp_thrift")

Timestamp_service = timestamp_thrift.TimestampService

class TimestampServiceHandler:
    def getCurrentTimestamp(self):
        current_time = datetime.datetime.utcnow()
        return f"{current_time}"

def run_server():
    handler = TimestampServiceHandler()
    server = make_server(Timestamp_service, handler, 'localhost', 10000)
    server.serve()


if __name__ == "__main__":
    run_server()
