import boto3

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket']
    
    # Proceso
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=bucket_name)
    
    # Salida
    return {
        'statusCode': 200,
        'message': f"Bucket '{bucket_name}' creado exitosamente",
        'response': response
    }
