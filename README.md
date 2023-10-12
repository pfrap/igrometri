# The sensor project
L'anno scorso ho comprato dei meravigliosi igrometri di una non meglio identificata marca cinese, [Oria](https://www.amazon.it/gp/product/B08GKB5D1M/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1).

Devo dire che per il prezzo funzionano bene, semplici da utilizzare ed esteticamente piacevoli.

Ne ho presi sei e li ho utilizzati per monitorare la temperatura ambientale in alcune stanze di casa mia.

## Business case
Principalmente mi interessava sperimentare nel campo dell'acquisizione di dati ambientali, la loro organizzazione ed archiviazione.

Secondariamente volevo vedere quanto potessero differire le temperature rilevate all'interno rispetto a quelle rilevate sui terrazzi.

Infine volevo controllare la temperatura nella camera dei miei figli.

## Preparazione dei dati
Gli igrometri Oria rilevano temperatura (°C) e umidità relativa (%) ogni 10 minuti.
Li ho utilizzati da Marzo ad Ottobre 2023, non senza problemi.

Non era chiarissimo il funzionamento visto che le istruzioni erano in cinese, il trasferimento delle informazioni avviene tramite app sul telefono via bluetooth e la sincronizzazione non è molto ben studiata.
I dati infatti vengono autodistrutti sui dispositivi dopo il 100 giorno e non mi è ancora chiarissimo come gestire questa cosa.

Sintesi: **i dati non sono di qualità**, a tratti mancanti.

## Execution
### Importazione dati
L'app forniva appunto una scomodissima funzione di export in csv che potevi poi mandare alla email.

* Ho importato i csv su dataframe Pandas.
* Ho unito i dataframe delle stesse stanze tra di loro tramite *merge*.
* Ho modificato i dtypes per avere.  
    * Temperatura: float  
    * Umidità: float64
    * Data: datetime64[ns]
* Matplotlib per plottare i dati

### Analisi dei dati
Ho utilizzato principalmente dati ottenuti tramite *moving average*, essendo infatti dati puntuali ogni 10 minuti ho trovato più indicato sintetizzarli in una media mobile differente a seconda del tipo di analisi - di solito media mobile di 1 ora, 12 ore e 24 ore.

## Grafici
### Temperatura giornaliera delle stanze
* Media mobile 1 giorno
* Tutte le stanze in grafico a linea
* *x = tempo, y = temperatura °C*

![Graph](/grafici/Temperatura%20°C%20-%20daily%20running%20average.jpg)

### Temperatura giornaliera delle stanze
* Media mobile 1 giorno
* Tutte le stanze in grafici multipli
* Messa a confronto con la temperatura media di tutte le stanze
* *x = tempo, y = temperatura °C*

![Graph](/grafici/Andamento%20temperatura%20media%20giornaliera%20°C.jpg)

### Percentuale di umidità giornaliera delle stanze
* Media mobile 1 giorno
* Tutte le stanze in grafici multipli
* Messa a confronto con la percentuali medie di tutte le stanze
* *x = tempo, y = umidità %*

![Graph](/grafici/Andamento%20della%20percentuale%20di%20umidità%20media%20giornaliera.jpg)

### Differenza tra interno ed esterno nella variabilità delle temperature ogni 12 ore
* Media mobile 1 ora / Media mobile 12 ore
* Interno (soggiorno), esterno (balcone est)
* *x = tempo, y = percentuale di variazione*

![Graph](/grafici/Percentuale%20variazione%20della%20media%20oraria%20rispetto%20a%20media%20ogni%2012%20ore.jpg)

### Andamento temperature ogni 12 ore, interno ed esterno
* Media mobile 12 ore
* Interno (soggiorno), esterno (balcone est)
* *x = tempo, y = temperatura °C*

![Graph](/grafici/Contronto%20media%20ogni%2012%20ore%20Soggiorno%20e%20Balcone%20est.jpg)

### Andamento temperature stanza bagno
* Media mobile 24 ore
* Media mobile 1 ora
* *x = tempo, y = temperatura °C*

![Graph](/grafici/Andamento%20temperatura%20bagno.jpg)

### Calendar heatmap
Con [Tableau](https://public.tableau.com/views/sensor-project/TempCdashboard?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link) ho impostato una calendar heatmap delle varie stanze per vedere la distribuzione delle temperature medie nelle varie stanze durante l'anno.

![Heatpmap](/grafici/Temperature%20°C%20calendar%20heatmap.png)