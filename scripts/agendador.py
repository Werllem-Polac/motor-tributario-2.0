import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apscheduler.schedulers.blocking import BlockingScheduler
from aprendizado_diario.run_diario import executar_pipeline

scheduler = BlockingScheduler()

scheduler.add_job(executar_pipeline, "cron", hour=2, minute=0)

print("⏱️ Agendador iniciado. Aguardando próxima execução...")
scheduler.start()
