import boto3
from boto3.dynamodb.conditions import Key, Attr
GATE_TABLE_PK = 'id'

store_id = 'store001'
date = '20200221'
STATUS_ENTER = 'enter'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SessionTable')

ke = Key(GATE_TABLE_PK).eq(store_id + '/' + date + '/' + STATUS_ENTER)
fe = Attr('isExited').eq(False)
response = table.query(
    KeyConditionExpression=ke
    , FilterExpression=fe
)
print(response[u'Items'])
