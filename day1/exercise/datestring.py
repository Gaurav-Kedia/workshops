month2mm = { 'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12 }

COMMA = ','
SPACE = ' '
date_str = raw_input('Enter a date string? ')
date_str = date_str.replace( COMMA, SPACE)
d, m, y = date_str.split()
dd = int( d )
mon = m[:3].upper()
mm = month2mm[mon]
yyyy = int( y )

print dd,mm, yyyy
