import boto3

def lambda_handler(event, context):
    # Entrada
    bucket_name = event['body']['bucket']
    folder_name = event['body']['folder']
    
    # Proceso
    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=bucket_name, Key=(folder_name + '/'))

    # Salida
    return {
        'statusCode': 200,
        'message': f"Carpeta '{folder_name}' creada en el bucket '{bucket_name}'",
        'response': response
    }
