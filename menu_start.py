from util import equallines, clear_screen
import save_profil_sow

# Aksi menu : 1
def start_slash():
    clear_screen.clean_view()
    equallines.eqlines(37)
    equallines.titleline(10, "Mulai Permainan")
    equallines.eqlines(37)
    name = input('Masukkan nama user kamu : ')
    save_profil_sow.save_session_profil(name)