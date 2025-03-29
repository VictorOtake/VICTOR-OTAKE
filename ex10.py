total_compra=float(input("insira total da compra: ")) 
if total_compra>=100.00: 
    desconto=total_compra*0.10 
    print(f"o valor total da compra {total_compra}, mas com o desconto agora o valor é 
{total_compra-desconto}") 
else: 
    print(f"valor minimo não atingido para o desconto, valor da compra é R${total_compra}")