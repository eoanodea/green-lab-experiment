import os
import pandas as pd
import numpy as np

class Batterymanager:
    @staticmethod
    def preprocess_values(df):
        # Verifica se la colonna 'Timestamp' esiste nel DataFrame
        df['Timestamp'] = df['Timestamp'] - df['Timestamp'].iloc[0]
        # conversione da microsecondi a secondi
        df['Timestamp'] = df['Timestamp'] / 1000
        return df

    @staticmethod
    def calculate_power(df):
        df['power'] = (abs(df['BATTERY_PROPERTY_CURRENT_NOW']) / 1000 / 1000) * (df['EXTRA_VOLTAGE'] / 1000)
        return df

    @staticmethod
    def trapezoid_method(df):
        return np.trapz(df['power'].values, df['Timestamp'].values)

    @staticmethod
    def aggregate_batterymanager_runs():
        current_dir = os.path.dirname(os.path.abspath(__file__))  # Ottieni la directory corrente
        data_dir = os.path.join(current_dir, "data")  # Percorso alla cartella "data"
        runs = pd.DataFrame()
        run_number = 0

        for run_file in [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]:
            if run_file.endswith(".csv"):
                try:
                    run_df = pd.read_csv(os.path.join(data_dir, run_file))
                    if not run_df.empty:
                        stats = {}
                        if 'BATTERY_PROPERTY_CURRENT_NOW' in run_df.columns and 'EXTRA_VOLTAGE' in run_df.columns:
                            run_df = Batterymanager.preprocess_values(run_df)
                            run_df = Batterymanager.calculate_power(run_df)
                            avg_power = run_df['power'].mean()
                            stats.update({'Avg power (W)': avg_power})
                            stats.update({'Energy simple (J)': avg_power * run_df['Timestamp'].max()})
                            stats.update({'Energy trapz (J)': Batterymanager.trapezoid_method(run_df)})
                        stats.update(run_df.mean().to_dict())
                        stats.update({'run': run_number})
                        run_number += 1
                        runs = pd.concat([runs, pd.DataFrame(stats, index=[0])], ignore_index=True)
                except pd.errors.EmptyDataError:
                    pass

        runs = runs.drop(columns=['Timestamp', 'power'], axis=1)
        return runs

    @staticmethod
    def aggregate_end(output_file="output.csv"):
        print('Output file: {}'.format(output_file))
        rows = Batterymanager.aggregate_batterymanager_runs()
        print(rows)  # Stampa i dati prima di salvarli
        rows.to_csv(output_file, index=False)

# Esegui l'aggregazione e salva i risultati in "output.csv"
Batterymanager.aggregate_end()
