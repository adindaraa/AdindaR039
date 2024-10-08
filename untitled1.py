# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nNtrdN40mpn7Y-aHWg02jnkIYjVeX2u2
"""

import pandas as pd
# Memuat data dari file csv
df = pd.read_csv('movie_sample_dataset.csv')
# Menampilkan 5 baris pertama dari dataset
df.head()

import pandas as pd

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Memeriksa informasi umum tentang dataset
print("Informasi umum dataset:")
print(df.info())

# Memeriksa apakah ada nilai yang hilang
print("\nJumlah nilai yang hilang di setiap kolom:")
print(df.isnull().sum())

# Melihat beberapa baris pertama data
print("\nBeberapa baris pertama dari dataset:")
print(df.head())

import pandas as pd

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Memeriksa informasi umum dataset setelah penghapusan
print("Informasi dataset setelah menghapus baris dengan nilai NaN di kolom 'gross' dan 'budget':")
print(df_clean.info())

# Memeriksa jumlah nilai yang hilang setelah penghapusan
print("\nJumlah nilai yang hilang di setiap kolom setelah penghapusan:")
print(df_clean.isnull().sum())

# Melihat beberapa baris pertama dari data yang telah dibersihkan
print("\nBeberapa baris pertama dari dataset yang telah dibersihkan:")
print(df_clean.head())

import pandas as pd

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Menormalkan teks di kolom tertentu, misalnya kolom 'color'
# Ubah semua nilai di kolom 'color' menjadi huruf kecil
if 'color' in df_clean.columns:
    df_clean['color'] = df_clean['color'].str.lower()

# Periksa apakah ada perbedaan penulisan lain di kolom tertentu, seperti 'Color' atau 'Genre'
# Anda bisa menambahkan kolom lain sesuai kebutuhan
print("Nilai unik di kolom 'color' setelah normalisasi:")
print(df_clean['color'].unique())

# Memeriksa informasi dataset setelah normalisasi
print("\nInformasi dataset setelah normalisasi:")
print(df_clean.info())

# Melihat beberapa baris pertama dari data yang telah dibersihkan
print("\nBeberapa baris pertama dari dataset yang telah dinormalisasi:")
print(df_clean.head())

import pandas as pd
import numpy as np

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Menormalkan teks di kolom tertentu, misalnya kolom 'color'
if 'color' in df_clean.columns:
    df_clean['color'] = df_clean['color'].str.lower()

# Mengubah nilai 'N/A' menjadi NaN di seluruh DataFrame
df_clean.replace('N/A', np.nan, inplace=True)

# Menghapus nilai negatif di kolom 'gross' dan 'budget'
df_clean = df_clean[(df_clean['gross'] >= 0) & (df_clean['budget'] >= 0)]

# Memeriksa hasil setelah pembersihan
print("Informasi dataset setelah mengatasi nilai yang tidak standar:")
print(df_clean.info())

# Memeriksa apakah masih ada nilai yang tidak standar
print("\nBeberapa baris pertama dari dataset yang telah dibersihkan dari nilai tidak standar:")
print(df_clean.head())

import pandas as pd
import numpy as np

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Menormalkan teks di kolom tertentu, misalnya kolom 'color'
if 'color' in df_clean.columns:
    df_clean['color'] = df_clean['color'].str.lower()

# Mengubah nilai 'N/A' menjadi NaN di seluruh DataFrame
df_clean.replace('N/A', np.nan, inplace=True)

# Menghapus nilai negatif di kolom 'gross' dan 'budget'
df_clean = df_clean[(df_clean['gross'] >= 0) & (df_clean['budget'] >= 0)]

# Konversi kolom 'budget' dan 'gross' menjadi numerik
df_clean['budget'] = pd.to_numeric(df_clean['budget'], errors='coerce')
df_clean['gross'] = pd.to_numeric(df_clean['gross'], errors='coerce')

# Memeriksa apakah tipe data sudah benar
print("Tipe data kolom setelah konversi:")
print(df_clean.dtypes)

# Memeriksa beberapa baris pertama dari dataset yang telah dibersihkan
print("\nBeberapa baris pertama dari dataset yang telah dikonversi:")
print(df_clean.head())

import pandas as pd
import numpy as np

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Menormalkan teks di kolom tertentu, misalnya kolom 'color'
if 'color' in df_clean.columns:
    df_clean['color'] = df_clean['color'].str.lower()

# Mengubah nilai 'N/A' menjadi NaN di seluruh DataFrame
df_clean.replace('N/A', np.nan, inplace=True)

# Menghapus nilai negatif di kolom 'gross' dan 'budget'
df_clean = df_clean[(df_clean['gross'] >= 0) & (df_clean['budget'] >= 0)]

# Konversi kolom 'budget' dan 'gross' menjadi numerik
df_clean['budget'] = pd.to_numeric(df_clean['budget'], errors='coerce')
df_clean['gross'] = pd.to_numeric(df_clean['gross'], errors='coerce')

# Memisahkan genre yang bergabung dalam satu kolom menjadi beberapa kolom terpisah
if 'genre' in df_clean.columns:
    genres_split = df_clean['genre'].str.split(',', expand=True)

    # Menggabungkan hasil pemisahan dengan DataFrame asli
    df_clean = pd.concat([df_clean, genres_split], axis=1)

    # Memberi nama kolom untuk genre terpisah
    num_genres = genres_split.shape[1]
    genre_columns = [f'genre_{i+1}' for i in range(num_genres)]
    df_clean.rename(columns={i: genre_columns[i] for i in range(num_genres)}, inplace=True)

# Memeriksa beberapa baris pertama dari dataset yang telah dipisahkan
print("\nDataset dengan genre yang dipisah menjadi beberapa kolom:")
print(df_clean.head())

import pandas as pd
import numpy as np

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Mengubah nilai 'N/A' menjadi NaN di seluruh DataFrame
df_clean.replace('N/A', np.nan, inplace=True)

# Menghapus nilai negatif di kolom 'gross' dan 'budget'
df_clean = df_clean[(df_clean['gross'] >= 0) & (df_clean['budget'] >= 0)]

# Konversi kolom 'budget' dan 'gross' menjadi numerik
df_clean['budget'] = pd.to_numeric(df_clean['budget'], errors='coerce')
df_clean['gross'] = pd.to_numeric(df_clean['gross'], errors='coerce')

# Memisahkan genre yang bergabung dalam satu kolom menjadi beberapa kolom terpisah
if 'genre' in df_clean.columns:
    genres_split = df_clean['genre'].str.split(',', expand=True)
    df_clean = pd.concat([df_clean, genres_split], axis=1)

    # Memberi nama kolom untuk genre terpisah
    num_genres = genres_split.shape[1]
    genre_columns = [f'genre_{i+1}' for i in range(num_genres)]
    df_clean.rename(columns={i: genre_columns[i] for i in range(num_genres)}, inplace=True)

# Normalisasi teks: Mengubah teks dalam kolom tertentu menjadi huruf kecil
text_columns = ['color', 'genre', 'director', 'actor', 'language']  # Daftar kolom yang ingin dinormalisasi

for col in text_columns:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].str.lower()

# Memeriksa beberapa baris pertama dari dataset setelah normalisasi teks
print("\nDataset setelah normalisasi teks:")
print(df_clean.head())

import pandas as pd
import numpy as np

# Memuat data dari file CSV
df = pd.read_csv('movie_sample_dataset.csv')

# Menghapus baris yang memiliki nilai NaN di kolom 'gross' dan 'budget'
df_clean = df.dropna(subset=['gross', 'budget'])

# Mengubah nilai 'N/A' menjadi NaN di seluruh DataFrame
df_clean.replace('N/A', np.nan, inplace=True)

# Menghapus nilai negatif di kolom 'gross' dan 'budget'
df_clean = df_clean[(df_clean['gross'] >= 0) & (df_clean['budget'] >= 0)]

# Konversi kolom 'budget' dan 'gross' menjadi numerik
df_clean['budget'] = pd.to_numeric(df_clean['budget'], errors='coerce')
df_clean['gross'] = pd.to_numeric(df_clean['gross'], errors='coerce')

# Memisahkan genre yang bergabung dalam satu kolom menjadi beberapa kolom terpisah
if 'genre' in df_clean.columns:
    genres_split = df_clean['genre'].str.split(',', expand=True)
    df_clean = pd.concat([df_clean, genres_split], axis=1)

    # Memberi nama kolom untuk genre terpisah
    num_genres = genres_split.shape[1]
    genre_columns = [f'genre_{i+1}' for i in range(num_genres)]
    df_clean.rename(columns={i: genre_columns[i] for i in range(num_genres)}, inplace=True)

# Normalisasi teks: Mengubah teks dalam kolom tertentu menjadi huruf kecil
text_columns = ['color', 'genre', 'director', 'actor', 'language']  # Daftar kolom yang ingin dinormalisasi

for col in text_columns:
    if col in df_clean.columns:
        df_clean[col] = df_clean[col].str.lower()

# Menyimpan dataset yang telah diproses ke dalam file CSV baru
df_clean.to_csv('movie_dataset_cleaned.csv', index=False)

print("Dataset telah disimpan ke file 'movie_dataset_cleaned.csv'.")