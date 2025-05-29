from datetime import datetime

def ordenar_emergencias(emergencias):
    # Converte os horários de chegada para objetos datetime para facilitar a ordenação
    def chave_ordenacao(e):
        urgencia, horario = e
        horario_dt = datetime.strptime(horario, "%H:%M")
        return (-urgencia, horario_dt)  # Urgência decrescente, horário crescente

    return sorted(emergencias, key=chave_ordenacao)

# Exemplo
emergencias = [
    (3, "10:30"),
    (5, "10:45"),
    (5, "10:15"),
    (2, "10:20"),
    (3, "10:00")
]

emergencias_ordenadas = ordenar_emergencias(emergencias)
print("Ordem de atendimento:")
for urgencia, horario in emergencias_ordenadas:
    print(f"Urgência: {urgencia}, Horário: {horario}")
