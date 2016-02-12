from boto3.session import Session

# AWS workspace credentials
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = 'us-east-1'

# Model Info
aws_model_id = 'ml-Z1MQuoufJHR'
aws_model_endpoint = 'https://realtime.machinelearning.us-east-1.amazonaws.com'
aws_model_data = {
    'PassengerId': '',
    'Survived': '',
    'Pclass': '1',
    'Name': '',
    'Sex': 'male',
    'Age': '24',
    'SibSp': '0',
    'Parch': '0',
    'Ticket': '',
    'Fare': '22',
    'Cabin': '',
    'Embarked': 'C',
}
aws_data_source_id = 'ab4c0fed-9092-4fec-8792-2207b2d412ab'

aws_session = Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

aws_ml = aws_session.client('machinelearning')

response = aws_ml.get_data_source(
    DataSourceId=aws_data_source_id,
    Verbose=True
)

print(response)
