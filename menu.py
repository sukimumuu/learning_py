import menu_start

# Pilih menu
def choose_menus():
    option = [   
        "1. Mulai Permainan",
        "2. Muat Permainan",
        "3. Tentang",
        "4. Keluar",
    ]
    
    for opsi in option:
       choose_option = print(opsi)
    
    num_choose = int(input("Pilih menu : "))
    menus(num_choose)
    
# Aksi pilih menu
def menus(num_choose):
    match num_choose:
        case 1:
            menu_start.start_slash()
        case _:
            return "Anomali detected"

    
    