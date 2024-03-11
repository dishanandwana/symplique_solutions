from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ReminderSerializer
from rest_framework.exceptions import ValidationError


class ReminderList(APIView):
    def post(self, request, format=None):
        try:
            serializer = ReminderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
