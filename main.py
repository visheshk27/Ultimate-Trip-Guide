from hotel import *
from smtp import *
from corona import *
from places import *
from newsfetch.news import newspaper
import pyfiglet
import pyjokes
import random
import py8fact



print('''
██████╗░░█████╗░███╗░░██╗  ██╗░░░██╗░█████╗░██╗░░░██╗░█████╗░░██████╗░███████╗
██╔══██╗██╔══██╗████╗░██║  ██║░░░██║██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝░██╔════╝
██████╦╝██║░░██║██╔██╗██║  ╚██╗░██╔╝██║░░██║░╚████╔╝░███████║██║░░██╗░█████╗░░
██╔══██╗██║░░██║██║╚████║  ░╚████╔╝░██║░░██║░░╚██╔╝░░██╔══██║██║░░╚██╗██╔══╝░░
██████╦╝╚█████╔╝██║░╚███║  ░░╚██╔╝░░╚█████╔╝░░░██║░░░██║░░██║╚██████╔╝███████╗
╚═════╝░░╚════╝░╚═╝░░╚══╝  ░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝''')
Text = pyfiglet.figlet_format("Have a Safe Journey", font = "digital" )
print(Text)
print("Made By:- @Techsoftmedia @Prasan @Visheshk27\n")
print("Here is something to help you when you travel anywhere \n 1. Find hotels near you \n 2. Find Information about your travel country  \n 3. Email your loved ones good wishes \n 4. Check the number of covid cases before travelling \n 5. Safety Guide in case of emergency \n 6. Travel Comic books \n 7. Random jokes \n 8. Random facts \n 9. News \n 10.SOS USE WHEN YOU NEED URGENT HELP \n 11.Covid protection Guide \n 12. Type exit to close")
print("\n")
num = ""
while num != "exit":
  num = input ("Enter your choice between 1 to 12 :")
  if num == "11":
    print("""\nIf you are not fully vaccinated against COVID-19:

⦾ Wear a face mask, as advised by the CDC.
⦾ Maintain at least six feet of distance between yourself and others.
⦾ Avoid large gatherings.
⦾ Socialize outdoors.
⦾ Get vaccinated as soon as you are eligible.

Everyone:

⦾ Avoid close contact with people who are sick.
⦾ Minimize touching your eyes, nose, and mouth.
⦾ Stay home when you are sick.
⦾ Cover your cough or sneeze with a tissue, then throw the tissue in the trash.
⦾ Clean frequently touched objects and surfaces regularly.
⦾ Wash your hands often with soap and water.""")
  if num == "10":
      print(" 1.India \n 2.USA \n 3.Brazil \n 4.Chile \n 5.Australia \n 6.Ukraine \n 7.Morocco")
      sos = input ("Enter your choice :")
      if sos == "1":
        print("Police:100/AMBULANCE:101/FIRE:102")
      if sos == "2":
       print("Police:911")
      if sos == "3":
       print("Police:190/AMBULANCE:192/FIRE:193")
      if sos == "4":
       print("Police:133/AMBULANCE:131/FIRE:132")
      if sos == "5":
       print("Police:000/AMBULANCE:112")
      if sos == "6":
       print("Police:112/AMBULANCE:103/FIRE:101")
      if sos == "7":
       print("Police:19/AMBULANCE:15/FIRE:177")

  if num == "2":
      hotel()

  if num == "1":
      places()

  if num == "3":
      smail()

  if num == "7":
      print(pyjokes.get_joke())

  if num == "9":
        
      a = random.randint(0,20)
      news = newspaper('https://www.bbc.co.uk/search?q=latest+news&page='+str(a))
      print(news.article)
  
  if num == "8":
    fact = py8fact.random_fact()
    print(fact)

  if num == "4":
        corona()

  if num == "6":
    print('''A gentleman was walking through an elephant camp, and he spotted that the elephants weren’t being kept in cages or held by the use of chains.

All that was holding them back from escaping the camp, was a small piece of rope tied to one of their legs.

As the man gazed upon the elephants, he was completely confused as to why the elephants didn’t just use their strength to break the rope and escape the camp. They could easily have done so, but instead, they didn’t try to at all.

Curious and wanting to know the answer, he asked a trainer nearby why the elephants were just standing there and never tried to escape.

The trainer replied;
“when they are very young and much smaller we use the same size rope to tie them and, at that age, it’s enough to hold them. As they grow up, they are conditioned to believe they cannot break away. They believe the rope can still hold them, so they never try to break free.”


The only reason that the elephants weren’t breaking free and escaping from the camp was that over time they adopted the belief that it just wasn’t possible.

Moral of the story:
No matter how much the world tries to hold you back, always continue with the belief that what you want to achieve is possible. Believing you can become successful is the most important step in actually achieving it.''')

  if num == "5":

    print(" 1.During an avalanche \n 2.During an earthquake \n 3.During a flood \n 4.During a hurricane \n 5.During a landslide \n 6.During a severe storm \n 7.During a tornadoes \n 8.During a wildfire")
    guide = input("Enter your choice :")
    if guide == "1":
        print("""If you become caught in an avalanche, try to:

Push machinery, equipment or heavy objects away from you to avoid injury.
Grab onto anything solid (trees, rocks, etc.) to avoid being swept away.
Keep your mouth closed and your teeth clenched.
If you start moving downward with the avalanche, stay on the surface using a swimming motion.
Try to move yourself to the side of the avalanche.

When the avalanche slows, attempt to:
Push yourself towards the surface.
Make an air pocket in front of your face using one arm.
Push the other arm towards the surface.

When the avalanche stops, begin to:
Dig yourself out, if possible.
Relax your breathing, particularly if you cannot dig yourself out.
Stay calm and shout only when a searcher is near.""")
    if guide == "2":
       print("""Wherever you are when an earthquake starts, take cover immediately. Move a few steps to a nearby safe place 
       if need be. Stay there until the shaking stops.
If you are indoors: "DROP, COVER, HOLD ON"
Stay inside.
Drop under heavy furniture such as a table, desk, bed or any solid furniture.
Cover your head and torso to prevent being hit by falling objects.
Hold onto the object that you are under so that you remain covered.
If you can't get under something strong, or if you are in a hallway, flatten yourself or crouch against an interior wall.
If you are in a shopping mall, go into the nearest store.
Stay away from windows, and shelves with heavy objects.
If you are at school, get under a desk or table and hold on. Face away from windows.
If you are in a wheelchair, lock the wheels and protect the back of your head and neck.
If you are outdoors
Stay outside.
Go to an open area away from buildings.
If you are in a crowded public place, take cover where you won't be trampled.
If you are in a vehicle
Pull over to a safe place where you are not blocking the road. Keep roads clear for rescue and emergency vehicles.
Avoid bridges, overpasses, underpasses, buildings or anything that could collapse.
Stop the car and stay inside.
Listen to your car radio for instructions from emergency officials.
Do not attempt to get out of your car if downed power lines are across it. Wait to be rescued.
Place a HELP sign in your window if you need assistance.
If you are on a bus, stay in your seat until the bus stops. Take cover in a protected place. If you can't take cover, sit in a crouched position and protect your head from falling debris.
AVOID the following in an earthquake
Doorways. Doors may slam shut and cause injuries.
Windows, bookcases, tall furniture and light fixtures. You could be hurt by shattered glass or heavy objects.
Elevators. If you are in an elevator during an earthquake, hit the button for every floor and get out as soon as you can.
Downed power lines - stay at least 10 metres away to avoid injury.
Coastline. Earthquakes can trigger large ocean waves called tsunamis.""")
    if guide == "3":
       print("""Keep your radio on to find out what areas are affected, what roads are safe, where to go and what to do if the local emergency team asks you to leave your home.
Keep your emergency kit close at hand, in a portable container such as a duffel bag, back pack, or suitcase with wheels.
If you need to evacuate
Vacate your home when you are advised to do so by local emergency authorities. Ignoring such a warning could jeopardize the safety of your family or those who might eventually have to come to your rescue.
Take your emergency kit with you.
Follow the routes specified by officials. Don't take shortcuts. They could lead you to a blocked or dangerous area.
Make arrangements for pets.
Time permitting, leave a note informing others when you left and where you went. If you have a mailbox, leave the note there.
Never cross a flooded area
If you are on foot, fast water could sweep you away.
If you are in a car, do not drive through flood waters or underpasses. The water may be deeper than it looks and your car could get stuck or swept away by fast water.
Avoid crossing bridges if the water is high and flowing quickly.
If you are caught in fast-rising waters and your car stalls, leave it and save yourself and your passengers""")
    if guide == "4":
       print("""Always check the marine forecast from the Weatheroffice website before going boating and listen to weather reports during your cruise. Never go out in a boat during a storm. If you are on the water and you see bad weather approaching, head for shore immediately.
Do not go down to the water to watch the storm. Most people who are killed during hurricanes are caught in large waves, storm surges or flood waters.
If the eye of the hurricane passes over, there will be a lull in the wind lasting from two or three minutes to half an hour. Stay in a safe place. Make emergency repairs only and remember that once the eye has passed over, the winds will return from the opposite direction with possibly even greater force.
Listen for reports from authorities on your portable radio.
If lightning is present, remember that you can use a cellular telephone during a severe storm, but it's not safe to use a land-line telephone.
On a farm, depending on your location and available shelter, it may be better to leave livestock unsheltered. During Hurricane Andrew, some horses left outside suffered less injury then those placed in shelters. This was because some shelters did not withstand the high winds. Horses were injured by collapsing structures and flying objects that may have been avoided on the outside. For more information, view our publication Emergency Preparedness for Farm Animals.


Mobile homes

If you live in a mobile home:

Position your mobile home near a natural windbreak such as a hill or clump of trees.
Anchor the structure securely. Consult the manufacturer for information on secure tie-down systems.
When a severe storm approaches, seek shelter in a more secure building as staying in a mobile home during a hurricane can be more dangerous than going outside""")
    if guide == "5":
       print("""If indoors

>Find cover in the section of the building that is furthest away from the approaching landslide.
>Take shelter under a strong table or bench.
Hold on firmly and stay put until all movement has ceased.
If outdoors

>Move quickly away from its likely path, keeping clear of embankments, trees, power lines and poles.
>Stay away from the landslide. The slope may experience additional failures for hours to days afterwards.""")
    if guide == "6":
       print("""What to do during a severe storms


If you are indoors, stay away from windows, doors and fireplaces.
You may want to go to the sheltered area that you and your family chose for your emergency plan.

If you are advised by officials to evacuate, do so. Take your emergency kit with you.

You can use a cellular telephone during a severe storm, but it's not safe to use a land-line telephone.

Never go out in a boat during a storm. If you are on the water and you see bad weather approaching, head for shore immediately. Always check the marine forecast before leaving for a day of boating and listen to weather reports during your cruise.

If you are in a car, stop the car away from trees or power lines that might fall on you). Stay there.


What to do during

Blizzards

When a winter storm hits, stay indoors. If you must go outside, dress for the weather. Outer clothing should be tightly woven and water-repellent. The jacket should have a hood. Wear mittens - they are warmer than gloves - and a hat, as large portion of body heat is lost through the head.
In wide-open areas, visibility can be virtually zero during heavy blowing snow or a blizzard. You can easily lose your way. If a blizzard strikes, do not try to walk to another building unless there is a rope to guide you or something you can follow.
If you must travel during a winter storm, do so during the day and let someone know your route and arrival time.
If your car gets stuck in a blizzard or snowstorm, remain calm and stay in your car. Allow fresh air in your car by opening the window slightly on the sheltered side - away from the wind. You can run the car engine about 10 minutes every half-hour if the exhaust system is working well. Beware of exhaust fumes and check the exhaust pipe periodically to make sure it is not blocked with snow. Remember: you can't smell potentially fatal carbon monoxide fumes.
To keep your hands and feet warm, exercise them periodically. In general, it is a good idea to keep moving to avoid falling asleep. If you do try to shovel the snow from around your car, avoid overexerting yourself.
Overexertion in the bitter cold can cause death as a result of sweating or a heart attack.
Keep watch for traffic or searchers.


Hail

Take cover when hail begins to fall. Do not go out to cover plants, cars or garden furniture or to rescue animals. Hail comes down at great speed, especially when accompanied by high winds. Although no one in Canada has ever been killed by hail, people have been seriously injured by it.
When a hailstorm hits, stay indoors, and keep yourself and your pets away from windows, glass doors and skylights which can shatter if hit by hailstones. Avoid using the telephone during a storm, and do not touch metal objects like stoves, radiators, metal pipes, and sinks.
When a hailstorm hits, find shelter and avoid underpasses or any low lying areas that may flood.


Ice storms

Ice from freezing rain accumulates on branches, power lines and buildings. If you must go outside when a significant amount of ice has accumulated, pay attention to branches or wires that could break due to the weight of the ice and fall on you. Ice sheets could also do the same.
Never touch power lines. A hanging power line could be charged (live) and you would run the risk of electrocution. Remember also that ice, branches or power lines can continue to break and fall for several hours after the end of the precipitation.
When freezing rain is forecast, avoid driving. Even a small amount of freezing rain can make roads extremely slippery. Wait several hours after freezing rain ends so that road maintenance crews have enough time to spread sand or salt on icy roads.
Rapid onsets of freezing rain combined with the risks of blizzards increase the chances for extreme hypothermia. If you live on a farm, move livestock promptly to shelter where feed is available. Forage is often temporarily inaccessible during and immediately after ice storms. Animal reactions to ice storms are similar to that of blizzards.


Lightning

Always take shelter during a lightning storm.
There is no safe place outside during a thunderstorm. Safe shelter can be found either in an enclosed building or a hard-topped vehicle.
If you can see lightning or hear thunder, you are in danger of being hit. Seek shelter immediately.
Wait 30 minutes after the last lightning strike in a severe storm before venturing outside again.
Do not ride bicycles, motorcycles, tractors, or golf carts. These will not protect you from a lightning strike.


Thunderstorms

During thunderstorms, you should also stay away from items that conduct electricity, such as corded telephones, appliances, sinks, bathtubs, radiators and metal pipes.""")
    if guide == "7":
       print("""If you are in a house


Go to the basement or take shelter in a small interior ground floor room such as a bathroom, closet or hallway.
If you have no basement, protect yourself by taking shelter under a heavy table or desk.
In all cases, stay away from windows, outside walls and doors.


If you live on a farm

Livestock hear and sense impending tornadoes. If your family or home is at risk, the livestock will be a non-issue. If your personal safety is not an issue, you may only have time to open routes of escape for your livestock. Open the gate, if you must, and then exit the area in a tangent direction away from the expected path of the twister.


If you are in an office or apartment building

Take shelter in an inner hallway or room, ideally in the basement or on the ground floor.
Do not use the elevator.
Stay away from windows.


If you are in a gymnasium, church or auditorium

Large buildings with wide-span roofs may collapse if a tornado hits.
If possible, find shelter in another building.
If you are in one of these buildings and cannot leave, take cover under a sturdy structure such as a table or desk.


Avoid cars and mobile homes

More than half of all deaths from tornadoes happen in mobile homes.
Find shelter elsewhere, preferably in a building with a strong foundation.


If no shelter is available, lie down in a ditch away from the car or mobile home. Beware of flooding from downpours and be prepared to move.


If you are driving
If you spot a tornado in the distance go to the nearest solid shelter.


If the tornado is close, get out of your car and take cover in a low-lying area, such as a ditch.
In all cases

Get as close to the ground as possible, protect your head and watch for flying debris.
Do not chase tornadoes - they are unpredictable and can change course abruptly.

A tornado is deceptive. It may appear to be standing still but is, in fact, moving toward you.""")
    if guide == "8":
       print("""#Monitor local radio stations.
 #Be prepared to evacuate at any time. If told to evacuate, do so.
 #Keep all doors and windows closed in your home.
 #Remove flammable drapes, curtains, awnings or other window coverings.
 #Keep lights on to aid visibility in case smoke fills the house.
 #If sufficient water is available, turn sprinklers on to wet the roof and any water-proof valuables.""")

