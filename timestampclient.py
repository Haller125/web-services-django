import thriftpy2
from thriftpy2.rpc import make_client
from thriftpy2.thrift import TException

timestamp_thrift = thriftpy2.load("timestamp_service/timestamp_service.thrift", module_name="timestamp_thrift")
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
