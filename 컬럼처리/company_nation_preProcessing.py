import pandas as pd 

data = pd.read_csv('company&nation.csv', encoding='utf-8')
 
print( len( data['NATION_NM'].unique() ) )
print( len( data['COMPANY_NM'].unique() ) )

data['NATION_NM'] = data['NATION_NM'].str.replace(' ', '')
data['NATION_NM'] = data['NATION_NM'].str.split('/')
data['NATION_NM'] = data['NATION_NM'].apply(lambda x : sorted(x))
data['NATION_NM'] = data['NATION_NM'].apply(lambda x : str(x).strip('[]'))
data['NATION_NM'] = data['NATION_NM'].apply(lambda x : x.replace("'", ""))
data['NATION_NM'] = data['NATION_NM'].apply(lambda x : x.replace(", ", "/"))


data['COMPANY_NM'] = data['COMPANY_NM'].str.replace(' ', '')
data['COMPANY_NM'] = data['COMPANY_NM'].fillna('')
data['COMPANY_NM'] = data['COMPANY_NM'].str.split('/')
data['COMPANY_NM'] = data['COMPANY_NM'].apply(lambda x : sorted(x))
data['COMPANY_NM'] = data['COMPANY_NM'].apply(lambda x : str(x).strip('[]'))
data['COMPANY_NM'] = data['COMPANY_NM'].apply(lambda x : x.replace("'", ""))
data['COMPANY_NM'] = data['COMPANY_NM'].apply(lambda x : x.replace(", ", "/"))

    
print(data)

# print(data.iloc[100:150, 3])


# data.to_csv('company&nation_new.csv')

print( len( data['NATION_NM'].unique() ) )
print( len( data['COMPANY_NM'].unique() ) )
