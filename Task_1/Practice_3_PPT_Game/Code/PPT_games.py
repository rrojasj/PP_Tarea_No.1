from pptg_functions import *

print("\nBienvenidos al juego del año - Piedra, Papel y Tijera\n")

player_1 = {}
player_2 = {}

input("Jugador 1 su turno, presione 'Enter' para iniciar y a Divertirse!!\n")
player_1 = get_player_1_data()

input("\nJugador 2 su turno, presione 'Enter' iniciar y a Divertirse!!\n")
player_2 = get_player_2_data()

print(f"\nSelección del jugador 1 - usuario: {player_1['username']}")
print(f"-  {player_1['choice']}: {player_1['choice_name']}\n")

print(f"Selección del jugador 2 - usuario: {player_2['username']}")
print(f"-  {player_2['choice']}: {player_2['choice_name']}\n")

msg = verify_winner(player_1, player_2)

print("\nMuchas gracias por participar.")
print(f"{msg}\n")