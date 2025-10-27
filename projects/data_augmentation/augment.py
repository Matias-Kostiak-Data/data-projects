"""
Generador simple de datasets ampliados para el repositorio Data-projects.
- Usa pandas y Faker para crear filas adicionales manteniendo tipos y algunas distribuciones.
- Genera tres archivos: ventas_augmented.csv, clima_augmented.csv, opiniones_augmented.csv

Uso:
    python augment.py --dir "..\Proyecto_1_Ecommerce" --out-dir "..\augmented" --n-multiplier 10

Nota: pensado para ejecutarse en Windows PowerShell.
"""
import argparse
import os
from pathlib import Path
import pandas as pd
from faker import Faker
import random

fake = Faker()


def augment_ventas(path, out_path, multiplier=10):
    df = pd.read_csv(path)
    # suposiciones: columnas ['venta_id','cliente_id','producto_id','fecha','cantidad']
    max_id = df['venta_id'].max()
    clients = df['cliente_id'].unique().tolist()
    products = df['producto_id'].unique().tolist()
    dates = pd.to_datetime(df['fecha'])
    start = dates.min()
    end = dates.max()

    rows = []
    for i in range(len(df) * multiplier):
        max_id += 1
        cliente = random.choice(clients + [fake.random_int(min=1, max=1000) for _ in range(3)])
        producto = random.choice(products + [fake.random_int(min=1, max=500) for _ in range(3)])
        fecha = fake.date_between(start_date=start, end_date=end)
        cantidad = random.choices([1,2,3,4,5], weights=[50,30,10,7,3])[0]
        rows.append([max_id, cliente, producto, fecha.strftime('%Y-%m-%d'), cantidad])

    df_new = pd.DataFrame(rows, columns=df.columns)
    df_out = pd.concat([df, df_new], ignore_index=True)
    out_path.mkdir(parents=True, exist_ok=True)
    out_file = out_path / 'proyecto1_ventas_augmented.csv'
    df_out.to_csv(out_file, index=False)
    print(f"Ventas ampliadas: {df_out.shape} -> {out_file}")


def augment_clima(path, out_path, multiplier=10):
    df = pd.read_csv(path)
    # columnas: ['fecha','ciudad','temp_c','humedad']
    cities = df['ciudad'].unique().tolist()
    dates = pd.to_datetime(df['fecha'])
    start = dates.min()
    end = dates.max()

    rows = []
    for i in range(len(df) * multiplier):
        fecha = fake.date_between(start_date=start, end_date=end)
        ciudad = random.choice(cities)
        # sample temperature around city mean
        city_mean = df[df['ciudad'] == ciudad]['temp_c'].mean()
        temp = int(random.gauss(mu=city_mean, sigma=3))
        humedad = int(random.gauss(mu=df['humedad'].mean(), sigma=5))
        rows.append([fecha.strftime('%Y-%m-%d'), ciudad, temp, max(0, min(100, humedad))])

    df_new = pd.DataFrame(rows, columns=df.columns)
    df_out = pd.concat([df, df_new], ignore_index=True)
    out_path.mkdir(parents=True, exist_ok=True)
    out_file = out_path / 'proyecto2_clima_augmented.csv'
    df_out.to_csv(out_file, index=False)
    print(f"Clima ampliado: {df_out.shape} -> {out_file}")


def augment_opiniones(path, out_path, multiplier=10):
    df = pd.read_csv(path)
    # columnas: ['tweet_id','usuario','texto','fecha']
    users = df['usuario'].unique().tolist()
    dates = pd.to_datetime(df['fecha'])
    start = dates.min()
    end = dates.max()

    sample_texts = [
        "Me gusta este curso",
        "Aprendiendo SQL",
        "Pandas me confunde",
        "Buscando trabajo en data",
        "Hoy hice un pipeline",
        "La nube es increíble",
        "Necesito practicar joins",
        "Aprendiendo sobre ETL",
        "Modelando datos con Python",
        "Debugging y tests"
    ]

    rows = []
    max_id = df['tweet_id'].max()
    for i in range(len(df) * multiplier):
        max_id += 1
        usuario = random.choice(users + [fake.user_name()])
        texto = random.choice(sample_texts) + ' ' + fake.sentence(nb_words=6)
        fecha = fake.date_between(start_date=start, end_date=end)
        rows.append([max_id, usuario, texto, fecha.strftime('%Y-%m-%d')])

    df_new = pd.DataFrame(rows, columns=df.columns)
    df_out = pd.concat([df, df_new], ignore_index=True)
    out_path.mkdir(parents=True, exist_ok=True)
    out_file = out_path / 'proyecto3_opiniones_augmented.csv'
    df_out.to_csv(out_file, index=False)
    print(f"Opiniones ampliadas: {df_out.shape} -> {out_file}")


def main():
    parser = argparse.ArgumentParser(description='Generar datasets ampliados')
    parser.add_argument('--dir', type=str, required=False, default='.', help='Directorio con proyectos (default: .)')
    parser.add_argument('--out-dir', type=str, required=False, default='./augmented', help='Directorio de salida')
    parser.add_argument('--n-multiplier', type=int, required=False, default=10, help='Multiplicador de tamaño (entero)')
    parser.add_argument('--method', type=str, required=False, default='faker', choices=['faker', 'sdv'], help='Método para generar datos: faker o sdv')
    parser.add_argument('--seed', type=int, required=False, default=None, help='Semilla opcional para reproducibilidad')
    args = parser.parse_args()

    base_dir = Path(args.dir)
    out_dir = Path(args.out_dir)
    if args.seed is not None:
        Faker.seed(args.seed)
        random.seed(args.seed)

    # paths esperados
    ventas_path = base_dir / 'Proyecto_1_Ecommerce' / 'proyecto1_ventas.csv'
    clima_path = base_dir / 'Proyecto_2_Clima' / 'proyecto2_clima.csv'
    opin_path = base_dir / 'Proyecto_3_Opiniones' / 'proyecto3_opiniones.csv'

    if ventas_path.exists():
        if args.method == 'sdv':
            try:
                from sdv.tabular import GaussianCopula
                df = pd.read_csv(ventas_path)
                model = GaussianCopula()
                model.fit(df)
                n_samples = len(df) * args.n_multiplier
                df_new = model.sample(n_samples)
                df_out = pd.concat([df, df_new], ignore_index=True)
                out_dir.mkdir(parents=True, exist_ok=True)
                out_file = out_dir / 'proyecto1_ventas_augmented.csv'
                df_out.to_csv(out_file, index=False)
                print(f"Ventas ampliadas (sdv): {df_out.shape} -> {out_file}")
            except Exception as e:
                print(f"SDV falló para ventas: {e}. Volviendo a faker.")
                augment_ventas(ventas_path, out_dir, multiplier=args.n_multiplier)
        else:
            augment_ventas(ventas_path, out_dir, multiplier=args.n_multiplier)
    else:
        print(f"No se encontró {ventas_path}")

    if clima_path.exists():
        if args.method == 'sdv':
            try:
                from sdv.tabular import GaussianCopula
                df = pd.read_csv(clima_path)
                model = GaussianCopula()
                model.fit(df)
                n_samples = len(df) * args.n_multiplier
                df_new = model.sample(n_samples)
                df_out = pd.concat([df, df_new], ignore_index=True)
                out_dir.mkdir(parents=True, exist_ok=True)
                out_file = out_dir / 'proyecto2_clima_augmented.csv'
                df_out.to_csv(out_file, index=False)
                print(f"Clima ampliado (sdv): {df_out.shape} -> {out_file}")
            except Exception as e:
                print(f"SDV falló para clima: {e}. Volviendo a faker.")
                augment_clima(clima_path, out_dir, multiplier=args.n_multiplier)
        else:
            augment_clima(clima_path, out_dir, multiplier=args.n_multiplier)
    else:
        print(f"No se encontró {clima_path}")

    if opin_path.exists():
        if args.method == 'sdv':
            try:
                from sdv.tabular import GaussianCopula
                df = pd.read_csv(opin_path)
                # SDV won't model free-text well; drop 'texto' column for modeling and regenerate with Faker
                texto_col = 'texto' if 'texto' in df.columns else None
                model_df = df.drop(columns=[texto_col]) if texto_col else df
                model = GaussianCopula()
                model.fit(model_df)
                n_samples = len(df) * args.n_multiplier
                df_new = model.sample(n_samples)
                # regenerate texto with Faker
                textos = [fake.sentence(nb_words=8) for _ in range(len(df_new))]
                if texto_col:
                    df_new[texto_col] = textos
                df_out = pd.concat([df, df_new], ignore_index=True)
                out_dir.mkdir(parents=True, exist_ok=True)
                out_file = out_dir / 'proyecto3_opiniones_augmented.csv'
                df_out.to_csv(out_file, index=False)
                print(f"Opiniones ampliadas (sdv): {df_out.shape} -> {out_file}")
            except Exception as e:
                print(f"SDV falló para opiniones: {e}. Volviendo a faker.")
                augment_opiniones(opin_path, out_dir, multiplier=args.n_multiplier)
        else:
            augment_opiniones(opin_path, out_dir, multiplier=args.n_multiplier)
    else:
        print(f"No se encontró {opin_path}")


if __name__ == '__main__':
    main()
