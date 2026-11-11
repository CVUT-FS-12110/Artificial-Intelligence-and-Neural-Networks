# Data pro cvičení 08 / Data for lab 08

## Česky

Všech pět souborů obsahuje **syntetická data**, vytvořená deterministicky skriptem `../prepare_data.py` se základním semínkem 20261110. Nejde o záznamy skutečných zařízení ani osob. Jednotky a vztahy jsou ilustrační; generátor není fyzikálním modelem stroje. Soubory neobsahují osobní údaje ani referenční předpovědi modelu. Příprava dat probíhá před cvičením, odděleně od studentských úkolů.

### stratification-records.csv

Pevná minitabulka pro samostatnou úlohu o stratifikaci: 120 řádků, sloupce `state` a `load`. Štítky `normal`, `warning`, `fault` mají postupně 84, 24 a 12 výskytů. Jde pouze o umělé kategorie, nikoli o diagnózy skutečných zařízení. `load` obsahuje 120 různých rovnoměrně rozmístěných hodnot od 10 do 100 v ilustračních procentech. Soubor nemá chybějící hodnoty, čas ani identifikátor skupiny. Pořadí řádků nemá časový význam. Číselné hodnoty a pořadí odpovídají původní minitabulce příkladu.

### machine-records.csv

720 samostatných simulovaných provozních situací, doplněných o 6 přesných kopií záznamů. CSV tedy obsahuje 726 řádků. Situace nejsou po sobě jdoucí měření jednoho stroje ani opakovaná měření týchž zařízení. Pro základní úlohu se považují za nezávislé vzorky ze stejného generujícího procesu; šest přidaných kopií tuto podmínku narušuje a představuje záměrnou vadu dat. Závislost příznaků uvnitř řádku neznamená závislost mezi různými situacemi.

| Sloupec | Význam | Ilustrační jednotka / hodnoty |
|---|---|---|
| record_id | Identifikátor situace, nikoli příznak pro predikci | R0001 až R0720 |
| temperature | Teplota | °C |
| vibration | Velikost vibrací | mm/s |
| pressure | Tlak | kPa |
| power | Příkon | W |
| speed | Otáčky | ot/min |
| load | Relativní zatížení | % |
| mode | Provozní režim, bez přirozeného pořadí | auto, manual, eco |
| environment | Prostředí | indoor, outdoor |
| state | Cílový stav | 0 běžný simulovaný stav, 1 simulovaný stav ke kontrole |

Numerické příznaky mají různé škály a některé spolu korelují. Velké číselné hodnoty samy neznamenají větší význam pro cílový stav. Třída 1 tvoří přibližně čtvrtinu až třetinu nezávislých situací.

Záměrné mezní případy:

- Každý z osmi vstupních sloupců má mezi 720 původními situacemi 36 prázdných hodnot, tedy 5 %. Prázdné pole znamená chybějící údaj, nikoli nulu nebo kategorii s názvem „nan“. Přidané kopie mohou celkové počty prázdných polí mírně zvýšit.
- Čtyři pozorované teploty byly nahrazeny hodnotou **−999**, která je zde výslovně definovaným neplatným kódem. Žádné další obecné číselné meze nejsou pro čištění stanoveny.
- Pět hodnot `AUTO` znamená tentýž režim jako `auto`.
- Šest řádků je přesnou kopií včetně `record_id` a `state`. Identifikátory jsou jedinečné pro 720 původních situací, nikoli pro všech 726 řádků souboru.
- Některé velmi vysoké kladné hodnoty jsou skutečné vzácné situace v simulaci. Jejich výše není sama o sobě důvodem k odstranění.

### new-records.csv

Čtyři nové situace s týmž vstupním schématem, **bez sloupce `state`**. Obsahují chybějící vstupy a dosud neviděný režim `service`. Neobsahují kód −999 ani variantu `AUTO`. Výsledky predikce nejsou předem dodány a tento soubor není testovací množinou s dostupnou správnou odpovědí.

### grouped-records.csv

288 měření: 36 simulovaných zařízení, každé s 8 měřeními. Sloupce jsou `group_id`, `temperature`, `vibration`, `state`. Jednotky odpovídají hlavnímu souboru. Zařízení má společný provozní profil a v tomto příkladu i stejný cílový stav napříč svými měřeními. Řádky stejného zařízení proto nejsou nezávislé. Soubor neobsahuje chybějící hodnoty. `group_id` vyjadřuje hranici skupiny pro dělení dat, nikoli vstup modelu. Žádné zařízení není totožné se situací v hlavním souboru.

### time-series.csv

240 řádků pro předpověď následující hodiny. Řada má hodinový krok; hodnoty jsou v ilustračních bezrozměrných jednotkách. Neobsahuje chybějící hodnoty.

| Sloupec | Význam a dostupnost |
|---|---|
| timestamp | Čas vydání předpovědi, od 2025-01-01 01:00 |
| current_value | Měření známé v čase `timestamp` |
| lag1 | Měření známé o jednu hodinu dříve |
| next_value | Cíl: skutečně simulované měření o jednu hodinu později |
| target_available_time | Čas, kdy se `next_value` stane známým; `timestamp` + 1 hodina |

Generátor nejprve vytvoří 242 měření. Posun těchto pozorování vytvoří zpožděný příznak a cíl. První řádek bez předchozí hodnoty a poslední řádek bez budoucího výsledku se do souboru nezařadí. Poslední exportovaný cíl tedy pochází z existujícího simulovaného měření. Při učení modelu v určitém čase mohou být použity pouze cíle s `target_available_time` nejvýše rovným tomuto času. Shoda času znamená, že právě doručené měření již je dostupné. Závislost v čase vylučuje interpretaci tohoto souboru jako nezávislých náhodně zaměnitelných řádků.

## English

All five files contain **synthetic data**, generated deterministically by `../prepare_data.py` with base seed 20261110. They are not records of real devices or people. Units and relationships are illustrative; the generator is not a physical machine model. No personal data or reference model predictions are included. Data preparation takes place before the lab, separately from student tasks.

### stratification-records.csv

A fixed miniature table for the independent stratification task: 120 rows with columns `state` and `load`. Labels `normal`, `warning`, and `fault` occur 84, 24, and 12 times respectively. These are artificial categories, not diagnoses of real devices. `load` contains 120 distinct, evenly spaced values from 10 to 100 in illustrative percent units. There are no missing values, timestamps, or group identifiers. Row order has no temporal meaning. Numeric values and row order match the example's original miniature table.

### machine-records.csv

720 independent simulated operating situations plus 6 exact copied records, giving 726 CSV rows. Situations are neither consecutive measurements of one machine nor repeated measurements of the same devices. The basic task treats the original situations as independent draws from one generating process; the six added copies deliberately violate this condition. Correlation among features within a row does not imply dependence between separate situations.

| Column | Meaning | Illustrative unit / values |
|---|---|---|
| record_id | Situation identifier, not a predictive input | R0001 to R0720 |
| temperature | Temperature | °C |
| vibration | Vibration magnitude | mm/s |
| pressure | Pressure | kPa |
| power | Power consumption | W |
| speed | Rotational speed | rpm |
| load | Relative load | % |
| mode | Unordered operating mode | auto, manual, eco |
| environment | Operating environment | indoor, outdoor |
| state | Target condition | 0 normal simulated state, 1 simulated state requiring inspection |

Numeric inputs have different scales and some are correlated. Large numeric magnitudes do not necessarily indicate greater relevance to the target. Class 1 represents approximately one quarter to one third of the independent situations.

Deliberate boundary cases:

- Each of the eight input columns contains 36 missing entries among the original 720 situations, exactly 5%. Empty fields mean missing information, not zero or a category named “nan”. Copied records may slightly increase the total count of missing fields.
- Four observed temperatures are replaced by **−999**, the only explicitly defined invalid numeric code. No other universal numeric cleaning limits are specified.
- Five `AUTO` entries denote the same mode as `auto`.
- Six rows are exact copies including `record_id` and `state`. Identifiers are unique among the original 720 situations, not among all 726 exported rows.
- Some high positive extremes are genuine rare simulated situations. Magnitude alone is not a reason to remove them.

### new-records.csv

Four new situations with the same input schema and **no `state` column**. They contain missing inputs and the previously unseen mode `service`. Neither −999 nor `AUTO` occurs. No predictions are supplied, and this is not a labelled test set.

### grouped-records.csv

288 measurements: 36 simulated devices with 8 measurements each. Columns are `group_id`, `temperature`, `vibration`, `state`, with the same illustrative units as above. Each device shares an operating profile and, in this example, one target condition across its measurements. Rows from the same device are therefore dependent. No values are missing. `group_id` defines a splitting group, not a model input. These devices are separate from the independent situations in the main file.

### time-series.csv

240 rows for next-hour prediction, sampled at regular hourly intervals in illustrative dimensionless units. There are no missing values.

| Column | Meaning and availability |
|---|---|
| timestamp | Forecast issue time, starting at 2025-01-01 01:00 |
| current_value | Measurement available at `timestamp` |
| lag1 | Measurement available one hour earlier |
| next_value | Target: an actually simulated measurement one hour later |
| target_available_time | Time when `next_value` becomes known: `timestamp` + 1 hour |

The generator first creates 242 measurements. Shifts of those observations produce the lagged feature and target. The first row without a previous measurement and the last row without a future outcome are excluded. The final exported target therefore comes from an existing simulated observation. When fitting a model at a given time, only targets with `target_available_time` no later than that time are available. Equality means that the newly arrived measurement is already known. Temporal dependence means these rows are not independent, randomly exchangeable observations.
