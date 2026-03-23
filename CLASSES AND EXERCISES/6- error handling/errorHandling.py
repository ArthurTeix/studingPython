try: # try = estou dixendo a linguagem "tente fazer isso"
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b

# except = "faça isso se der errado" (posso ter varios 'except')
# except Exception as erro: # usando a classe 'Exception' posso mostrar o tipo de erro (posso usar na hora de programar)
    # print(f"Houve um erro: {erro.__class__}")

except (ValueError, TypeError): # posso especificar qual o tipo do erro
    print("Tivemos um problema com o tipo de dado que você inseriu!")
    
except ZeroDivisionError:
    print("Não é possível dividir por zero!")

except KeyboardInterrupt:
    print("\nO usuário preferiu não informar os dados!")

else: # else = "faça isso se der certo" (opcional)
    print(f"O resultado é {r:.1f}")

finally: # finally = vai acontecer independente de dar certo ou errado, é o "finalmente" (opcional)
    print("Programa concluído!")