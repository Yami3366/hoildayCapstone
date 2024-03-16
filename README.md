# Order Northern Line Night Tour  
###### Two version: hoilday.py ,hoilday_OOP.py
### Flow Diagram


```mermaid
graph LR
A[Welcome Page] -->B(Select Tours 1,2,3,4)
    B --> C{Traveler to decide}
    C -->|One| D[City Flying]
    C -->|Two| E[Staying Hotel]
    C -->|Three| F[hiring a 4x4 car]
    D -->G[Holiday Fee Deatils]
    E -->G[Holiday Fee Deatils]
    F -->G[Holiday Fee Deatils]
 

```
### Class HolidayCostCalculator Diagrams,hoilday_OOP.py
```mermaid
classDiagram
      HolidayCostCalculator <|-- Color
      HolidayCostCalculator : +Dict city_cost
      HolidayCostCalculator : +Dict hotel_cost
      HolidayCostCalculator : +Dict rental_cost
      HolidayCostCalculator: +iwelcomepage()
      HolidayCostCalculator: +validate_city_flight()
      HolidayCostCalculator: +validate_rental_days()
      HolidayCostCalculator: +calcutlate_cost()
      HolidayCostCalculator: +print_holiday_details()
      class Color{
          +dict COLORS
          +decorate()
      }

```
### Display the demo program operation screen.
<img width="500" alt="h1" src="https://github.com/Yami3366/hoildayCapstone/assets/159643271/aff17d18-1fe7-4633-b021-7a4e05f3572c">
