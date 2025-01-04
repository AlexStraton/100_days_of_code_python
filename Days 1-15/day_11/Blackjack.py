from art import logo
from random import choice


print(logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


player = True
player_cards= []
computer_cards = []
is_blackjack = False
#total_below_17 = sum(player_cards) < 17




def hand_card():
  random_card = choice(cards)
  if player:
      player_cards.append(random_card)
  else:
      computer_cards.append(random_card)




def check_over_21(array):
  if player:
      if sum(array) > 21:
          print("You went over! You lost!")
          print("\n" * 3)
  else:
      print("Computer went over! You win")
      print("\n" * 3)




def check_win(player_arr, comp_arr):
  if sum(player_arr) > sum(comp_arr):
      print("CONGRATULATIONS! YOU WIN")
  elif sum(player_arr) == sum(comp_arr):
      print("OH DEAR, IT'S A DRAW!")
  else:
      print("COMPUTER WON! BETTER LUCK NEXT TIME")


#player deal;
hand_card()
hand_card()
#computer deal
player = False
hand_card()


initial_q = input("Do you want to play Blackjack? Type 'y' or 'n': ")
print(initial_q)


if initial_q.lower() == 'y':
  while True:
      total_player = sum(player_cards)
      total_computer = sum(computer_cards)
      print(f"Your cards: {player_cards}, current score: {total_player}")
      print(f"Computer's first card: {computer_cards}")
      player = True
      if total_player == 21:
          print("You got 21! You WON!!!!")
          break
      if total_player > 21:
           print("You went over 21! You lost!")
           break
      another_card = input("Type 'y' to get another card, or 'n' to pass: ")
      print(another_card)
      if another_card.lower() == 'y':
              #player continues drawing
           hand_card()
           if total_player == 21:
               print("You got 21! You WON!!!!")
               break
      else:
          #computer plays
          player = False
          while total_computer < 17:
               hand_card()
               total_computer = sum(computer_cards)
               if total_computer == 21:
                   print("Computer got 21! You LOST!!!!")
                   break


          print(f"Your final cards: {player_cards}, final score: {total_player}")
          print(f"Computer's final hand: {computer_cards}, final score: {total_computer}")


          if total_computer > 21:
              print("Computer went over 21! You WON!")
              break
          check_win(player_cards, computer_cards)
          break
else:
  print("No worries. Goodbye!")

