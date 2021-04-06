"""
Shopping cart
Nasim cilem bude vytvorit kosik, kam bude uzivatel vkladat zbozi z virtualni nabidky.
Uzivatel muze pridavat tak dlouho, jak bude potrebovat.
Pokud bude mit vse, co potrebuje, muze cely nakup zaplatit.

Krok za krokem vyreste tyto bodu, ktere by nas program mel splnovat.

1. pozdravit uivatele
2. vypsat nabidku zbozi (bez poctu kusu)
3. Vlozit zbozi do kosiku, dokud nebudete chtit nakup ukoncit
    * Pouze vkladat zbozi, dokud neukoncime nakup
    * Vice kusu stejneho zbozi
    *Zbozi neni skaldem
    *Neplatny vstup uzivatele
4. Pri ukonceni vypsat obsah nakupniho kosiku
5. Potvrdit nakup a ukoncit program
"""


# vstupni udaje
kosik = {}
ODDELOVAC = "=" * 44
POTRAVINY = {
    "mleko" : [30,5], # index 0 -> cena, index 1 -> pocet
    "maso" : [100,1],
    "banan" : [30,10],
    "jogurt" : [10,5],
    "chleb" : [20,5],
    "jablko" : [10,10],
    "pomeranc" : [15,10]
    }

# pozdraveni uzivatele
print(ODDELOVAC,
      'Vitejte na e-shop obchodu Rohlik.cz'.center(len(ODDELOVAC)),
      ODDELOVAC, sep="\n"
      )

# nabidka zbozi
for zbozi, cena_pocet in POTRAVINY.items():
    print(f'|Zbozi: {zbozi: ^8} |Cena: {cena_pocet[0]: ^3}kc |Pocet: {cena_pocet[1]: ^2}ks |')
else:
    print(ODDELOVAC)

# vkladani zbozi do kosiku


while (vyber := input("Zadej zbozi nebo slovo 'stop': ")) != "stop":
    if vyber not in POTRAVINY.keys():
        print(f'Zbozi {vyber} neni v nabidce')

    elif POTRAVINY[vyber][1] == 0:
        print(f'Zbozi {vyber} neni skladem')


    elif vyber not in kosik:
        kosik[vyber] = [POTRAVINY[vyber][0], 1]
        print(f'|kosik = {kosik}')
        POTRAVINY[vyber][1] -= 1

    elif vyber in kosik:
        kosik[vyber][1] = kosik[vyber][1] + 1
        print(f'|kosik = {kosik}')
        POTRAVINY[vyber][1] -= 1
else:
    print(ODDELOVAC)
    celkem = 0

    for zbozi, cisla in kosik.items():
        cena = cisla[0]
        pocet = cisla[1]
        celkem = celkem + (mezisoucet := cena * pocet)
        print(
            f"{zbozi:<8}:{cena:>4} x {pocet:<2} = {mezisoucet:>3},-"
            .center(len(ODDELOVAC))
        )

    else:
        print(ODDELOVAC)

        if (platba := input("Pokracovat v platbe (y/n): ")) == "y":
            print(ODDELOVAC,
                  f'prechazim k platbe...'.center(len(ODDELOVAC)),
                  sep="\n"
                  )
        elif platba == "n":
            print(ODDELOVAC,
                  f'platba prerusena...'.center(len(ODDELOVAC)),
                  sep="\n"
            )
        else:
            print(
                ODDELOVAC,
                f'invalid operation...platba prerusena'.center(len(ODDELOVAC)),
                  sep="\n"
                  )




