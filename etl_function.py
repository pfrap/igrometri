import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import glob

lista_stanze=["Soggiorno", "Cucina", "Balcone_est", "Balcone_nord", "Bagno", "Camera_2"]
source_folder="./sensor/"

def estrazione_igrometri(lista_stanze:list, source:str):
    """Funzione che cicla sopra i file in cartella contenente csv ottenuti da igrometri, estrae i dati, concatena i dataframe, 
    modifica nomi e ordine colonne ed esporta un csv."""
    
    now=datetime.now().strftime('%Y%m%d_%H-%M-%S')
    log_file=f"./log_files/{now} - log_file.txt"
    def log(message):
        "Semplice funzione di log"
        with open (log_file,"a") as log:
            log.write(f"{now}: {message}\n")

    log("Creo df_igrometri") 
    df_igrometri=pd.DataFrame()
    
    #ESTRAZIONE DATI
    for n in lista_stanze:
        log(f"Cerco stanza {n}")
        df=pd.DataFrame()
        for file in glob.glob(f"{source}*{n}*.csv"):
            df_temperatura=pd.read_csv(file)
            log(f"df temperatura {n}: {df_temperatura.shape}")

            #TRASFORMAZIONE DATI
            #Inizio condizione particolare utilizzata per i primi csv estratti che erano in formato diverso.
            if df_temperatura.columns[0]=="Date":
                df_temperatura.rename(columns={'Date': 'data','Temp': 'temperatura','Umidità': 'umidita','Remark': 'note'}, inplace=True)
            if df_temperatura.columns[0]=="time":
                df_temperatura.rename(columns={'time': 'data','temperature': 'temperatura','humidity': 'umidita','note': 'note'}, inplace=True)
            #Fine condizione particolare
            df=pd.concat([df,df_temperatura],ignore_index=True).drop_duplicates("data",ignore_index=True)

            df.drop(columns=["note"], inplace=True)
            df["stanza"]=n
            
            log(f"df stanza {n}: {df_temperatura.shape}")
        
        df_igrometri=pd.concat([df_igrometri,df],ignore_index=True)
        df_igrometri.drop(columns=["Unnamed: 4"], inplace=True, errors="ignore")
        log(f"df_igrometri: {df_igrometri.shape}")

    #TRASFORMAZIONE DATI
    # Modifica dtypes delle colonne
    df_igrometri["temperatura"]=df_igrometri["temperatura"].str.replace("℃","")
    df_igrometri["umidita"]=df_igrometri["umidita"].str.replace("%","")
    df_igrometri["stanza"]=df_igrometri["stanza"].astype(str)
    df_igrometri["temperatura"]=df_igrometri["temperatura"].astype(float)
    df_igrometri["umidita"]=df_igrometri["umidita"].astype(float)
    df_igrometri["data"]=pd.to_datetime(df_igrometri["data"])
    
    #LOAD
    df_igrometri.to_csv("igrometri.csv", columns=["data","stanza","temperatura","umidita"], index=False)
    log(f"Esportazione csv.")
    df_igrometri.sort_values(by=["data"], inplace=True)
    return df_igrometri

#Chiama funzione
df_igrometri=estrazione_igrometri(lista_stanze, source_folder)