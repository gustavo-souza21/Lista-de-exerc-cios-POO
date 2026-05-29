from notificador import NotificadorEmail, NotificadorSMS, NotificadorApp
from central import CentralNotificacoes

central = CentralNotificacoes()

central.adicionar_notificador(NotificadorEmail("gustavo@ufam.edu.br"))
central.adicionar_notificador(NotificadorSMS("+55 92 99999-0000"))
central.adicionar_notificador(NotificadorApp("gustavo_icet"))

central.enviar_para_todos("Sua prova foi agendada para amanhã às 08h.")
