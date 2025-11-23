"""
COMP.CS.100 Blackjack peli
Creator: Elias Ahonen <elias.ahonen@tuni.fi>
Student id number: 151845334

Käyttöohjeet:

Tämä projekti on luomus korttipelistä Blackjack. Pelissä voi olla useampi
pelaaja, mutta pelaajat eivät pelaa keskenään, vaan aina jakajaa (dealeria)
vastaan. Aluksi kaikille pelaajille jaetaan kaksi korttia, joista jakajalla
toinen on väärinpäin. Kukin pelaaja vuorollaan joko ottaa uuden kortin (Hit) tai
pitää kortti kätensä ennallaan ja antaa vuoronsa seuraavalle pelaajalle (stand).

Pelin tavoitteena on saada mahdollisimman suuri korttien yhteislukema, mutta
kuitenkin niin, että yhteislukema on alle 21. Jos yhteislukema menee yli 21,
pelaaja häviää (bust). Kuvakortit ovat lukemaltaan 10 ja kuvattomat oman
numeronsa verran. Poikkeuksena on ässä.

Ässä voi olla lukemaltaan joko 1 tai 11. Kun saat ensimmäisen ässäsi lukema on
11 ja sinun kätesi/korttisi on ns. soft hand. Tämä tarkoittaa sitä, että kun
lukemasi olisi menossa kortin noston jälkeen yli 21, ensimmäinen ässä
muuttuukin lukemaksi 1 ja kätesi muuttuu hard handiksi. Nyt kun saat seuraavan
kerran ässän se on aina 11 ja ei voi enää muuttua ykköseksi.

Käyttöliittymässä on aina jokaisen pelaajan alla kaksi nappulaa, jotka toimivat
hit ja stand nappuloina. Kun kaikki pelaajat ovat päättäneet vuoronsa, on jakajan
vuoro. Hän nostaa kortteja niin kauan kun, hänen yhteislukemansa on alle 17.
Jakajaan pätee samat säännöt korteista. Peliä siis pelataan aina jakajaa vastaan
ja sen voi voittaa, jos jakaja bustaa tai, että kumpikaan ei bustaa,
mutta pelaajan yhteislukema on enemmän kuin jakajan. Tämän on tarkoitus olla
kehittynyt versio graafisesta käyttöliittymästä.
"""

from random import *
from tkinter import *


# Jokaisella kortilla on oma numeronsa väliltä 1-52, alaspäin olevalla on numero 0.
# Tämän listan avulla voidaan arvottu numero liittää korttiin. Listassa on 53
# alkiota, jotka ovat listoja, jotka taas sisältävät kortin arvon.
CARD_LIST = [["XX", 0], ["A♤", 11], ["2♤", 2], ["3♤", 3], ["4♤", 4], ["5♤", 5], ["6♤", 6], ["7♤", 7], ["8♤", 8], ["9♤", 9], ["10♤", 10], ["J♤", 10], ["Q♤", 10], ["K♤", 10],
             ["A♣", 11], ["2♣", 2], ["3♣", 3], ["4♣", 4], ["5♣", 5], ["6♣", 6], ["7♣", 7], ["8♣", 8], ["9♣", 9], ["10♣", 10], ["J♣", 10], ["Q♣", 10], ["K♣", 10],
             ["A♠", 11], ["2♠", 2], ["3♠", 3], ["4♠", 4], ["5♠", 5], ["6♠", 6], ["7♠", 7], ["8♠", 8], ["9♠", 9], ["10♠", 10], ["J♠", 10], ["Q♠", 10], ["K♠", 10],
             ["A♦", 11], ["2♦", 2], ["3♦", 3], ["4♦", 4], ["5♦", 5], ["6♦", 6], ["7♦", 7], ["8♦", 8], ["9♦", 9], ["10♦", 10], ["J♦", 10], ["Q♦", 10], ["K♦", 10]]

# Tämä sekasorto on erikseen ennalta määrätyt pelaajien sijainnit peli-ikkunassa
# Mainitsemisen arvoista on ainakin se, että sanakirjan sisällä olevan listan
# sisällä olevat sanakirjat ovat pelaajien nimen sijainnit pelissä, jossa on
# 1, 2, 3, 4 tai 5 pelaajaa. Muiden widgettien sijainnit määräytyvät aina näiden
# mukaan, joten niitä ei tarvitse tähän kirjoittaa.
PLAYER_POSITIONS = {"Player1": [{"name_x": 360, "name_y": 400},
                                {"name_x": 460, "name_y": 400},
                                {"name_x": 560, "name_y": 400},
                                {"name_x": 638, "name_y": 350},
                                {"name_x": 660, "name_y": 350}],
                    "Player2": [{},
                                {"name_x": 260, "name_y": 400},
                                {"name_x": 360, "name_y": 450},
                                {"name_x": 458, "name_y": 400},
                                {"name_x": 510, "name_y": 400}],
                    "Player3": [{},
                                {},
                                {"name_x": 160, "name_y": 400},
                                {"name_x": 264, "name_y": 400},
                                {"name_x": 360, "name_y": 450}],
                    "Player4": [{},
                                {},
                                {},
                                {"name_x": 84, "name_y": 350},
                                {"name_x": 210, "name_y": 400}],
                    "Player5": [{},
                                {},
                                {},
                                {},
                                {"name_x": 60, "name_y": 350}],
                    "Dealer": [{"name_x": 360, "name_y": 50},
                               {"name_x": 360, "name_y": 50},
                               {"name_x": 360, "name_y": 50},
                               {"name_x": 360, "name_y": 50},
                               {"name_x": 360, "name_y": 50}]}


# nimi fontti, jota käytetään
name_font = ("Courier New", 14)

# muita vakioita, joita käytetään väreinä
active_bg = "#313131"
bg = "#222222"
fg = "#ff5656"


class UserInterface:

    def __init__(self, list_of_players):

        self.__ui = Tk()
        self.__ui.minsize(800, 900)
        self.__ui.maxsize(800, 900)
        self.__min_players = 1
        self.__players = 5
        self.__max_players = 5

        self.__ui.iconbitmap("g59.ico")
        self.__ui.title("Blackjack")

        # käyttöliittymän widgettejä, joita ei tarvitse muuttaa
        self.__start_button = None
        self.__new_game_button = None
        self.__quit_button = None
        self.__information_label = None
        self.__small_info_label = None
        self.__right_arrow_button = None
        self.__left_arrow_button = None
        self.__players_label = None
        self.__restart_button = None
        self.__background = None
        self.__bg_image_label = None
        self.__bg_image = None

        # lista pelaaja olioista
        self.__list_of_players = list_of_players

        # lisätään listaan jokainen kortin kuva
        self.__image = None
        self.__image_list = []
        for number in range(53):
            card_image = PhotoImage(file=f"{number}.png")
            self.__image_list.append(card_image)

        # tämä on pelaajan nimen label
        self.__name_label = None

        # korttien yhteislukeman label, jotka lisätään myöhemmin listaan
        self.__total_value_label = None
        self.__list_of_total_value_labels = []

        # napit
        self.__hit_button = None
        self.__stand_button = None
        self.__list_of_buttons = []

        # player card on label pelikortin kuvalle. Nämäkin lisätään listaan
        # myöhempää tarkoitusta varten
        self.__player_card = None
        self.__list_of_card_labels = []

        # labeli jokaiselle pelaaja, joka kertoo hävisikö tämä vai voittiko
        self.__win_label = None

        # kutsutaan metodi, joka aloittaa uuden pelin
        self.new_game()
        self.__ui.mainloop()

    def prepare_permanent_widgets(self):
        """ Tässä asetellaan widgetit, joiden paikkaa tai parametreja ei tarvi
        sen kummemmin muuttaa

        :return:
        """
        self.__background = Label(bg=bg, padx=800, pady=900)
        self.__background.place(x=0, y=0)

        self.__bg_image = PhotoImage(file="bjaloitusruutu.png")
        self.__bg_image_label = Label(image=self.__bg_image, bg=bg)
        self.__bg_image_label.place(x=400, y=325, anchor=CENTER)

        self.__start_button = Button(text="Start Game", command=self.start,
                                     bg=bg, fg=fg, bd=5,
                                     activebackground=active_bg)
        self.__start_button.place(x=400, y=812, anchor=CENTER)

        self.__new_game_button = Button(text="New Game", command=self.new_game,
                                        state=DISABLED, bg=bg, fg=fg, bd=5,
                                        activebackground=active_bg)
        self.__new_game_button.place(x=400, y=846, anchor=CENTER)

        self.__quit_button = Button(text="Quit", command=self.quit_game,
                                    padx=18, bg=bg, fg=fg, bd=5,
                                    activebackground=active_bg)
        self.__quit_button.place(x=400, y=880, anchor=CENTER)

        self.__restart_button = Button(text="Restart", command=self.restart,
                                       padx=12, bg=bg, fg=fg, bd=5,
                                       activebackground=active_bg)

        self.__information_label = Label(font=name_font, bg=bg, fg=fg, bd=5,
                                         activebackground=active_bg)
        self.__information_label.place(x=400, y=15, anchor=CENTER)

        self.__small_info_label = Label(bg=bg, fg="white")
        self.__small_info_label.place(x=400, y=37, anchor=CENTER)

        self.__right_arrow_button = Button(text=">", command=self.right_arrow,
                                           bg=bg, fg=fg, bd=5,
                                           activebackground=active_bg)
        self.__right_arrow_button = Button(text=">", command=self.right_arrow,
                                           bg=bg, fg=fg, bd=5,
                                           activebackground=active_bg)
        self.__right_arrow_button.place(x=780, y=880, anchor=CENTER)

        self.__left_arrow_button = Button(text="<", command=self.left_arrow,
                                          bg=bg, fg=fg, bd=5,
                                          activebackground=active_bg)
        self.__left_arrow_button.place(x=680, y=880, anchor=CENTER)

        self.__players_label = Label(text=f"Players: {self.__players}",
                                     background="white", relief=RAISED,
                                     padx=6, pady=4, bg=bg, fg=fg, bd=5,
                                     activebackground=active_bg)
        self.__players_label.place(x=730, y=880, anchor=CENTER)

    def new_game(self):
        """ tällä metodilla luodaan aina uusi peli

        :return:
        """

        # tuhotaan vanhat widgetit
        for widget in self.__ui.winfo_children():
            widget.destroy()

        self.prepare_permanent_widgets()

        # Koska pelaajien vaihto nappulat käyttävät tätä metodia ja pelissä on
        # maksimi ja minimi pelaaja määrä, täytyy tämä pätkä olla tässä
        if self.__players == self.__min_players:
            self.__left_arrow_button.configure(state=DISABLED)
        elif self.__players == self.__max_players:
            self.__right_arrow_button.configure(state=DISABLED)

        self.__information_label.configure(text="Press Start Game to start!")

        # tyhjennetään listat vanhoista widgeteistä
        self.__list_of_card_labels = [[], [], [], [], [], []]
        self.__list_of_buttons = []
        self.__list_of_total_value_labels = []
        self.position_player_widgets()

    def position_player_widgets(self):
        """ Tämä metodi alustaa kaikki pelaajien widgetit paikoilleen uutta
        peliä varten.

        :return:
        """

        # jokaiselle pelaajalle yksi kerrallaan
        for number in range(self.__players + 1):
            if number == 0:
                player_name = "Dealer"
            else:
                player_name = f"Player{number}"

            # määritellään kaikkien widgettien paikat
            name_x = PLAYER_POSITIONS[player_name][self.__players - 1]["name_x"]
            name_y = PLAYER_POSITIONS[player_name][self.__players - 1]["name_y"]
            total_value_x = name_x
            total_value_y = name_y + 110
            card_x = name_x + 45
            card_y = name_y + 30
            card_offset = 60  # viereisten korttien etäisyys toisistaan
            true_offset = 0  # apumuuttuja, jolla kortit asetellaan vierekkäin

            # Asetetaan nimet paikalleen
            self.__name_label = Label(text=f"{player_name}:",
                                      font=name_font, bg=bg, fg="white")
            self.__name_label.place(x=name_x, y=name_y)

            # Asetetaan yhteislukema label paikalleen
            self.__total_value_label = Label(text=f"Total value: 0", bg=bg,
                                             fg="white")
            self.__list_of_total_value_labels.append(self.__total_value_label)
            self.__total_value_label.place(x=total_value_x, y=total_value_y)

            # Asetetaan kortit paikalleen
            for i in range(2):
                # kortti on alaspäin aina tässä vaiheessa
                card_image = self.__image_list[0]
                self.__player_card = Label(image=card_image, bg=bg)
                self.__player_card.place(x=card_x - true_offset, y=card_y)
                true_offset += card_offset

            # Lyönti ja standi napitkin luodaan jo, mutta ei vielä aseteta
            self.__hit_button = Button(text="Hit", padx=17,
                                       command=self.player_hit, state=DISABLED,
                                       bg=bg, fg=fg, bd=5,
                                       activebackground=active_bg)
            self.__stand_button = Button(text="Stand", padx=10,
                                         command=self.player_stand,
                                         state=DISABLED, bg=bg, fg=fg, bd=5,
                                         activebackground=active_bg)
            self.__list_of_buttons.append([self.__hit_button,
                                           self.__stand_button])

    def update_player_widgets(self, player):
        """ Päivittää tietyn pelaajan kaikki tarvittavat widgetit. Käytännössä
        sama kuin position_player_widgets, mutta pienillö muutoksilla

        :param player: Player, pelaaja olio, jota päivitellää
        :return:
        """

        player_index = self.__list_of_players.index(player)  # pelaajan numero
        player_name = player.get_name()
        name_x = PLAYER_POSITIONS[player_name][self.__players - 1]["name_x"]
        name_y = PLAYER_POSITIONS[player_name][self.__players - 1]["name_y"]
        card_x = name_x + 45
        card_y = name_y + 30
        total_value_x = name_x
        total_value_y = name_y + 110
        hit_x = total_value_x + 10
        hit_y = total_value_y + 25
        stand_x = hit_x
        stand_y = hit_y + 34

        cards = player.get_cards()


        # oikea lista, johon pelaajan kortit tallennetaan
        card_labels = self.__list_of_card_labels[player_index]
        card_index = 1  # card_index kuvaa kuinka mones kortti on kädessä,
        # listojen kanssa tästä vakiosta poistetaan jatkossa aina yksi, koska
        # listat alkavat nollasta

        # säännönmukainen logiikka, jolla asetellaan kortit oikeille paikoille
        # card on tässä kontekstissa luku väliltä 1-52
        for card in cards:
            card_offset_x = -60  # korttien etäisyys x-suunnassa
            card_offset_y = 80  # ja y-suunnassa
            if card_index == 1:
                card_offset_x = 0
            elif card_index % 2 == 1:
                card_offset_x = -30
            card_offset_y *= (card_index // 2.1)

            # määritellään kortille kuva
            image = self.__image_list[card]
            self.__player_card = Label(image=image, bg=bg)
            # koska listassa ei vielä ole ollenkaan kortteja, tallennetaan aina
            # uusin kortti sinne.
            if len(card_labels) + 1 == card_index:
                card_labels.append(self.__player_card)

            # Jotta jakajan toinen kortti päivittyisi myös listaan, kun se
            # paljastetaan, täytyy tämän olla tässä, kömpelö mutta toimii
            if card_index == 2 and player_name == "Dealer":
                card_labels[1] = self.__player_card
            card_labels[card_index - 1].place(x=card_x + card_offset_x,
                                              y=card_y + card_offset_y)

            # joskus edellistä korttia täytyy hieman siirtää
            if card_index % 2 == 0 and card_index != 2:
                card_to_move = card_labels[card_index - 2]
                card_to_move.place(x=card_x, y=card_y + card_offset_y)
            card_index += 1

        # päivitellään yhteislukema
        player_total_value = player.get_total_card_value()
        total_value_label = self.__list_of_total_value_labels[player_index]
        if player.get_softness():
            # soft-handilla näytetään molemmat vaihtoehdot yhteislukemalle
            total_value_label.configure(
                text=f"Total value: {player_total_value - 10}/"
                     f"{player_total_value}")
        else:
            total_value_label.configure(
                text=f"Total value: {player_total_value}")

        # sijoitellaan napit
        buttons = self.__list_of_buttons[player_index]
        total_value_label.place(x=total_value_x,
                                       y=total_value_y + card_offset_y)
        if player.get_name() != "Dealer" and not check_bust(player):
            buttons[0].place(x=hit_x, y=hit_y + card_offset_y)
            buttons[1].place(x=stand_x, y=stand_y + card_offset_y)

    def start(self):
        """ Aloitus metodi. Tätä kutsutaan, kun painetaan start game.

        :return:
        """
        self.restart_button_manager(True)
        self.game_starter()
        self.__start_button.configure(state=DISABLED)

    def restart_button_manager(self, boolean):
        """ Metodi, jolla hallinnoidaan restart-napin olemassa oloa

        :param boolean: bool, jos halutaan, että nappi näkyy true ja toisinpäin
        :return:
        """
        if boolean:
            self.__restart_button.place(x=400, y=846, anchor=CENTER)
        else:
            self.__restart_button.place_forget()

    def game_starter(self):
        """ Tämä metodi huolehtii pelin alkamisesta

        :return:
        """

        # korttien kuva lista täytyy tyhjentää aina ennen uutta peliä ja
        # tämä metodi sattui olemaan järkevin, johon sen laittaa
        self.__list_of_card_labels = [[], [], [], [], [], []]
        self.config_small_info("Revealing the cards!")
        self.game_initializer(self.__list_of_players)  # luodaan pelaaja oliot
        for player in self.__list_of_players:
            self.update_player_widgets(player)
        # pelaaja 1 aloittaa aina
        player1 = self.__list_of_players[1]
        player1.change_turn()
        self.enable_buttons(player1)

    def game_initializer(self, list_of_players):
        """ Luo pelaaja oliot ja antaa heille ensimmäiset kortit.

        :param list_of_players: list, lista pelaajista, jonne oliot heitetään
        :return:
        """
        list_of_players.clear()  # poistetaan aiemmat pelaajat, jos niitä on
        dealer = Player("Dealer")
        dealer.deal_card()
        dealer.deal_card(True)  # toinen kortti jakajalla on alaspäin
        list_of_players.append(dealer)
        for number in range(1, self.__players + 1):
            player = Player("Player" + str(number))
            list_of_players.append(player)
            player.deal_card()
            player.deal_card()
            check_bust(player)

    def restart(self):
        """ Tätä kutsutaan, kun painetaan restart. Jakaa uudet kortit
        pelaajille ja aloittaa pelin alusta

        :return:
        """
        for player in self.__list_of_players:
            self.disable_buttons(player)
        # kaikki vanhat kortit pois näkyvistä
        for sub_list in self.__list_of_card_labels:
            for card in sub_list:
                card.place_forget()
        self.game_initializer(self.__list_of_players)
        self.game_starter()

    def player_hit(self):
        """ Tätä kutsutaan, kun pelaaja painaa hit nappia

        :return:
        """

        # etsitään se pelaaja olio, jolla on vuoro
        player_in_turn = self.get_turn()
        player_in_turn.deal_card()
        name_as_string = player_in_turn.get_name()
        self.config_small_info(f"{name_as_string} decides to hit!")
        if check_bust(player_in_turn):
            self.config_small_info(f"{name_as_string} busts!")
            # jos pelaaja bustaa, vaihdetaan vuoroa seuraavaan
            self.change_turn(player_in_turn)
        self.update_player_widgets(player_in_turn)

    def get_turn(self):
        """ Palauttaa sen pelaaja olion, jolla on vuoro

        :return: Player, olio, jolla on vuoro
        """
        for player in self.__list_of_players:
            if player.get_players_turn():
                return player

    def player_stand(self):
        """ Kutsutaan, kun painetaan stand. Eli siis perjaatteeesa vain vaihtaa
         vuoron seuraavalle pelaajalle

        :return:
        """
        player_in_turn = self.get_turn()
        name_as_string = player_in_turn.get_name()
        self.config_small_info(f"{name_as_string} decides to stand!")
        self.change_turn(player_in_turn)

    def change_turn(self, old_player):
        """ Vaihtaa pelaajan vuoron seuraavalle

        :param old_player: Player, pelaaja, jonka vuoro pitää vaihtaa
        :return:
        """
        # saadaan tieto, kuinka mones pelaaja on
        old_player_index = self.get_player_index(old_player)
        # jos pelaaja ei ole viimeinen, vaihdetaan vuoro seuraavalle
        if old_player_index != self.__players:
            new_player_index = old_player_index + 1
            new_player = self.__list_of_players[new_player_index]
            old_player.change_turn()
            new_player.change_turn()
            self.disable_buttons(old_player)
            self.enable_buttons(new_player)
        else:
            # jos on viimeinen, on jakajan vuoro
            self.disable_buttons(self.__list_of_players[self.__players])
            # otetaan nappien toimivuus pois koska muuten menee
            # plörinäks jos niitä painelee jakajan vuoron aikana
            self.__restart_button.configure(state=DISABLED)
            self.__right_arrow_button.configure(state=DISABLED)
            self.__left_arrow_button.configure(state=DISABLED)
            # tauoitetaan jakajan vuoro, eli ei aloiteta sitä heti
            self.__ui.after(1000, self.dealers_turn)

    def enable_buttons(self, player):
        """ Asettaa pelaajan napit sillai et niit voi painella. Lisäksi
        päivittää informaatio labelin, joka kertoo kans kenen vuoro on

        :param player: Player, pelaaja, jonka nappeja halutaan painella
        :return:
        """
        name_as_string = player.get_name()
        # jos pelaajan napit aktivoidaan, on aina pelaajan vuoro
        self.__information_label.configure(text=f"{name_as_string}'s "
                                                f"turn, hit or stand.")

        player_number = self.__list_of_players.index(player)
        buttons = self.__list_of_buttons[player_number]
        for button in buttons:
            button.configure(state=NORMAL)

    def disable_buttons(self, player):
        """ Asettaa pelaajan napit sillai et niit ei voi painella.

        :param player: Player, pelaaja, jonka nappeja ei haluta enää painella
        :return:
        """
        player_number = self.__list_of_players.index(player)
        buttons = self.__list_of_buttons[player_number]
        for button in buttons:
            button.place(x=-100, y=-100)  # napit pois näkyvistä
            button.configure(state=DISABLED)

    def config_small_info(self, text):
        """ Metodi, jolla voidaan helposti muuttaa pienempää infoa

        :param text: str, teksti, joka halutaan näkyvän
        :return:
        """
        self.__small_info_label.configure(text=text)

    def dealers_turn(self):
        """ Hoitaa jakajan vuoron automaattiseti

        :return:
        """
        self.__information_label.configure(text=f"Dealer's turn.")
        self.config_small_info("Revealing Dealer's 2nd card!")
        # Odotetaan hetki aina jakajan toimitojen välissä. Täytyy toteuttaa
        # tälleen osissa, muuten ei work
        self.__ui.after(1500, self.reveal_dealers_2nd)

    def reveal_dealers_2nd(self):
        """ Paljastetaan jakajan toinen kortti

        :return:
        """
        dealer = self.__list_of_players[0]
        # määritellään jakajan toinen kortti, joka on alaspäin
        dealer.get_cards().pop()
        dealer.deal_card()
        check_bust(dealer)  # jos sattuu saamaan kaksi ässää, softhand poistuu
        self.update_player_widgets(dealer)
        self.__ui.after(1500, self.dealer_1st_choice)

    def dealer_1st_choice(self):
        """ Dealer päättää hittaako vai standaako

        :return:
        """
        dealer = self.__list_of_players[0]
        # jos jakajan yhteislukema on yli 17, hän standaa ja peli on ohi
        if dealer.get_total_card_value() >= 17:
            self.__information_label.configure(text=f"Game Over!")
            self.__ui.after(1500, self.decide_winners)
            self.config_small_info("Dealer's total value exceeds 16. "
                                   "He decides to stand.")
        else:
            self.dealer_decides_about_hitting()

    def dealer_decides_about_hitting(self):
        """ Jakaja päättää mikäli jatkaa lyömistä. Toteutettu rekursiiviseti
        tkinterin after metodin takia

        :return:
        """
        dealer = self.__list_of_players[0]
        if dealer.get_total_card_value() < 17:
            self.config_small_info(
                "Dealer's total value is under 17. He decides to hit.")
            # sekuntin jälkeen lyö
            self.__ui.after(1000, self.dealer_hit)
            # toisen sekuntin jälkeen kutsutaan uudestaan ja tarkastetaan, onko
            # yhteislukema vieläkin alle 17
            self.__ui.after(2000, self.dealer_decides_about_hitting)
        else:
            # jos ei lyyä enää nii peli päättyy
            self.__information_label.configure(text=f"Game Over!")
            self.__ui.after(750, self.decide_winners)
            if check_bust(dealer):
                self.config_small_info(
                    "The dealer busts!")
            else:
                self.config_small_info(
                    "Dealer's total value exceeds 16. He decides to stand.")

    def dealer_hit(self):
        """ Jakaa jakajalle uuden kortin ja päivittää näkymän

        :return:
        """
        dealer = self.__list_of_players[0]
        dealer.deal_card()
        check_bust(dealer)  # softness päivitetään jos menee yli
        self.update_player_widgets(dealer)

    def decide_winners(self):
        """ Päätetään voittajat yksi kerrallaan

        :return:
        """
        dealer = self.__list_of_players[0]
        for player in self.__list_of_players[1:]:
            if win(player, dealer):
                self.update_player_win_label(player,
                                             f"{player.get_name()} wins!")
            elif tie(player, dealer):
                self.update_player_win_label(player,
                                             f"{player.get_name()} "
                                             f"and the dealer tie!")
            else:
                self.update_player_win_label(player,
                                             f"{player.get_name()} loses!")
        # voidaan aloittaa uusi peli
        self.__new_game_button.configure(state=NORMAL)
        self.restart_button_manager(False)
        self.__right_arrow_button.configure(state=NORMAL)
        self.__left_arrow_button.configure(state=NORMAL)

    def update_player_win_label(self, player, label_text):
        """ Metodi, joka asettaa voitto labelit oikeille paikoille

        :param player: Player, pelaaja olio, jolle voitto label asetetaan
        :param label_text: str, teksti, joka näytetään labelissa
        :return:
        """
        name_x = PLAYER_POSITIONS[player.get_name()][self.__players - 1]["name_x"]
        name_y = PLAYER_POSITIONS[player.get_name()][self.__players - 1]["name_y"]
        win_label_x = name_x + 47
        win_label_y = name_y - 5
        self.__win_label = Label(text=label_text, bg=bg, fg=fg)
        self.__win_label.place(x=win_label_x, y=win_label_y, anchor=CENTER)

    def quit_game(self):
        """ Sulkee peli-ikkunan

        :return:
        """
        self.__ui.destroy()

    def get_player_index(self, player):
        """Ottaa sisäänsä pelaaja olion ja kertoo kuinka mones pelaaja tämä on.
        Dealer 0. pelaaja, player1 1. jne...

        :param player: Player, pelaaja, jonka numero halutaan
        :return: int, pelaajan numero
        """
        return self.__list_of_players.index(player)

    def right_arrow(self):
        """ Tätä kutsutaan kun painetaan nappia >. Lisää pelaajien määrää
        yhdellä

        :return:
        """
        self.__players += 1
        self.new_game()

    def left_arrow(self):
        """ Tätä kutsutaan kun painetaan nappia <. Vähentää pelaajien määrää
        yhdellä

        :return:
        """
        self.__players -= 1
        self.new_game()


class Player:

    def __init__(self, name):
        # määritellään pelaaja olio

        self.__name = name
        self.__cards = []
        self.__cards_total_value = 0
        self.__bust = False
        self.__has_softhand = False
        self.__has_had_softhand = False  # jos ollut jo softhand
        self.__has_turn = False

    def change_turn(self):
        """ Muutetaan pelaajan vuoro falsesta trueksi tai toisinpäin

        :return:
        """
        self.__has_turn = not self.__has_turn

    def get_players_turn(self):
        """ Palauttaa totuusarvon pelaajan vuorosta

        :return: bool, True, False, riippuen onko pelaajalle annettu vuoro
        """
        return self.__has_turn

    def get_cards(self):
        """ Palauttaa listan, jossa alkiot ovat korttien numeroita (0-52)

        :return: list, lista korteista
        """
        return self.__cards

    def get_name(self):
        """ palauttaa pelaajan nimen

        :return: str, nimi
        """
        return self.__name

    def get_total_card_value(self):
        """ Palauttaa kaikkien pelaajan korttien yhteislukeman

        :return: int, yhteislukema
        """
        return self.__cards_total_value

    def get_softness(self):
        """ palauttaa tiedon siitä, onko pelaajalla vielä soft-hand

        :return: bool
        """
        return self.__has_softhand

    def get_bust_state(self):
        """ Palauttaa true tai false riippuen onko pelaaja bustannut (🥵)

        :return: bool, True tai false riippuen onko bustannu
        """
        return self.__bust

    def set_bust_state(self):
        """ Asettaa pelaajan bust-tilan

        :return:
        """
        self.__bust = True

    def set_softness(self, boolean):
        """ Asettaa pelaajalle soft-handin tai ottaa sen pois

        :param boolean: bool, True tai False
        :return:
        """
        self.__has_softhand = boolean

    def deal_card(self, upsidedown=False):
        """ Antaa pelaajalle yhden kortin ja antaa soft-handin tarvittaessa
        ja päivittää korttien yhteislukeman

        :param upsidedown: bool, kertoo jaetaanko kortti alaspäin vai ylöspäin
        :return:
        """
        card = random_card()
        if upsidedown:
            card = 0
        # jos ässä, nuo lukemat ovat ässiä
        elif card in [1, 14, 27, 40] and not self.__has_had_softhand:
            self.set_softness(True)
            self.__has_had_softhand = True
        self.__cards.append(card)
        card_value = CARD_LIST[card][1]
        self.update_total_card_value(card_value)

    def update_total_card_value(self, card_value):
        """ Päivittää korttien yhteislukeman

        :param card_value: int, se lukema, joka lisätään yhteislukemaan
        :return:
        """
        self.__cards_total_value += card_value

def win(player, dealer):
    """ Päättää onko pelaaja voittanut jakajaa vastaan

    :param player: Player, pelaaja olio
    :param dealer: Player, pelaaja olio, joka on jakaja
    :return:
    """
    if not player.get_bust_state() and not dealer.get_bust_state():
        if player.get_total_card_value() > dealer.get_total_card_value():
            return True
    elif not player.get_bust_state() and dealer.get_bust_state():
        return True


def tie(player, dealer):
    """ Päättää onko pelaaja ja jakaja saanut tasapelin.

    :param player: Player, pelaaja olio
    :param dealer: Player, pelaaja olio, joka on jakaja
    :return:
    """
    if not player.get_bust_state() and not dealer.get_bust_state():
        if player.get_total_card_value() == dealer.get_total_card_value():
            return True

# Ei häviö metodia, sillä jos ei tasapeliä tai voittoa niin pelaaja
# on hävinnyt)


def random_card():
    """ Arpoo satunnaisen kortin väliltä 1-52

    :return: int, palauttaa kortin lukeman väliltä 1-52
    """
    card = choice(range(1, 53))
    # card = choice([1, 14, 27, 40, 13, 26, 2, 39, 9])
    return card


def check_bust(player):
    """ Tarkistaa onko pelaaja mennyt yli 21. Jos pelaajalla on soft hand,
    kokonaislukemasta vähennetään kymmenen, mikä kuvaa sitä, että ässä muuttuu
    ykköseksi.

    :param player: Player, pelaaja, joka tarkastetaan
    :return:
    """
    total_value = player.get_total_card_value()
    if total_value > 21:
        if player.get_softness():
            player.update_total_card_value(-10)
            player.set_softness(False)
            # jos arvo on silti yli 21, bustataan
            # (harvinaista, mutta voi tapahtua)
            if player.get_total_card_value() > 21:
                player.set_bust_state()
                return True
            else:
                return False
        else:
            player.set_bust_state()
            return True
    return False


def main():
    list_of_players = []
    UserInterface(list_of_players)


if __name__ == "__main__":
    main()
