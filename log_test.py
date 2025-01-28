from loguru import logger

# Configuração do Loguru - Log em arquivo e no console
logger.add("logs/app.log", rotation="500 KB", retention="7 days", level="INFO")

# Exemplos de logs em diferentes níveis
logger.debug("Isso é um log de depuração (DEBUG)")
logger.info("O sistema iniciou com sucesso! (INFO)")
logger.warning("Aviso: Entrada de dados inesperada (WARNING)")
logger.error("Erro ao conectar ao banco de dados! (ERROR)")
logger.critical("Falha crítica! O sistema será encerrado. (CRITICAL)")


# Captura automática de exceções com Loguru
@logger.catch
def divisao_por_zero():
    return 1 / 0  # Isso gerará um erro capturado automaticamente

divisao_por_zero()

# Exemplo de log em loop (Emulando processamento de arquivos)
logger.info(f"Iniciando processamento de arquivos")
for file in range(10):
    logger.info(f"Arquivo {file} processado com sucesso")
    file += 1
