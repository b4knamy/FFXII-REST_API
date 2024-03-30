from .models import Character, Esper
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CharacterSerializer, EsperSerializer

# Create your views here.

@api_view(['GET'])
def get_all_char(req):

    if req.method == 'GET':
        
        if req.GET:
            try:
                limit = int(req.GET['limit'])
                if limit == 0:
                    return Response(status=status.HTTP_411_LENGTH_REQUIRED)
                chars = Character.objects.all()[:limit]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            serializer = CharacterSerializer(chars, many=True)

            return Response(serializer.data)
        
        else:
            chars = Character.objects.all()

            serializer = CharacterSerializer(chars, many=True)

            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_filter_char(req):
    if req.method == 'GET':

        keys_all = req.GET
        if len(keys_all) == 1:
            try:

                keys = list(zip(keys_all))
                key = keys[0][0]
                valor = keys_all[key]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
                
            match key:
                case 'name':
                    chars = Character.objects.filter(pk=valor.capitalize())
                case 'race':
                    chars = Character.objects.filter(race=valor.capitalize())
                case 'hometown':
                    chars = Character.objects.filter(hometown=valor.capitalize())
                case 'age':
                    chars = Character.objects.filter(age=valor.capitalize())
                case 'char_type':
                    chars = Character.objects.filter(char_type=valor.capitalize())
                case _:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                
            if len(chars) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            serializer = CharacterSerializer(chars, many=True)

            return Response(serializer.data)


                
        elif len(keys_all) == 2:
        
            try:
                keys = list(zip(keys_all))
                key = keys[0][0]
                valor = str(keys_all[key])
                limit = int(keys_all['limit'])
                if limit == 0:
                    return Response(status=status.HTTP_411_LENGTH_REQUIRED)
                
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            match key:
                case 'name':
                    chars = Character.objects.filter(pk=valor.capitalize())[:limit]
                case 'race':
                    chars = Character.objects.filter(race=valor.capitalize())[:limit]
                case 'hometown':
                    chars = Character.objects.filter(hometown=valor.capitalize())[:limit]
                case 'age':
                    chars = Character.objects.filter(age=valor.capitalize())[:limit]
                case 'char_type':
                    chars = Character.objects.filter(char_type=valor.capitalize())[:limit]
                case _:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            
            if len(chars) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
            serializer = CharacterSerializer(chars, many=True)

            return Response(serializer.data)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_all_esper(req):

    if req.method == 'GET':
        
        if req.GET:
            try:
                limit = int(req.GET['limit'])
                if limit == 0:
                    return Response(status=status.HTTP_411_LENGTH_REQUIRED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


            espers = Esper.objects.all()[:limit]

            serializer = EsperSerializer(espers, many=True)

            return Response(serializer.data)
        
        else:
            espers = Esper.objects.all()

            serializer = EsperSerializer(espers, many=True)

            return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_filter_esper(req):
    if req.method == 'GET':

        keys_all = req.GET
        if len(keys_all) == 1:
            try:
                keys = list(zip(keys_all))
                key = keys[0][0]
                valor = keys_all[key]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
                
            match key:
                case 'name_esper':
                    espers = Esper.objects.filter(pk=valor.capitalize())
                case 'sign':
                    espers = Esper.objects.filter(sign=valor.capitalize())
                case 'element':
                    espers = Esper.objects.filter(element=valor.capitalize())
                case _:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                
            if len(espers) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
                
            serializer = EsperSerializer(espers, many=True)

            return Response(serializer.data)


                
        elif len(keys_all) == 2:
        
            try:
                keys = list(zip(keys_all))
                key = keys[0][0]
                valor = str(keys_all[key])
                limit = int(keys_all['limit'])
                if limit == 0:
                    return Response(status=status.HTTP_411_LENGTH_REQUIRED)
                
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            match key:
                case 'name_esper':
                    espers = Esper.objects.filter(pk=valor.capitalize())[:limit]
                case 'sign':
                    espers = Esper.objects.filter(sign=valor.capitalize())[:limit]
                case 'element':
                    espers = Esper.objects.filter(element=valor.capitalize())[:limit]
                case _:
                    Response(status=status.HTTP_400_BAD_REQUEST)

            if len(espers) == 0:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = EsperSerializer(espers, many=True)

            
                

            return Response(serializer.data)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)



