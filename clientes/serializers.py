from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve possuir a formatação: 123.456.789-01'})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome precisa conter apenas letras'})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter pelo menos 7 dígitos'})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve possuir a formatação: 83 91234-5678'})
        
        return data