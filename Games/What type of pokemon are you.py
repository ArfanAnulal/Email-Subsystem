from time import sleep
import webbrowser
import random
print('Welcome to "What type of pokemon are you?"');sleep(1)

while True: #Game continue loop
  input('Enter your name?: ')
  input('Enter your year of birth?: ')
  input('Enter your favourite colour?: ')
  input('Enter your favourite number?: ')
  input('What is your primary hand?: ')
  input('Are you athletic?: ')
  input('Are you a vegetarian?: ')
  input('Are you impatient?: ')
  input('You walk down a dark alleyway and see a man get attacked, what do you do?: ')
  input('Do you prefer day or night?: ')
  gen1no=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]
  gen1pok=["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
  n=random.choice(gen1no)
  p=gen1pok[n-1]
  print("\nFinding the perfect pokemon for you",end='');sleep(0.5)
  print('.',end='');sleep(0.5)
  print('.',end='');sleep(0.5)
  print('.',end='');sleep(0.5)
  print('.');sleep(0.5)
  print("\nPokedex Number:",n);sleep(1)
  print("Pokemon:",p);sleep(1)
  yeno=str(input('Do you want to know more about this pokemon?:'))
  if yeno== 'Yes' or yeno=='yes' or yeno== 'YES' or yeno=='yES' or yeno=='y':
    decoy=1;sleep(0.5)   
    print('You will now be redirected to an external website');sleep(0.7)
    print('A project by GamerBro6q7');sleep(2.5)
    webbrowser.open('https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon#Bulbasaur')
    break
  elif yeno== 'No' or yeno=='no' or yeno=='NO' or yeno=='nO' or yeno=='n':
      print('Thank you for playing!');sleep(0.7)
      break


