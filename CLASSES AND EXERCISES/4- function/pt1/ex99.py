# analisar números e dizer qual o maior
def valores(* num):
    print("-=-"*15)
    print(f"{num} -> foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {max(num)}")
    

valores(1,2,3,5)
valores(9,8,7)
valores(1,5,6,8,4,6)