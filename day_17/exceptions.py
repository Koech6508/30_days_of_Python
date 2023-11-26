#Python uses try and except to handle errors gracefully
#Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
nordic_countries,*rest,es,ru = names[:5] ,names[5],names[6]
print('Nordic Countries:' , nordic_countries)
print('Estonia:' , es)
print('Russia:', ru)

      