from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import ( HTTP_200_OK, 
                                    HTTP_201_CREATED, 
                                    HTTP_400_BAD_REQUEST, 
                                    HTTP_405_METHOD_NOT_ALLOWED)
from apps.users.models import User
from .serializers import UserSerializer, TestUserSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    """
        Vista para obtener lista de usuarios y crear usuario
    """
    if request.method == 'GET':
        users = User.objects.all()
        
        #prueba
        # test_user = {
        #     'name' : 'lobito',
        #     'email' : 'lobillo@gmail.com'
        # }
        # test_user_serializer = TestUserSerializer(data=test_user)
        # if test_user_serializer.is_valid():
        #     test_user_serializer.save()
        # else:
        #     return Response({'message': test_user_serializer.errors}, status=HTTP_400_BAD_REQUEST)
        # #fin de prueba
        
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data, status=HTTP_200_OK)

         
    if request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status = HTTP_400_BAD_REQUEST)
    return Response(status=HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request, user_id = None):
    """
    Vista para obtener, actualizar y eliminar un usuario específico.
    """
    user = User.objects.filter(id = user_id).first()
    if user:
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=HTTP_200_OK)    
        if request.method == 'PUT':
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=HTTP_200_OK)
            return Response(user_serializer.errors, status=HTTP_400_BAD_REQUEST)       
        if request.method == 'DELETE':
            user.delete()
            return Response({'message': 'Eliminado exitosamente'}, status=HTTP_200_OK)
    return Response({'message': 'No se a encontrado el usuario con esos datos'}, status=HTTP_400_BAD_REQUEST)