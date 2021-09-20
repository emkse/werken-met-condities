# Vacature: Circusdirecteur voor Circus HotelDeBotel
import time
import webbrowser

# Begin scherm.
print("+++++++++++++++++++++++++++++++")
print("+ Vacature - Ruimtevuilnisman +")
print("+++++++++++++++++++++++++++++++")
time.sleep(0.5)
print("Er is een vacature ruimtevuilnisman. Die moet al het ruimtepuin dat rondom de aarde zweeft op gaan ruimen.")
print("Om in aanmerking te komen voor een sollicitatiegesprek moet je als kandidaat moet je aan alle eisen voldoen")
print("Succes met het invullen!")
print("---------------------------------")
time.sleep(1)

# Hier niet aanzitten. Hier staan alle vragen.
# If-statements die zorgen ervoor dat zij de vragen kunnen beantwoorden. 
#
Vraag1 = input("U heeft meer dan 4 jaar praktijkervaring met dieren-dressuur OF meer dan 5 jaar ervaring met jongleren OF meer dan 3 jaar praktijkervaring met acrobatiek? ")
Vraag2 = input("U bent in bezit van een Diploma MBO-4 ondernemen? ")
if Vraag2 == "Ja":
    vraag3 = input("Welke MBO heeft u gezeten? ")
    vraag3 = int(input("Hoelang heeft u op deze MBO opleiding gezeten? vul hier (1/2/3/4) in: "))
    if vraag3 >= 3:
        Vraag4 = input("Bent u in bezit van een geldig rijbewijs type C? ")
        if Vraag4 == "Ja":
            Vraag4 = int(input("Hoeveel jaar heeft u deze al? Vul hier een getal in: "))
            if Vraag4 >= 2:
                vraag5 = input("U bent bezit van een hoge hoed? ")
                if vraag5 == "Ja":
                    vraag5 = input("Welke kleur hoed heeft u? ")
                    if vraag5 == "Zwart":
                        vraag6 = input("U bezit aan de goede kleur hoed. Bent u een man of een vrouw? ")
                        if vraag6 == "Man":
                            vraag6 = int(input("Hoelang is uw snor minimaal 10cm"))
                            if vraag6 >= 10:
                                vraag7 = int(input("U heeft de goede formaat snor. Hoelang bent u? "))
                                if vraag7 >= 150:
                                    vraag8 = int(input("U bent lang genoeg. Hoe zwaar bent u? "))
                                    if vraag8 >= 90:
                                        vraag8 = input("U bent zwaar genoeg. Heeft u het Certificaat “Overleven met gevaarlijk personeel?” ")
                                        if vraag8 == "Ja":
                                            print("U bent geslaagd met uw sollicitatie. Stuur uw CV door naar CodeAura. Graag nodig ik uw uit voor een persoonlijk gesprek.")
                                        else:
                                            print("U moet dit Certificaat hebben. Anders kan u uw baan niet krijgen")
                                    else:
                                        print("U moet zwaarder worden. Dus meer gaan eten")
                                else:
                                    print("Koop groeimiddel en laat uwzelf groeien.")
                            else:
                                print("Je snor moet je laten groeien")
                        else:
                            vraag6 = int(input("Heeft u rood krul haar en hoe lang is uw haar? vul een getal in"))
                            if vraag6 >=20:
                                vraag7 = int(input("U heeft de goede lengte haar. Hoelang bent u? "))
                                if vraag7 >= 150:
                                    vraag9 = int(input("U bent lang genoeg. Hoe zwaar bent u? "))
                                    if vraag9 >= 90:
                                        vraag9 = input("U bent zwaar genoeg. Heeft u het Certificaat “Overleven met gevaarlijk personeel?” ")
                                        if vraag9 == "Ja":
                                            print("U bent geslaagd met uw sollicitatie. Stuur uw CV door naar CodeAura. Graag nodig ik uw uit voor een persoonlijk gesprek.")
                                        else:
                                            print("U moet dit Certificaat hebben. Anders kan u uw baan niet krijgen")
                                    else:
                                        print("U bent te licht. Ga meer eten")
                                else:
                                    print("Koop groeimiddel en laat uwzelf groeien")    
                else:
                    print("Koop eerst een hoed.")
            else:
                print("U rijd te kort de vrachtwagen probeer meer dan 2 jaar ervaring te hebben als chauffeur.")
        else:
            print("Haal eerst je vrachtwagen rijbewijs voordat je voor deze baan gaat solliciteren.")
    else:
        print("Dat is te kort voor een MBO opleiding. Ga terug.")

else:
    print("U voldoed niet aan de eisen.")
                                        





