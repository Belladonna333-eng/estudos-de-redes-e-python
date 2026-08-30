medida = input("Selecione a medida de seu arquivo(ex:MB,KB,Mb,GB): ")
quantidade=float(input("Qual o tamanho do arquivo?: "))
banda = float(input("qual a largura de banda?(Mbps): "))
if medida == "MB":
    conversao = quantidade*8 #de MB para Mb
    tempo = conversao/banda
    if tempo > 60:
        tempo = tempo/60
        print(f"tempo estimado para download:{tempo:.2} min")
    else:
     print(f"tempo estimado para download:{tempo:.2} seg")
if medida == "KB":
    conversao = quantidade/125 #de KB par Mb
    tempo = conversao/banda
    if tempo > 60:
        tempo = tempo/60
        print(f"tempo estimado para download:{tempo:.2} min")
    else:
        print(f"tempo estimado para download:{tempo:.2} seg")

if medida == "Mb":
     tempo = quantidade/banda
     if tempo>60:
          tempo = tempo/60
          print(f"o tempo estimado para download:{tempo:.2f} min")
     else:
         print(f"tempo estimado para download:{tempo:.2f} seg")
if medida =="GB":
    conversao= quantidade*1024*8
    tempo = conversao/banda
    if tempo>60:
        tempo=tempo/60
        print(f"tempo estimado para download:{tempo:.2f} min ")
    else:
        print(f"tempo estimado para download:{tempo:.2f} seg ")