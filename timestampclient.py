import thriftpy
from thriftpy.rpc import make_client
from thriftpy.thrift import TException

timestamp_thrift = thriftpy.load("timestamp_service/timestamp_service.thrift", module_name="timestamp_thrift")
Timestamp_service = timestamp_thrift.TimestampService

def get_thrift_timestamp():
    try:
        client = make_client(Timestamp_service, 'localhost', 10000)
        result = client.getCurrentTimestamp()
        return result
    except TException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print(get_thrift_timestamp())
