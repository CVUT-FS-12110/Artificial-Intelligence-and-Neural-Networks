# Data pro cvičení 10 / Data for lab 10

## Česky

Soubor `pumps.csv` obsahuje **syntetická data** vytvořená deterministicky skriptem `../prepare_data.py` (semínko 20261124). Nejde o záznamy skutečného provozu. Jednotky a vztahy jsou ilustrační; generátor není fyzikálním modelem čerpadla.

900 provozních záznamů odstředivých čerpadel stejného typu. Řádky nejsou časovou řadou; pro úlohu se považují za nezávislé vzorky. Soubor nemá chybějící hodnoty.

| Sloupec | Význam | Jednotka / hodnoty |
|---|---|---|
| record_id | Identifikátor záznamu, nikoli příznak | R001 až R900 |
| flow | Průtok (pracovní bod) | m³/h (20 až 80) |
| pressure | Výtlačný tlak | bar (asi 2 až 6) |
| bearing_temp | Teplota ložiska | °C (kolem 60) |
| current | Proud motoru | A (kolem 28) |
| vibration | Rychlost vibrací | mm/s (kolem 0,6) |
| ambient_temp | Teplota okolí | °C (kolem 22) |
| fault | Výsledek prohlídky, cíl klasifikace | 0 v pořádku, 1 porucha |

Vlastnosti důležité pro cvičení:

- Poruch je 19 %.
- Tlak klesá s průtokem po charakteristice čerpadla (přibližně parabola). Porucha je **odchylka od charakteristiky na kteroukoli stranu** (příliš vysoký i příliš nízký tlak) nebo neobvyklá teplota ložiska. Hranice mezi třídami proto není nadrovina.
- Příznaky mají rozdílné škály (průtok v desítkách, tlak v jednotkách).
- `vibration` a `ambient_temp` s poruchou nesouvisejí; `current` je odvozený od pracovního bodu.

## English

The file `pumps.csv` contains **synthetic data** generated deterministically by `../prepare_data.py` (seed 20261124). These are not records of real operation. Units and relationships are illustrative; the generator is not a physical model of a pump.

900 operating records of centrifugal pumps of the same type. Rows are not a time series; the task treats them as independent samples. The file has no missing values.

| Column | Meaning | Unit / values |
|---|---|---|
| record_id | Record identifier, not a feature | R001 to R900 |
| flow | Flow rate (operating point) | m³/h (20 to 80) |
| pressure | Discharge pressure | bar (about 2 to 6) |
| bearing_temp | Bearing temperature | °C (around 60) |
| current | Motor current | A (around 28) |
| vibration | Vibration velocity | mm/s (around 0.6) |
| ambient_temp | Ambient temperature | °C (around 22) |
| fault | Inspection result, classification target | 0 normal, 1 fault |

Properties that matter in the lab:

- 19 % of the records are faults.
- The pressure falls with the flow along the pump curve (roughly a parabola). A fault is a **deviation from the curve on either side** (too high or too low pressure) or an unusual bearing temperature. The boundary between the classes is therefore not a hyperplane.
- The features have different scales (flow in tens, pressure in units).
- `vibration` and `ambient_temp` are unrelated to the fault; `current` follows the operating point.
