from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status  # Untuk mengatur kode status HTTP

@api_view(['GET', 'POST'])  # Tambahkan 'POST' sebagai metode yang diizinkan
def getData(request):
    if request.method == 'GET':
        person = {'id': 1, 'name': 'Dennis'}
        return Response(person)
    elif request.method == 'POST':
        data = request.data  # Mengambil data yang dikirimkan melalui POST request
        # Di sini Anda dapat memproses data yang diterima dan memberikan respons sesuai
        print(data)
        return Response(data, status=status.HTTP_201_CREATED)  # Contoh: HTTP 201 Created
