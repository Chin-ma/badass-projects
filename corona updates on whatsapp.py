import sys
sys.path.append('..')
from coronavirus_updates import corona_info
from whatsapp_automation import whats_automater

info_getter = corona_info()
t_cases = info_getter.total_cases_india
inc_cases = info_getter.increased_cases

sender = whats_automater()
sender.send_someone('chiniboy')
sender.send_message(f'''coronavirus cases in india today: {t_cases}
coronavirus cases increased from yesterday: {inc_cases}''')


