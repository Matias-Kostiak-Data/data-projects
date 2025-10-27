"""
Generador de datos sintéticos usando SDV (Synthetic Data Vault) para crear datasets más realistas.
Mantiene las distribuciones y correlaciones del dataset original.
"""

import argparse
from pathlib import Path
import pandas as pd
import numpy as np
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker(['es_ES'])  # Configurado para español

class DatasetSynthesizer:
    def __init__(self, seed=42):
        self.seed = seed
        random.seed(seed)
        np.random.seed(seed)
        Faker.seed(seed)

    def _train_synthesizer(self, data, metadata):
        synthesizer = GaussianCopulaSynthesizer(metadata)
        synthesizer.fit(data)
        return synthesizer

    def generate_ventas(self, input_path, output_path, multiplier=50):
        """Genera datos sintéticos para el dataset de ventas"""
        df = pd.read_csv(input_path)
        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data=df)
        
        # Configurar tipos específicos
        metadata.update_column(column_name='venta_id', sdtype='id')
        metadata.update_column(column_name='cliente_id', sdtype='categorical')
        metadata.update_column(column_name='producto_id', sdtype='categorical')
        metadata.update_column(column_name='fecha', sdtype='datetime')
        metadata.update_column(column_name='cantidad', sdtype='numerical')

        synthesizer = self._train_synthesizer(df, metadata)
        num_samples = len(df) * multiplier
        synthetic_data = synthesizer.sample(num_rows=num_samples)

        # Asegurar que los IDs sean únicos y consecutivos
        synthetic_data['venta_id'] = range(len(df) + 1, len(df) + len(synthetic_data) + 1)
        synthetic_data['fecha'] = pd.to_datetime(synthetic_data['fecha']).dt.strftime('%Y-%m-%d')
        
        # Combinar datos originales y sintéticos
        result = pd.concat([df, synthetic_data], ignore_index=True)
        result = result.sort_values('fecha').reset_index(drop=True)
        
        # Guardar resultado
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output_path, index=False)
        print(f"Ventas ampliadas: {result.shape} -> {output_path}")
        return result

    def generate_clima(self, input_path, output_path, multiplier=50):
        """Genera datos sintéticos para el dataset de clima"""
        df = pd.read_csv(input_path)
        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data=df)
        
        metadata.update_column(column_name='fecha', sdtype='datetime')
        metadata.update_column(column_name='ciudad', sdtype='categorical')
        metadata.update_column(column_name='temp_c', sdtype='numerical')
        metadata.update_column(column_name='humedad', sdtype='numerical')

        synthesizer = self._train_synthesizer(df, metadata)
        num_samples = len(df) * multiplier
        synthetic_data = synthesizer.sample(num_rows=num_samples)

        # Ajustar valores generados
        synthetic_data['temp_c'] = synthetic_data['temp_c'].round().astype(int)
        synthetic_data['humedad'] = synthetic_data['humedad'].round().clip(0, 100).astype(int)
        synthetic_data['fecha'] = pd.to_datetime(synthetic_data['fecha']).dt.strftime('%Y-%m-%d')

        # Combinar y ordenar
        result = pd.concat([df, synthetic_data], ignore_index=True)
        result = result.sort_values(['fecha', 'ciudad']).reset_index(drop=True)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output_path, index=False)
        print(f"Clima ampliado: {result.shape} -> {output_path}")
        return result

    def generate_opiniones(self, input_path, output_path, multiplier=50):
        """Genera datos sintéticos para el dataset de opiniones"""
        df = pd.read_csv(input_path)
        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data=df)
        
        metadata.update_column(column_name='tweet_id', sdtype='id')
        metadata.update_column(column_name='usuario', sdtype='categorical')
        metadata.update_column(column_name='fecha', sdtype='datetime')

        # Para el texto, usaremos templates y Faker
        templates = [
            "Me encanta {tema} 🚀",
            "Aprendiendo sobre {tema} 💡",
            "Hoy logré dominar {tema} ✨",
            "Increíble experiencia con {tema} 💪",
            "Necesito ayuda con {tema} 🤔",
            "Compartiendo conocimiento sobre {tema} 📚",
            "Practicando {tema} hoy 💻",
            "Nuevo proyecto usando {tema} 🎯",
            "Resolviendo problemas de {tema} 🔧",
            "Avanzando en mi aprendizaje de {tema} 📈"
        ]
        
        temas = [
            "Python", "SQL", "pandas", "data science", "machine learning",
            "visualización de datos", "ETL", "análisis de datos", "big data",
            "estadística", "bases de datos", "data engineering", "power BI",
            "tableau", "deep learning", "docker", "AWS", "cloud computing",
            "data mining", "business intelligence"
        ]

        synthesizer = self._train_synthesizer(df[['tweet_id', 'usuario', 'fecha']], metadata)
        num_samples = len(df) * multiplier
        synthetic_data = synthesizer.sample(num_rows=num_samples)

        # Generar textos más variados y realistas
        synthetic_data['texto'] = [
            random.choice(templates).format(tema=random.choice(temas)) + " " + fake.sentence()
            for _ in range(len(synthetic_data))
        ]

        # Asegurar IDs únicos y fechas correctas
        synthetic_data['tweet_id'] = range(len(df) + 1, len(df) + len(synthetic_data) + 1)
        synthetic_data['fecha'] = pd.to_datetime(synthetic_data['fecha']).dt.strftime('%Y-%m-%d')

        # Combinar y ordenar
        result = pd.concat([df, synthetic_data], ignore_index=True)
        result = result.sort_values('fecha').reset_index(drop=True)
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        result.to_csv(output_path, index=False)
        print(f"Opiniones ampliadas: {result.shape} -> {output_path}")
        return result

def main():
    parser = argparse.ArgumentParser(description='Generar datos sintéticos realistas')
    parser.add_argument('--dir', type=str, required=False, default='.',
                      help='Directorio con proyectos (default: .)')
    parser.add_argument('--out-dir', type=str, required=False, default='.',
                      help='Directorio de salida')
    parser.add_argument('--n-multiplier', type=int, required=False, default=50,
                      help='Multiplicador de tamaño (default: 50)')
    parser.add_argument('--seed', type=int, required=False, default=42,
                      help='Semilla para reproducibilidad')
    args = parser.parse_args()

    base_dir = Path(args.dir)
    out_dir = Path(args.out_dir)
    
    synthesizer = DatasetSynthesizer(seed=args.seed)

    # Procesar cada dataset
    datasets = [
        ('Proyecto_1_Ecommerce/proyecto1_ventas.csv', 'proyecto1_ventas_augmented.csv', synthesizer.generate_ventas),
        ('Proyecto_2_Clima/proyecto2_clima.csv', 'proyecto2_clima_augmented.csv', synthesizer.generate_clima),
        ('Proyecto_3_Opiniones/proyecto3_opiniones.csv', 'proyecto3_opiniones_augmented.csv', synthesizer.generate_opiniones)
    ]

    for input_file, output_file, generator in datasets:
        input_path = base_dir / input_file
        if input_path.exists():
            generator(input_path, out_dir / output_file, args.n_multiplier)
        else:
            print(f"No se encontró {input_path}")

if __name__ == '__main__':
    main()