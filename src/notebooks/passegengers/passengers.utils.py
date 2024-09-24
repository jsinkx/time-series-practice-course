__SHARED_PATH = os.path.join(os.getcwd(), 'passengers.shared.py')

with open(__SHARED_PATH) as file:
    exec(file.read())

def get_not_nan_rows(df, column):
  not_nan_rows = df[df['missing'].notna()] 
  
  return not_nan_rows

def compare_fills(df, target_column ='target'):
  df['Month'] = pd.to_datetime(df['Month'])

  plt.figure(figsize=(10, 6))
  plt.plot(df['Month'], df['reference'], label='Reference', color=ENUM_COLORS['BLUE'], linestyle='-')
  plt.plot(df['Month'], df[target_column], label=target_column, color=ENUM_COLORS['RED'], linestyle='--')

  plt.title(f'График данных по {target_column} и reference')
  plt.xlabel('Год')
  plt.ylabel('Значения')
  plt.legend()
  plt.show()