# Data pro cvičení 09 / Data for lab 09

## Česky

Soubor `parts.csv` obsahuje **syntetická data** vytvořená deterministicky skriptem `../prepare_data.py` (semínko 20261118). Nejde o záznamy skutečné výroby. Jednotky a vztahy jsou ilustrační; generátor není fyzikálním modelem vstřikolisu.

2000 samostatných výlisků z jedné simulované linky. Řádky nejsou časovou řadou; pro úlohu se považují za nezávislé vzorky. Soubor nemá chybějící hodnoty ani záměrné vady zápisu – cvičení se soustředí na model, metriky a ladění.

| Sloupec | Význam | Jednotka / hodnoty |
|---|---|---|
| part_id | Identifikátor výlisku, nikoli příznak | P0001 až P2000 |
| melt_temp | Teplota taveniny | °C (kolem 230) |
| pressure | Vstřikovací tlak | bar (kolem 900) |
| cooling_time | Doba chlazení | s (kolem 12) |
| mould_temp | Teplota formy | °C (kolem 60) |
| humidity | Vlhkost ve skladu granulátu | % (kolem 45) |
| vibration | Vibrace lisu | mm/s (kolem 0,5, šikmé rozdělení) |
| shot_weight | Hmotnost dávky | g (kolem 52) |
| cycle_time | Doba cyklu | s (kolem 30) |
| shrinkage | Naměřené smrštění, ve cvičení se nepoužívá | % (kolem 1,5) |
| defect | Výsledek kontroly, cíl klasifikace | 0 v pořádku, 1 vadný |

Vlastnosti důležité pro cvičení:

- Vadných výlisků je 10,7 %. Model, který vše označí za v pořádku, má přesnost asi 0,89.
- Příznaky mají velmi rozdílné škály (tlak ve stovkách, vibrace v desetinách).
- Třídy se překrývají; žádná přímka je neoddělí.
- Riziko vady závisí i na **součinu** odchylek teploty a tlaku. Lineární model na původních příznacích tuto složku nezachytí.
- `shot_weight` a `cycle_time` s vadou nesouvisí.
- `shrinkage` se ve cvičení nepoužívá a není vstupem klasifikace.

## English

The file `parts.csv` contains **synthetic data** generated deterministically by `../prepare_data.py` (seed 20261118). These are not records of real production. Units and relationships are illustrative; the generator is not a physical model of an injection-moulding machine.

2000 separate moulded parts from one simulated line. Rows are not a time series; the task treats them as independent samples. The file has no missing values and no intentional recording defects – the lab focuses on the model, metrics and tuning.

| Column | Meaning | Unit / values |
|---|---|---|
| part_id | Part identifier, not a feature | P0001 to P2000 |
| melt_temp | Melt temperature | °C (around 230) |
| pressure | Injection pressure | bar (around 900) |
| cooling_time | Cooling time | s (around 12) |
| mould_temp | Mould temperature | °C (around 60) |
| humidity | Humidity in the granulate store | % (around 45) |
| vibration | Press vibration | mm/s (around 0.5, skewed) |
| shot_weight | Shot weight | g (around 52) |
| cycle_time | Cycle time | s (around 30) |
| shrinkage | Measured shrinkage, not used in the lab | % (around 1.5) |
| defect | Inspection result, classification target | 0 good, 1 defective |

Properties that matter for the lab:

- 10.7 % of parts are defective. A model that labels every part as good has an accuracy of about 0.89.
- Features have very different scales (pressure in hundreds, vibration in tenths).
- The classes overlap; no straight line separates them.
- The defect risk also depends on the **product** of the temperature and pressure deviations. A linear model on the original features cannot capture this component.
- `shot_weight` and `cycle_time` are unrelated to the defect.
- `shrinkage` is not used in the lab and is not a classification input.
