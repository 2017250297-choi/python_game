
from characters import *
from manager import *


window_=WindowManager()
player_name=window_.name_input()
class_name=window_.choose_class()
player_entity=make_player(player_name,class_name)
enemy=make_monster()
sleep(1)
window_.clear_all()
print("==================\nBattle Start!\n==================")
sleep(1.3)
window_.battle_window(player_entity,enemy)
