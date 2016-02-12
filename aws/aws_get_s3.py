from boto3.session import Session

# AWS workspace credentials
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = 'us-east-1'

# Model Info
aws_model_id = ''
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
aws_data_source_id = ''
aws_evaluation_id = ''

aws_session = Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

aws_client = aws_session.resource('s3')
aws_client.meta.client.download_file('dojodemo', 'titanic.csv', 'C:/Users/Phuc H Duong/Downloads/titanic.csv')
print("done")
